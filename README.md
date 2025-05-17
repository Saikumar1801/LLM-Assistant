# 🧠 LLM Assistant

LLM Assistant is a modular framework for building and testing agent-based interactions with Large Language Models (LLMs), including support for OpenRouter integration and Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

-   🔗 **OpenRouter LLM Integration** – Modular integration for accessing OpenRouter-backed LLMs.
-   🧩 **Agent Architecture** – Separate agents for research, response generation, and core orchestration.
-   📄 **RAG Support** – Components for retrieval-augmented workflows.
-   🧪 **Testing Scripts** – Unit tests for model and RAG validation.

---

## 📁 Project Structure

The project is organized as follows:

```
llm-assistant/
├── agents/
│   ├── __init__.py
│   ├── research_agent.py
│   └── response_agent.py
├── memory/
│   ├── __init__.py
│   └── vector_store.py
├── tools/
│   ├── __init__.py
│   ├── web_search.py
│   └── doc_retriever.py
├── config.py
├── main.py
└── requirements.txt
```

---

## ⚙️ Setup

### 1. Clone the Repository

If you have access to the repository, clone it to your local machine:
```bash
git clone https://github.com/your-username/llm-assistant.git
cd llm-assistant
```
(Replace `your-username/llm-assistant.git` with the actual repository URL if applicable.)

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies. (Python 3.9+ recommended).

```bash
python -m venv venv
```

Activate the virtual environment:
-   On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```
-   On Windows:
    ```bash
    venv\Scripts\activate
    ```

### 3. Install Dependencies

Install the required Python packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

The application requires API keys to interact with LLM providers like OpenRouter. Create a `.env` file in the root directory of the project (`llm-assistant/.env`).

Add your OpenRouter API key to this file:
```dotenv
OPENROUTER_API_KEY="your_openrouter_api_key_here"
```
Replace `"your_openrouter_api_key_here"` with your actual API key.

---

## 🧪 Running Tests

To verify that the core components are functioning as expected, you can run the provided test scripts. Ensure your virtual environment is activated and the `.env` file is correctly set up.

```bash
python test_llm.py
python test_rag.py
```
These tests will help confirm connectivity with the LLM provider and the basic functionality of the RAG pipeline.

---

## 🧠 Usage

To start the LLM Assistant application, run the `main.py` script from the root of the project directory:

```bash
python main.py
```
Ensure that your `.env` file is present and contains a valid `OPENROUTER_API_KEY`. The application will then be ready to process your requests.

*(Conceptual Interaction Example)*
```
You: What were the key findings of the latest climate report regarding arctic sea ice?
LLM Assistant: ... (processes request, potentially uses research and response agents to generate an answer) ...
```

---

## 📌 TODO

The following features and improvements are planned for future development:

-   [ ] Add a Command Line Interface (CLI) for more user-friendly interaction.
-   [ ] Implement support for additional LLM providers (e.g., Hugging Face Hub, local models via Ollama).
-   [ ] Develop a simple Web UI (e.g., using Streamlit or FastAPI/React) for interacting with the agents.
-   [ ] Enhance the RAG system with more advanced retrieval strategies (e.g., hybrid search, re-ranking).
-   [ ] Expand unit and integration test coverage for all modules.
-   [ ] Implement more sophisticated error handling and logging.
-   [ ] Add support for persistent conversation history across sessions.
```
