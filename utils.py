"""
Utility functions for the LangChain chatbot.
"""
import os
import json
from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path


def ensure_directory(directory: str) -> None:
    """
    Ensure a directory exists, create if it doesn't.
    
    Args:
        directory: Path to the directory
    """
    Path(directory).mkdir(parents=True, exist_ok=True)


def save_conversation(
    conversation: List[Dict[str, str]],
    filename: Optional[str] = None,
    output_dir: str = "outputs"
) -> str:
    """
    Save a conversation to a JSON file.
    
    Args:
        conversation: List of message dictionaries with 'role' and 'content'
        filename: Optional custom filename
        output_dir: Directory to save the file
        
    Returns:
        Path to the saved file
    """
    ensure_directory(output_dir)
    
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversation_{timestamp}.json"
    
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(conversation, f, indent=2, ensure_ascii=False)
    
    return filepath


def load_conversation(filepath: str) -> List[Dict[str, str]]:
    """
    Load a conversation from a JSON file.
    
    Args:
        filepath: Path to the conversation file
        
    Returns:
        List of message dictionaries
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def format_message_history(messages: List[Any]) -> str:
    """
    Format chat history into a readable string.
    
    Args:
        messages: List of LangChain message objects
        
    Returns:
        Formatted string representation
    """
    formatted = []
    for i, msg in enumerate(messages):
        role = "User" if i % 2 == 0 else "AI"
        content = msg.content if hasattr(msg, 'content') else str(msg)
        formatted.append(f"{role}: {content}")
    
    return "\n\n".join(formatted)


def truncate_text(text: str, max_length: int = 100) -> str:
    """
    Truncate text to a maximum length with ellipsis.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."


def count_tokens_estimate(text: str) -> int:
    """
    Estimate token count (rough approximation).
    
    Args:
        text: Text to count tokens for
        
    Returns:
        Estimated token count
    """
    # Rough estimate: ~4 characters per token
    return len(text) // 4


def validate_api_key(api_key: Optional[str]) -> bool:
    """
    Validate API key format.
    
    Args:
        api_key: API key to validate
        
    Returns:
        True if valid format, False otherwise
    """
    if not api_key:
        return False
    
    # Basic validation - should be a non-empty string
    return isinstance(api_key, str) and len(api_key.strip()) > 0


def get_file_size(filepath: str) -> str:
    """
    Get human-readable file size.
    
    Args:
        filepath: Path to the file
        
    Returns:
        Formatted file size string
    """
    size_bytes = os.path.getsize(filepath)
    
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    
    return f"{size_bytes:.2f} TB"


def list_saved_conversations(output_dir: str = "outputs") -> List[Dict[str, Any]]:
    """
    List all saved conversation files.
    
    Args:
        output_dir: Directory to search for conversation files
        
    Returns:
        List of dictionaries with file information
    """
    if not os.path.exists(output_dir):
        return []
    
    conversations = []
    for filename in os.listdir(output_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(output_dir, filename)
            conversations.append({
                'filename': filename,
                'filepath': filepath,
                'size': get_file_size(filepath),
                'modified': datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d %H:%M:%S')
            })
    
    return sorted(conversations, key=lambda x: x['modified'], reverse=True)


def clean_old_files(output_dir: str = "outputs", days_old: int = 30) -> int:
    """
    Clean up old files from the output directory.
    
    Args:
        output_dir: Directory to clean
        days_old: Remove files older than this many days
        
    Returns:
        Number of files removed
    """
    if not os.path.exists(output_dir):
        return 0
    
    current_time = datetime.now().timestamp()
    cutoff_time = current_time - (days_old * 24 * 60 * 60)
    
    removed_count = 0
    for filename in os.listdir(output_dir):
        filepath = os.path.join(output_dir, filename)
        if os.path.isfile(filepath):
            file_time = os.path.getmtime(filepath)
            if file_time < cutoff_time:
                os.remove(filepath)
                removed_count += 1
    
    return removed_count


def export_to_markdown(
    conversation: List[Dict[str, str]],
    title: str = "Conversation Export",
    output_dir: str = "outputs"
) -> str:
    """
    Export conversation to a markdown file.
    
    Args:
        conversation: List of message dictionaries
        title: Title for the markdown document
        output_dir: Directory to save the file
        
    Returns:
        Path to the saved file
    """
    ensure_directory(output_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"conversation_{timestamp}.md"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
        f.write("---\n\n")
        
        for msg in conversation:
            role = msg.get('role', 'unknown').title()
            content = msg.get('content', '')
            f.write(f"## {role}\n\n")
            f.write(f"{content}\n\n")
    
    return filepath
