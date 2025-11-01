# Quick Start Guide

Get the LangChain AI Agent running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- A Google API key (get from [Google AI Studio](https://ai.google.dev/))

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/itanishqshelar/langchain-ai-agent.git
cd langchain-ai-agent
```

### 2. Create Virtual Environment

**Windows:**

```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` and add your API key:

```env
GOOGLE_API_KEY=your_actual_api_key_here
```

### 5. Run the Chatbot!

```bash
python main.py
```

That's it! 🎉

## Your First Conversation

Try these commands:

```
You: Hello! What can you do?

You: Tell me about Python programming

You: Search for the latest AI news

You: Save that information to a file

You: What time is it?
```

## Next Steps

- **Explore Examples**: Run `python examples.py` for demonstrations
- **Customize**: Edit `config.py` to change settings
- **Add Tools**: Follow `CONTRIBUTING.md` to add custom tools
- **API Mode**: Run `uvicorn api:app --reload` for REST API

## Common Issues

### "No API key found"

- Make sure `.env` file exists
- Check that `GOOGLE_API_KEY` is set correctly
- Ensure no extra spaces in the `.env` file

### "Module not found"

- Activate your virtual environment
- Run `pip install -r requirements.txt` again

### Import errors

- Update packages: `pip install --upgrade -r requirements.txt`

## Docker Alternative

If you prefer Docker:

```bash
# Build and run
docker-compose up chatbot

# Or for API mode
docker-compose up api
```

## Getting Help

- Check the [README](README.md) for detailed documentation
- See [examples.py](examples.py) for usage examples
- Open an issue on GitHub for problems

---

**Happy chatting! 🤖**
