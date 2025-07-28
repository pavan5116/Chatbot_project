# Streamlit AI Chatbot

A simple web-based AI chatbot built with Python, Streamlit, and Google Gemini (via LangChain), allowing users to interact with an LLM through an intuitive browser interface.

## ✨ Features

- **Conversational AI** using Google Gemini (via LangChain)
- **Web UI** built with [Streamlit](https://streamlit.io/)
- **Instant prompt-response** for natural language queries
- **Simple setup**—just configure your Google API key and run

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Google Gemini API key (from [Google AI](https://aistudio.google.com/app/apikey))
- `pip` for installing packages

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies**:
    ```bash
    pip install streamlit langchain-google-genai
    ```

3. **Set your Google API key**:  
   Replace `"Your-Google-api-key"` in the code or, preferably, set it as an environment variable:
    ```bash
    export GOOGLE_API_KEY="your-key-here"
    ```

### Usage

To launch the chatbot locally:
```bash
streamlit run main.py
```
*(Change `main.py` if your script has a different filename.)*

A web interface will open automatically in your browser. Enter a prompt in the text input box and the chatbot will reply instantly.

## 📝 Example

![Chatbot Demo Screenshot](https://placehold.co/600x200?text=Demo “What is the capital of France?”  
2. The chatbot replies: “Paris.”

## 🛠️ How it Works

- The app initializes a Google Gemini LLM via LangChain.
- Streamlit provides a form for entering prompts and displays the response.
- All LLM processing happens server-side; no user data is stored.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

*Feel free to enhance this README with real screenshots, more instructions, or contribution guidelines to match your project goals!*
