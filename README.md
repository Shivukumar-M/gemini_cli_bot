# Gemini CLI Chatbot

A simple, interactive command-line interface (CLI) chatbot powered by Google's Gemini API. This application allows you to chat directly with a Gemini model, maintaining conversational context throughout your session.

## ✨ Features

*   **Interactive Chat:** Engage in a turn-by-turn conversation with the Gemini model.
*   **Conversational Memory:** The chatbot remembers previous turns in the conversation, allowing for more natural and context-aware interactions.
*   **API Key Management:** Securely loads your Gemini API key from a `config.json` file.
*   **Robust Error Handling:** Includes checks for missing configuration files, malformed JSON, missing API keys, and issues during API calls (e.g., network errors, content safety blocks).
*   **Graceful Exit:** Easily quit the chat by typing 'exit', 'quit', or 'q'.

## 🚀 Getting Started

Follow these steps to set up and run the Gemini CLI Chatbot on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.x:** Download from [python.org](https://www.python.org/downloads/).
*   **Google Gemini API Key:** You'll need an API key to access the Gemini models.

### Installation

1.  **Clone or Download the Repository:**
    If you're using Git:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
    (Replace `<repository_url>` and `<repository_name>` with your actual GitHub repository details once it's set up.)

    Alternatively, download the `chatbot.py` file directly.

2.  **Install Required Libraries:**
    Open your terminal or command prompt and run:
    ```bash
    pip install google-generativeai
    ```

### 🔑 API Key Configuration

**IMPORTANT: Never commit your API keys directly into your code or public repositories!**

1.  **Generate a Gemini API Key:**
    *   Go to the [Google AI Studio](https://aistudio.google.com/app/apikey) website.
    *   Sign in with your Google account.
    *   Click "Get API key" or "Create API key in new project."
    *   Copy the generated API key.

2.  **Create `config.json`:**
    In the **same directory** where you saved `chatbot.py`, create a new file named `config.json`.
    Open `config.json` with a text editor and add the following content, replacing `"YOUR_ACTUAL_GEMINI_API_KEY"` with the key you generated:

    ```json
    {
      "GEMINI_API_KEY": "YOUR_ACTUAL_GEMINI_API_KEY"
    }
    ```

## 🎮 Usage

1.  **Run the Chatbot:**
    Open your terminal or command prompt, navigate to the directory where you saved `chatbot.py` and `config.json`, and run:
    ```bash
    python chatbot.py
    ```

2.  **Start Chatting:**
    The chatbot will greet you, and you can start typing your questions or prompts after the "You:" prompt.

    ```
    Welcome to Gemini Chat!
    Type 'exit', 'quit', or 'q' to end the conversation.
    ----------------------------------------
    You: Hello, how are you?
    Gemini: I am an AI, so I don't have feelings, but I'm ready to help you! How can I assist you today?
    You: What is the capital of France?
    Gemini: The capital of France is Paris.
    You: And what about Germany?
    Gemini: The capital of Germany is Berlin.
    You: quit
    Gemini: Goodbye! It was nice chatting with you.
    ```

3.  **Exit the Chat:**
    To end the conversation, type `exit`, `quit`, or `q` at any `You:` prompt and press Enter.

## ⚠️ Error Handling

The script includes basic error handling for:
*   Missing `config.json` file.
*   Invalid JSON syntax in `config.json`.
*   Missing `GEMINI_API_KEY` within `config.json`.
*   General API call issues (e.g., network problems).
*   Prompts that are blocked by Gemini's content safety policies.

If an error occurs, the script will usually print an informative message.

## 💡 Enhancements & Future Improvements

*   **More Advanced Error Handling:** Implement specific handling for different API error codes.
*   **Prompt Engineering:** Add system instructions or initial prompts to guide the chatbot's persona or behavior.
*   **Logging:** Implement logging to save conversation history or debug information.
*   **Configuration Options:** Allow model name, temperature, or other parameters to be set via command-line arguments or a more elaborate config file.
*   **User Interface:** Convert to a GUI application (e.g., using Tkinter, PyQt, Streamlit).
*   **Multimodal Support:** Integrate vision capabilities if using a `gemini-pro-vision` type model.

## 📄 License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details. (You'd create a separate LICENSE file if you want to include a formal license).
