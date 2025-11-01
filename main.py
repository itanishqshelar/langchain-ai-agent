from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage
from tools import all_tools
from pydantic import BaseModel, Field
from typing import Optional

# Load environment variables
load_dotenv()


class ResearchResponse(BaseModel):
    """Structured response for research queries."""
    topic: str = Field(description="The main topic researched")
    summary: str = Field(description="A comprehensive summary of the findings")
    sources: list[str] = Field(description="List of sources used", default_factory=list)
    tools_used: list[str] = Field(description="List of tools utilized", default_factory=list)


class ChatBot:
    """LangChain-powered chatbot with tool integration and memory."""
    
    def __init__(self, model_name: str = "gemini-2.0-flash-exp", temperature: float = 0.7):
        """
        Initialize the chatbot.
        
        Args:
            model_name: The LLM model to use
            temperature: Temperature setting for response generation (0.0-1.0)
        """
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=temperature
        )
        self.tools = all_tools
        self.chat_history = []
        self.agent_executor = self._create_agent()
    
    def _create_agent(self) -> AgentExecutor:
        """Create the agent with tools and prompt template."""
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """You are a helpful AI assistant with access to various tools.
                
Your capabilities include:
- Searching Wikipedia for detailed information
- Searching the web for current information
- Saving content to files
- Getting the current date and time

Always be helpful, accurate, and cite your sources when using tools.
When saving information, provide a clear summary of what was saved.
If you're unsure about something, say so rather than making up information.
                """
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])
        
        agent = create_tool_calling_agent(
            llm=self.llm,
            prompt=prompt,
            tools=self.tools
        )
        
        return AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=5
        )
    
    def chat(self, user_input: str) -> str:
        """
        Process user input and return AI response.
        
        Args:
            user_input: The user's message
            
        Returns:
            The AI's response
        """
        try:
            # Invoke agent
            response = self.agent_executor.invoke({
                "input": user_input,
                "chat_history": self.chat_history
            })
            
            # Extract output
            output = response.get("output", "I'm sorry, I couldn't process that request.")
            
            # Update chat history
            self.chat_history.append(HumanMessage(content=user_input))
            self.chat_history.append(AIMessage(content=output))
            
            # Limit chat history to last 10 messages (5 exchanges)
            if len(self.chat_history) > 10:
                self.chat_history = self.chat_history[-10:]
            
            return output
            
        except Exception as e:
            error_msg = f"Error processing request: {str(e)}"
            print(error_msg)
            return "I apologize, but I encountered an error processing your request. Please try again."
    
    def clear_history(self):
        """Clear the chat history."""
        self.chat_history = []
        print("Chat history cleared.")
    
    def get_history(self) -> list:
        """Get the current chat history."""
        return self.chat_history


def main():
    """Main function to run the chatbot."""
    print("=" * 60)
    print("🤖 LangChain AI Assistant")
    print("=" * 60)
    print("\nAvailable commands:")
    print("  - Type your question or request")
    print("  - 'clear' - Clear chat history")
    print("  - 'history' - View chat history")
    print("  - 'quit' or 'exit' - Exit the chatbot")
    print("\n" + "=" * 60 + "\n")
    
    # Initialize chatbot
    bot = ChatBot()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Goodbye! Thanks for chatting!")
                break
            
            elif user_input.lower() == 'clear':
                bot.clear_history()
                continue
            
            elif user_input.lower() == 'history':
                history = bot.get_history()
                if not history:
                    print("No chat history yet.")
                else:
                    print("\n--- Chat History ---")
                    for msg in history:
                        role = "You" if isinstance(msg, HumanMessage) else "AI"
                        print(f"{role}: {msg.content}")
                    print("--- End of History ---\n")
                continue
            
            # Get AI response
            print("\nAI: ", end="", flush=True)
            response = bot.chat(user_input)
            print(response + "\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for chatting!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    main()
