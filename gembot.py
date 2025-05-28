import json
import google.generativeai as genai
import sys # For graceful exit on config errors

# --- 1. Load API key from config.json with error handling ---
try:
    with open("config.json", "r") as f:
        config = json.load(f)
    api_key = config.get("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in config.json. Please ensure it's set.")

except FileNotFoundError:
    print("Error: config.json not found. Please create a config.json file in the same directory.")
    print("It should contain: {\"GEMINI_API_KEY\": \"YOUR_GEMINI_API_KEY\"}")
    sys.exit(1) # Exit the script if config.json is missing


# --- 2. Configure Gemini ---
genai.configure(api_key=api_key)

# --- 3. Initialize model and start a chat session for context ---
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash") 

# Start a chat session to maintain conversational history
chat = model.start_chat(history=[])

print("Welcome to Gemini Chat!")
print("Type 'exit', 'quit', or 'q' to end the conversation.")
print("-" * 40)

# --- 4. Chat loop ---
while True:
    try:
        prompt = input("You: ")

        # Exit conditions
        if prompt.lower() in ['exit', 'quit', 'q']:
            print("Gemini: Goodbye! It was nice chatting with you.")
            break

        # Send message to the chat session to maintain context
        response = chat.send_message(prompt)
        print("Gemini:", response.text)
        
    except Exception as e:
        # Catch general exceptions during API call (e.g., network error, API key issue)
        print(f"An error occurred: {e}")
        print("Please check your internet connection or API key, and try again.")
        # For now, we'll continue to allow the user to try again