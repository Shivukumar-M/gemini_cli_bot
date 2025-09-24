from flask import Flask, render_template, request, jsonify
import json
import google.generativeai as genai
import sys

app = Flask(__name__)

# --- Load API key from config.json with error handling ---
try:
    with open("config.json", "r") as f:
        config = json.load(f)
    api_key = config.get("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in config.json. Please ensure it's set.")

except FileNotFoundError:
    print("Error: config.json not found. Please create a config.json file in the same directory.")
    print("It should contain: {\"GEMINI_API_KEY\": \"YOUR_GEMINI_API_KEY\"}")
    sys.exit(1)

# --- Configure Gemini ---
genai.configure(api_key=api_key)

# --- Initialize model ---
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# Store chat sessions in memory (in production, use a database)
chat_sessions = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '')
        session_id = data.get('session_id', 'default')
        
        if not message.strip():
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get or create chat session
        if session_id not in chat_sessions:
            chat_sessions[session_id] = model.start_chat(history=[])
        
        chat_session = chat_sessions[session_id]
        
        # Send message and get response
        response = chat_session.send_message(message)
        
        return jsonify({
            'response': response.text,
            'success': True
        })
        
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'success': False
        }), 500

@app.route('/clear', methods=['POST'])
def clear_chat():
    try:
        data = request.get_json()
        session_id = data.get('session_id', 'default')
        
        # Clear the chat session
        if session_id in chat_sessions:
            del chat_sessions[session_id]
        
        return jsonify({'success': True, 'message': 'Chat cleared successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

if __name__ == '__main__':
    app.run(debug=True)