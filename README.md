# AI Assistant using LangChain and OpenAI

## Overview

This project is a command-line AI assistant built using LangChain and OpenAI's language models. The assistant allows users to have interactive conversations through the terminal and generates intelligent responses using an LLM.

## Features

* Interactive command-line chatbot
* Powered by OpenAI language models
* Built using LangChain agents
* Streaming responses for a real-time chat experience
* Secure API key management using environment variables
* Simple and lightweight implementation

## Technologies Used

* Python
* LangChain
* OpenAI
* python-dotenv
* uv Package Manager

## Project Structure

```text
aiproject/
│
├── main.py
├── .env
├── .gitignore
├── README.md
├── pyproject.toml
└── uv.lock
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/aiproject.git
cd aiproject
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
uv sync
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

## Running the Project

```bash
python main.py
```

You will see:

```text
Welcome! I am your AI assistant. Type 'quit' to exit.
```

Example:

```text
You: What is artificial intelligence?

Assistant: Artificial Intelligence (AI) is...
```

To exit:

```text
You: quit
```

## How It Works

1. Loads the OpenAI API key from the `.env` file.
2. Initializes a LangChain `ChatOpenAI` model.
3. Creates an AI agent using LangChain.
4. Accepts user input from the terminal.
5. Sends prompts to the language model.
6. Streams responses back to the user in real time.

## Future Improvements

* Add custom tools and function calling
* Web search integration
* Memory and conversation history
* Streamlit or Flask web interface
* Voice-based interaction
* Multi-agent workflows

## Author

**Suhani Verma**

B.Tech – AI & Data Engineering
