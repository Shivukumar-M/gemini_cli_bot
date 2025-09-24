# Gemini AI Web Chatbot

A simple, interactive **web-based chatbot** powered by **Google's Gemini
API**, built using **Python (Flask)** and a modern **Tailwind CSS**
frontend.\
This application provides a **clean, responsive UI** for natural
conversations with the Gemini model.

------------------------------------------------------------------------

## ✨ Features

-   **Responsive Web Interface** → Works seamlessly on desktop & mobile
    devices.\
-   **Conversational Memory** → Maintains context across the chat
    session.\
-   **Secure API Key Management** → Loads Gemini API key from
    `config.json` (not exposed in code).\
-   **Dynamic UI** → Loading indicator + smooth animations for new
    messages.\
-   **Error Handling** → User-friendly error messages for network/API
    failures.\
-   **Clear Chat** → Reset button to clear chat history instantly.

------------------------------------------------------------------------

## 🚀 Getting Started

Follow these steps to set up and run the chatbot locally.

### ✅ Prerequisites

-   [Python 3.x](https://www.python.org/downloads/)\
-   [Google Gemini API Key](https://aistudio.google.com/)

------------------------------------------------------------------------

### ⚙️ Installation

1.  **Clone / Download the Project**\
    Download the files (`app.py`, `index.html`, `config.json`,
    `README.md`) into a single folder.

2.  **Install Dependencies**

    ``` bash
    pip install Flask google-generativeai
    ```

------------------------------------------------------------------------

### 🔑 API Key Configuration

⚠️ **Never commit your API keys to GitHub or public repos!**

1.  **Get API Key**

    -   Go to [Google AI Studio](https://aistudio.google.com/).\
    -   Sign in → Click **Get API Key** → Copy the generated key.

2.  **Update `config.json`**\
    Replace the placeholder with your actual API key:

    ``` json
    {
      "GEMINI_API_KEY": "YOUR_ACTUAL_GEMINI_API_KEY"
    }
    ```

------------------------------------------------------------------------

### 🎮 Usage

1.  **Run the Flask app**

    ``` bash
    python app.py
    ```

    You should see:

        * Running on http://127.0.0.1:5000

2.  **Open in Browser**\
    Go to → <http://127.0.0.1:5000>

3.  **Start Chatting**

    -   Type your message → Press **Enter** or click **Send**\
    -   Click **Clear** to reset the chat

------------------------------------------------------------------------

## 📁 Project Structure

    📂 Gemini-Web-Chatbot
     ├── app.py        # Flask backend (routes, API requests, chat session handling)
     ├── index.html    # Frontend (Tailwind + JS for dynamic chat UI)
     ├── config.json   # Stores Gemini API Key securely
     └── README.md     # Project documentation

------------------------------------------------------------------------

## 💡 Enhancements (Future Improvements)

-   🔐 **User Authentication** → Maintain chat history per user.\
-   💾 **Persistent Storage** → Save chats in SQLite/Postgres/MongoDB.\
-   📝 **Markdown Rendering** → Rich formatting (lists, tables, code
    blocks).\
-   ☁️ **Deployment** → Host on **Heroku, Vercel, or AWS** for
    production.
