from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime
import os

def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """
    Save research data to a text file.
    
    Args:
        data: The content to save
        filename: Output filename (default: research_output.txt)
    
    Returns:
        Success message with file path
    """
    try:
        output_dir = "outputs"
        os.makedirs(output_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename_with_timestamp = f"{timestamp}_{filename}"
        filepath = os.path.join(output_dir, filename_with_timestamp)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(data)
        
        return f"Successfully saved to {filepath}"
    except Exception as e:
        return f"Error saving file: {str(e)}"


def get_current_time() -> str:
    """
    Get the current date and time.
    
    Returns:
        Formatted current datetime string
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Initialize Wikipedia tool
wikipedia = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        top_k_results=2,
        doc_content_chars_max=1000
    )
)

# Initialize DuckDuckGo search tool
search = DuckDuckGoSearchRun()

# Create custom tools
wiki_tool = Tool(
    name="Wikipedia",
    func=wikipedia.run,
    description="Useful for searching Wikipedia for detailed information about topics, people, places, and events. Input should be a search query."
)

search_tool = Tool(
    name="WebSearch",
    func=search.run,
    description="Useful for searching the web for current information, news, and general queries. Input should be a search query."
)

save_tool = Tool(
    name="SaveToFile",
    func=save_to_txt,
    description="Useful for saving research results or any text content to a file. Input should be the text content to save."
)

time_tool = Tool(
    name="CurrentTime",
    func=get_current_time,
    description="Get the current date and time. No input required."
)

# Export all tools
all_tools = [wiki_tool, search_tool, save_tool, time_tool]