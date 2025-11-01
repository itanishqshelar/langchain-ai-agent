"""
Example usage and demonstrations of the LangChain chatbot.
"""
from main import ChatBot
from tools import all_tools


def example_basic_chat():
    """Example 1: Basic conversational interaction."""
    print("\n" + "="*60)
    print("Example 1: Basic Chat")
    print("="*60 + "\n")
    
    bot = ChatBot()
    
    questions = [
        "Hello! Who are you?",
        "What can you help me with?",
        "What's the weather like today?",
    ]
    
    for question in questions:
        print(f"User: {question}")
        response = bot.chat(question)
        print(f"AI: {response}\n")


def example_wikipedia_search():
    """Example 2: Using Wikipedia tool."""
    print("\n" + "="*60)
    print("Example 2: Wikipedia Search")
    print("="*60 + "\n")
    
    bot = ChatBot()
    
    print("User: Tell me about Albert Einstein")
    response = bot.chat("Tell me about Albert Einstein")
    print(f"AI: {response}\n")


def example_web_search():
    """Example 3: Using web search tool."""
    print("\n" + "="*60)
    print("Example 3: Web Search")
    print("="*60 + "\n")
    
    bot = ChatBot()
    
    print("User: What are the latest developments in AI?")
    response = bot.chat("What are the latest developments in AI?")
    print(f"AI: {response}\n")


def example_save_to_file():
    """Example 4: Saving information to a file."""
    print("\n" + "="*60)
    print("Example 4: Save to File")
    print("="*60 + "\n")
    
    bot = ChatBot()
    
    print("User: Tell me about Python programming")
    response1 = bot.chat("Tell me about Python programming")
    print(f"AI: {response1}\n")
    
    print("User: Save that information to a file")
    response2 = bot.chat("Save that information to a file")
    print(f"AI: {response2}\n")


def example_multi_turn_conversation():
    """Example 5: Multi-turn conversation with memory."""
    print("\n" + "="*60)
    print("Example 5: Multi-turn Conversation")
    print("="*60 + "\n")
    
    bot = ChatBot()
    
    conversation = [
        "What is machine learning?",
        "Can you give me some examples?",
        "Which one is used for image recognition?",
        "Save a summary of our conversation about machine learning"
    ]
    
    for message in conversation:
        print(f"User: {message}")
        response = bot.chat(message)
        print(f"AI: {response}\n")


def example_custom_temperature():
    """Example 6: Using different temperature settings."""
    print("\n" + "="*60)
    print("Example 6: Temperature Comparison")
    print("="*60 + "\n")
    
    question = "Write a creative story about a robot learning to paint"
    
    # Low temperature (more focused)
    print("Low Temperature (0.2) - More Focused:\n")
    bot_focused = ChatBot(temperature=0.2)
    print(f"User: {question}")
    response1 = bot_focused.chat(question)
    print(f"AI: {response1}\n")
    
    # High temperature (more creative)
    print("\nHigh Temperature (0.9) - More Creative:\n")
    bot_creative = ChatBot(temperature=0.9)
    print(f"User: {question}")
    response2 = bot_creative.chat(question)
    print(f"AI: {response2}\n")


def example_history_management():
    """Example 7: Managing chat history."""
    print("\n" + "="*60)
    print("Example 7: History Management")
    print("="*60 + "\n")
    
    bot = ChatBot()
    
    # Build up some history
    bot.chat("Hello!")
    bot.chat("What is Python?")
    bot.chat("What are its main uses?")
    
    # View history
    print("Current chat history:")
    for i, msg in enumerate(bot.get_history(), 1):
        role = "User" if hasattr(msg, 'content') and i % 2 == 1 else "AI"
        print(f"{i}. {role}: {msg.content[:50]}...")
    
    # Clear history
    print("\nClearing history...")
    bot.clear_history()
    
    # Verify it's cleared
    print(f"History length after clearing: {len(bot.get_history())}")


def example_error_handling():
    """Example 8: Error handling demonstration."""
    print("\n" + "="*60)
    print("Example 8: Error Handling")
    print("="*60 + "\n")
    
    bot = ChatBot()
    
    # This might fail gracefully
    print("User: [Intentionally complex request]")
    response = bot.chat(
        "Search for information that definitely doesn't exist: "
        "xyzabc123notarealthing"
    )
    print(f"AI: {response}\n")


def run_all_examples():
    """Run all examples in sequence."""
    examples = [
        example_basic_chat,
        example_wikipedia_search,
        example_web_search,
        example_save_to_file,
        example_multi_turn_conversation,
        example_custom_temperature,
        example_history_management,
        example_error_handling,
    ]
    
    for example in examples:
        try:
            example()
            input("\nPress Enter to continue to next example...")
        except KeyboardInterrupt:
            print("\n\nExamples interrupted by user.")
            break
        except Exception as e:
            print(f"\nError in example: {e}")
            continue


if __name__ == "__main__":
    print("LangChain Chatbot - Usage Examples")
    print("=" * 60)
    print("\nChoose an option:")
    print("1. Run all examples")
    print("2. Basic chat")
    print("3. Wikipedia search")
    print("4. Web search")
    print("5. Save to file")
    print("6. Multi-turn conversation")
    print("7. Temperature comparison")
    print("8. History management")
    print("9. Error handling")
    
    choice = input("\nEnter your choice (1-9): ").strip()
    
    examples_map = {
        "1": run_all_examples,
        "2": example_basic_chat,
        "3": example_wikipedia_search,
        "4": example_web_search,
        "5": example_save_to_file,
        "6": example_multi_turn_conversation,
        "7": example_custom_temperature,
        "8": example_history_management,
        "9": example_error_handling,
    }
    
    example_func = examples_map.get(choice)
    if example_func:
        example_func()
    else:
        print("Invalid choice. Please run again and select 1-9.")
