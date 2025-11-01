"""
Test suite for the LangChain chatbot.
Run with: pytest test_chatbot.py -v
"""
import pytest
from main import ChatBot
from tools import save_to_txt, get_current_time
import os


class TestChatBot:
    """Test cases for the ChatBot class."""
    
    def test_chatbot_initialization(self):
        """Test that chatbot initializes correctly."""
        bot = ChatBot()
        assert bot is not None
        assert bot.llm is not None
        assert bot.tools is not None
        assert bot.chat_history == []
    
    def test_chat_basic(self):
        """Test basic chat functionality."""
        bot = ChatBot()
        response = bot.chat("Hello")
        assert response is not None
        assert len(response) > 0
        assert len(bot.chat_history) == 2  # User message + AI response
    
    def test_clear_history(self):
        """Test clearing chat history."""
        bot = ChatBot()
        bot.chat("Test message 1")
        bot.chat("Test message 2")
        assert len(bot.chat_history) > 0
        
        bot.clear_history()
        assert len(bot.chat_history) == 0
    
    def test_get_history(self):
        """Test retrieving chat history."""
        bot = ChatBot()
        bot.chat("Hello")
        
        history = bot.get_history()
        assert isinstance(history, list)
        assert len(history) == 2
    
    def test_custom_temperature(self):
        """Test chatbot with custom temperature."""
        bot = ChatBot(temperature=0.5)
        assert bot.llm.temperature == 0.5


class TestTools:
    """Test cases for custom tools."""
    
    def test_save_to_txt(self):
        """Test file saving functionality."""
        test_data = "Test content for file saving"
        result = save_to_txt(test_data, "test_output.txt")
        
        assert "Successfully saved" in result
        
        # Clean up
        output_dir = "outputs"
        if os.path.exists(output_dir):
            for file in os.listdir(output_dir):
                if "test_output.txt" in file:
                    os.remove(os.path.join(output_dir, file))
    
    def test_get_current_time(self):
        """Test time retrieval functionality."""
        result = get_current_time()
        assert result is not None
        assert len(result) > 0
        # Check if it contains date-like format
        assert "-" in result or "/" in result


class TestIntegration:
    """Integration tests."""
    
    def test_multi_turn_conversation(self):
        """Test multi-turn conversation with context."""
        bot = ChatBot()
        
        response1 = bot.chat("My name is Test User")
        assert response1 is not None
        
        # This should remember the name from previous message
        response2 = bot.chat("What is my name?")
        assert response2 is not None
        # Note: Actual name recognition depends on LLM behavior
    
    def test_tool_usage(self):
        """Test that tools can be invoked."""
        bot = ChatBot()
        
        # This should trigger the time tool
        response = bot.chat("What time is it?")
        assert response is not None
        assert len(response) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
