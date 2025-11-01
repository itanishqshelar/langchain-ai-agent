<div align="center">

# 🤖 LangChain AI Agent

### _Intelligent Conversational AI with Multi-Tool Integration_

<img src="https://img.shields.io/badge/LANGCHAIN-AI_AGENT-00A67E?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAEjSURBVHjaYvz//z8DFQELAwMDw/9///4x/P//nwlZnImBgYGBkYGBgRGbJBMDAwPD////GRgZGRkY/v9nYGBkZGD4/58RXQMTuhcZ0b3IhM0bTNg0MqH7AZsmJnQvMjL+/8/A8P8/A8P//wyMjP8ZGBj/MzD+Z2Rg/P+fgfH/fwaG//8ZGf7/Z2T4j80pTOgaGf//Z2D8/5+B8f9/Bob//xkY/v9nZPj/n4nh/39mhv//WRj+/2dh+P+fheH/f1aG//9ZGf7/Z2X4/5+V4f9/Vob//9kY/v9nY/j/n43h/382hv//2Rn+/2dn+P+fneH/f3aG//85GP7/52D4/5+D4f9/Dob//zkZ/v/nZPj/n5Ph/39Ohv//uRj+/+di+P+fi+H/fy6G//+5Gf7/52b4/5+b4f9/bgYAoMKN+T8qxQAAAABJRU5ErkJggg==&labelColor=1C1C1C" alt="LangChain AI Agent" />

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/🦜_LangChain-Latest-00A67E?style=for-the-badge)](https://python.langchain.com/)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-API-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-V2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

---

### 📚 Tech Stack & Documentation

<table>
<tr>
<td align="center" width="140">
<a href="https://python.langchain.com/docs/introduction/" target="_blank">
<img src="https://img.shields.io/badge/LangChain-Core-00A67E?style=flat-square&logo=chainlink&logoColor=white" alt="LangChain"/><br/>
<sub><b>LangChain</b></sub>
</a>
</td>
<td align="center" width="140">
<a href="https://ai.google.dev/tutorials/python_quickstart" target="_blank">
<img src="https://img.shields.io/badge/Gemini-API-4285F4?style=flat-square&logo=google&logoColor=white" alt="Google Gemini"/><br/>
<sub><b>Google Gemini</b></sub>
</a>
</td>
<td align="center" width="140">
<a href="https://fastapi.tiangolo.com/" target="_blank">
<img src="https://img.shields.io/badge/FastAPI-REST-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/><br/>
<sub><b>FastAPI</b></sub>
</a>
</td>
<td align="center" width="140">
<a href="https://docs.pydantic.dev/latest/" target="_blank">
<img src="https://img.shields.io/badge/Pydantic-V2-E92063?style=flat-square&logo=pydantic&logoColor=white" alt="Pydantic"/><br/>
<sub><b>Pydantic</b></sub>
</a>
</td>
</tr>
<tr>
<td align="center" width="140">
<a href="https://en.wikipedia.org/wiki/Wikipedia:Copyrights" target="_blank">
<img src="https://img.shields.io/badge/Wikipedia-API-000000?style=flat-square&logo=wikipedia&logoColor=white" alt="Wikipedia"/><br/>
<sub><b>Wikipedia</b></sub>
</a>
</td>
<td align="center" width="140">
<a href="https://duckduckgo.com/" target="_blank">
<img src="https://img.shields.io/badge/DuckDuckGo-Search-DE5833?style=flat-square&logo=duckduckgo&logoColor=white" alt="DuckDuckGo"/><br/>
<sub><b>DuckDuckGo</b></sub>
</a>
</td>
<td align="center" width="140">
<a href="https://docs.docker.com/" target="_blank">
<img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/><br/>
<sub><b>Docker</b></sub>
</a>
</td>
<td align="center" width="140">
<a href="https://docs.pytest.org/" target="_blank">
<img src="https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=flat-square&logo=pytest&logoColor=white" alt="Pytest"/><br/>
<sub><b>Pytest</b></sub>
</a>
</td>
</tr>
</table>

---

</div>

## 🚀 Features

- **Multi-tool Integration**: Wikipedia search, web search, file saving, and time utilities
- **Conversation Memory**: Maintains chat history for contextual responses
- **Extensible Architecture**: Easy to add new tools and customize behavior
- **Error Handling**: Robust error handling and graceful degradation
- **Configuration Management**: Environment-based configuration
- **Clean CLI Interface**: User-friendly command-line interface

## 📋 Prerequisites

- Python 3.8+
- Google API Key (for Gemini models) or OpenAI API Key

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/itanishqshelar/langchain-ai-agent.git
   cd langchain-ai-agent
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv

   # Windows
   .\venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:

   ```env
   # Required: At least one API key
   GOOGLE_API_KEY=your_google_api_key_here
   # OPENAI_API_KEY=your_openai_api_key_here

   # Optional: Model Configuration
   DEFAULT_MODEL=gemini-2.0-flash-exp
   TEMPERATURE=0.7
   MAX_TOKENS=2048

   # Optional: Agent Settings
   MAX_ITERATIONS=5
   VERBOSE=True
   MAX_HISTORY_LENGTH=10

   # Optional: Storage
   OUTPUT_DIR=outputs
   ```

## 🎯 Usage

### Basic Usage

Run the chatbot:

```bash
python main.py
```

### Available Commands

While chatting:

- **Ask questions**: Just type your question naturally
- **`clear`**: Clear chat history
- **`history`**: View conversation history
- **`quit`** or **`exit`**: Exit the chatbot

### Example Interactions

```
You: What is LangChain?
AI: [Searches Wikipedia and provides detailed explanation]

You: Search for the latest AI news
AI: [Uses web search to find current information]

You: Save that information to a file
AI: [Saves the previous response to a timestamped file]

You: What time is it?
AI: [Returns current date and time]
```

## 🏗️ Project Structure

```
langchain-ai-agent/
├── main.py              # Main chatbot application
├── tools.py             # Tool definitions and implementations
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── outputs/            # Generated output files (auto-created)
```

## 🔧 Customization

### Adding New Tools

1. **Define your tool function** in `tools.py`:

   ```python
   def my_custom_tool(input: str) -> str:
       """Your tool implementation"""
       return result
   ```

2. **Create a Tool instance**:

   ```python
   custom_tool = Tool(
       name="MyTool",
       func=my_custom_tool,
       description="Description of what your tool does"
   )
   ```

3. **Add to the tools list**:
   ```python
   all_tools = [wiki_tool, search_tool, save_tool, time_tool, custom_tool]
   ```

### Changing the LLM Model

Edit `.env`:

```env
# For Google Gemini
DEFAULT_MODEL=gemini-2.0-flash-exp

# For OpenAI (requires OPENAI_API_KEY)
# DEFAULT_MODEL=gpt-4-turbo-preview
```

Update `main.py` to use OpenAI:

```python
from langchain_openai import ChatOpenAI

# In ChatBot.__init__:
self.llm = ChatOpenAI(
    model=model_name,
    temperature=temperature
)
```

### Adjusting Response Style

Modify the system prompt in `main.py`:

```python
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """Your custom system prompt here..."""
    ),
    # ... rest of the template
])
```

## 📚 Available Tools

| Tool            | Description                               | Input Example                 |
| --------------- | ----------------------------------------- | ----------------------------- |
| **Wikipedia**   | Search Wikipedia for detailed information | "Python programming language" |
| **WebSearch**   | Search the web for current information    | "latest AI developments 2024" |
| **SaveToFile**  | Save content to a text file               | "content to save"             |
| **CurrentTime** | Get current date and time                 | (no input needed)             |

## 🧪 Testing

Run a quick test:

```bash
python -c "from main import ChatBot; bot = ChatBot(); print(bot.chat('Hello!'))"
```

## 🔒 Security Best Practices

- **Never commit `.env`** files to version control
- **Rotate API keys** regularly
- **Use environment variables** for all sensitive data
- **Limit tool permissions** based on your use case
- **Monitor API usage** to avoid unexpected costs

## 📝 Configuration Options

Edit `.env` to customize:

| Variable             | Default              | Description                      |
| -------------------- | -------------------- | -------------------------------- |
| `GOOGLE_API_KEY`     | -                    | Google Gemini API key (required) |
| `OPENAI_API_KEY`     | -                    | OpenAI API key (optional)        |
| `DEFAULT_MODEL`      | gemini-2.0-flash-exp | LLM model to use                 |
| `TEMPERATURE`        | 0.7                  | Response creativity (0.0-1.0)    |
| `MAX_TOKENS`         | 2048                 | Maximum response length          |
| `MAX_ITERATIONS`     | 5                    | Max tool calling iterations      |
| `VERBOSE`            | True                 | Show detailed agent logs         |
| `MAX_HISTORY_LENGTH` | 10                   | Chat history size                |
| `OUTPUT_DIR`         | outputs              | Directory for saved files        |

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### "No API key found"

- Ensure `.env` file exists and contains valid API keys
- Check that `python-dotenv` is installed

### "Module not found" errors

- Run `pip install -r requirements.txt`
- Ensure virtual environment is activated

### Tool execution errors

- Check internet connection (required for Wikipedia and web search)
- Verify API rate limits haven't been exceeded

### Import errors

- Ensure all dependencies are up to date: `pip install --upgrade -r requirements.txt`

## 🔗 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- [OpenAI API](https://platform.openai.com/)

## 📧 Support

For issues and questions:

- Open an issue on GitHub
- Check existing issues for solutions

---

**Made with ❤️ using LangChain**
