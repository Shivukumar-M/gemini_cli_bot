import os
import requests
import json
import uuid
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

# Initialize Flask app
app = Flask(__name__)

# --- Helper Functions for File I/O ---

def writeFile(filename, data):
    """Writes data to a specified file."""
    try:
        # Define the base directory (where app.py is located)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, filename)
        
        # Security check: Prevent writing outside the current directory
        if not full_path.startswith(base_dir):
            return False, "Access denied: Cannot write outside the application directory."
            
        with open(full_path, "w", encoding='utf-8') as f:
            f.write(data)
        return True, f"File **'{filename}'** successfully created/updated."
    except IOError as e:
        return False, f"Error writing file '{filename}'. Reason: {e}"

def readFile(filename):
    """Reads content from a specified file."""
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, filename)
        
        if not full_path.startswith(base_dir):
            return False, "Access denied: Cannot read outside the application directory."

        with open(full_path, "r", encoding='utf-8') as f:
            content = f.read()
        return True, content
    except FileNotFoundError:
        return False, f"Error: The file **'{filename}'** was not found in the application directory."
    except IOError as e:
        return False, f"Error reading file '{filename}'. Reason: {e}"

# --- Configuration & Initialization ---

# Load API key from config.json or environment variable
api_key = None
try:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)
    api_key = config.get("GEMINI_API_KEY")
    if not api_key or "YOUR_ACTUAL_GEMINI_API_KEY_HERE" in api_key:
        api_key = os.environ.get("GEMINI_API_KEY")
except FileNotFoundError:
    api_key = os.environ.get("GEMINI_API_KEY")

# Create a GenAI client
client = None
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    print(f"Error initializing GenAI client: {e}")

chat_sessions = {}
MODEL_NAME = "gemini-2.5-flash"

# --- Flask Routes ---

@app.route('/')
def index():
    return render_template('index.html', initial_session_id=str(uuid.uuid4()))

@app.route('/chat', methods=['POST'])
def chat():
    """Handles standard chat messages via the Gemini API."""
    if not client:
        return jsonify({'error': 'Gemini Client failed to initialize. Check your API key.', 'success': False}), 500

    try:
        data = request.get_json()
        message = data.get('message', '')
        session_id = data.get('session_id', 'default')

        if not message.strip():
            return jsonify({'error': 'Message cannot be empty'}), 400

        if session_id not in chat_sessions:
            chat_sessions[session_id] = client.chats.create(model=MODEL_NAME)
        
        chat = chat_sessions[session_id]
        
        # Send message to the model
        response = chat.send_message(message)
        
        return jsonify({
            'response': response.text, 
            'success': True
        })

    except Exception as e:
        error_msg = f"API Error: {type(e).__name__}: {str(e)}"
        return jsonify({'error': error_msg, 'success': False}), 500

@app.route('/action', methods=['POST'])
def handle_action():
    """Handles special commands like /write or /read."""
    data = request.get_json()
    command = data.get('command', '').strip().lower()
    
    parts = command.split(' ', 2)
    action = parts[0]

    if action == '/write' and len(parts) == 3:
        filename = parts[1]
        content = parts[2]
        success, message = writeFile(filename, content)
        return jsonify({'response': message, 'success': success, 'is_file_action': True})

    elif action == '/read' and len(parts) >= 2:
        filename = parts[1]
        success, content = readFile(filename)
        if success:
            response_text = f"--- Content of '{filename}' ---\n\n{content}\n\n--- End of File ---"
        else:
            response_text = content # This is the error message
            
        return jsonify({'response': response_text, 'success': success, 'is_file_action': True})

    elif action == '/list':
        try:
            files = [f for f in os.listdir('.') if os.path.isfile(f) and f != 'app.py' and f != 'config.json' and f != 'README.md' and f != 'requirements.txt' and not f.startswith('.')]
            if files:
                response_text = "Files in current directory:\n- " + "\n- ".join(files)
            else:
                response_text = "No user-created files found in the current directory."
            return jsonify({'response': response_text, 'success': True, 'is_file_action': True})
        except Exception as e:
             return jsonify({'response': f"Error listing files: {e}", 'success': False, 'is_file_action': True})


    else:
        return jsonify({
            'response': "Invalid command format. Use:\n"
                        " - **/write [filename] [content]**\n"
                        " - **/read [filename]**\n"
                        " - **/list**", 
            'success': False, 
            'is_file_action': True
        })


@app.route('/clear', methods=['POST'])
def clear_chat():
    data = request.get_json()
    session_id = data.get('session_id', 'default')
    
    new_session_id = str(uuid.uuid4())
    if session_id in chat_sessions:
        del chat_sessions[session_id]
    
    return jsonify({
        'success': True, 
        'message': 'Chat history cleared.',
        'new_session_id': new_session_id
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
