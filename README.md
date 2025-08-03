# 🤖 AI Assistant with MCP + LangChain + Groq

This project demonstrates how to build a conversational AI assistant using [MCP (Modular Chain Processor)](https://github.com/langroid/MCP), [LangChain](https://www.langchain.com/), and [Groq LLMs](https://groq.com/). It leverages memory-enabled agents and Groq-hosted LLMs to interactively respond to user queries in a smart and contextual way.

---

## 📌 Features

- 🧠 Conversational memory (persistent session context)
- ⚙️ Integration with Groq's ultra-fast LLMs (Qwen, Mixtral, etc.)
- 🔄 Built using LangChain and MCP abstraction layers
- 💬 Interactive command-line chat interface
- ✅ Support for clearing history and exiting chat
- 🔒 Secure API Key loading from `.env`

---

## 🛠️ Requirements

- Python 3.9 or later
- Groq API Key (sign up at [Groq Cloud](https://console.groq.com/))
- MCP installed from source
- Optional: Create and activate a Python virtual environment

---

## 📦 Installation

### 1. Clone this repo:


git clone https://github.com/your-username/ai-assistant-mcp-groq.git
cd ai-assistant-mcp-groq

####2. Create a virtual environment and activate it:
python -m venv env
source env/bin/activate       # On Linux/macOS
env\Scripts\activate          # On Windows


🔑 Environment Setup
Create a .env file in the root directory and add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here


🧠 Configuration
Make sure you have a browser_mcp.json configuration file in your project directory. This file defines the behavior and tools of the MCP client.

{
  "tools": ["search", "calendar", "weather"],
  "settings": {
    "max_retries": 3,
    "timeout_seconds": 20
  }
}
Customize as needed for your use case.


▶️ Run the Assistant

python app.py

You will enter an interactive chat session:

You: Hello
MCP: Hi there! How can I assist you today?

You: clear
Conversation history cleared.

You: exit
Exiting the chat.



📁 Project Structure
pgsql
Copy
Edit
.
├── app.py                # Main application file
├── mcp_use.py            # MCPAgent and MCPClient wrapper
├── browser_mcp.json      # Tool configuration
├── .env                  # Your API key (not tracked by Git)
├── requirements.txt      # Python dependencies
└── README.md             # This file



🚀 Example Use Cases

Ask about weather, calendar, and search information

Use AI for summarization, suggestions, and planning

Build a smart chat experience in any terminal app
