"""
Help Resource

Provides help and documentation for available tools and resources.
"""

from fastmcp import resource
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class HelpResource:
    """Help resource providing documentation"""
    
    def __init__(self):
        self.tool_help = {
            "calculator": {
                "add": "Add two numbers together. Args: a (float), b (float)",
                "subtract": "Subtract second number from first. Args: a (float), b (float)",
                "multiply": "Multiply two numbers. Args: a (float), b (float)",
                "divide": "Divide first number by second. Args: a (float), b (float)"
            },
            "weather": {
                "get_weather": "Get weather information for a city. Args: city (str) - seoul, tokyo, newyork, london"
            },
            "file_reader": {
                "read_file": "Read contents of a text file. Args: file_path (str), max_lines (int, optional)",
                "list_files": "List files in a directory. Args: directory_path (str, optional)"
            },
            "text_processor": {
                "to_uppercase": "Convert text to uppercase. Args: text (str)",
                "to_lowercase": "Convert text to lowercase. Args: text (str)", 
                "reverse_text": "Reverse text character order. Args: text (str)",
                "count_words": "Count words, characters, and lines. Args: text (str)"
            }
        }
    
    @resource
    def get_help(self) -> Dict[str, Any]:
        """
        Get general help information about the server.
        
        Returns:
            Dictionary containing help information
        """
        help_info = {
            "server_name": "FastMCP Basic Example Server",
            "description": "A demonstration MCP server showcasing basic tools and resources",
            "getting_started": {
                "1": "Use tools to perform operations like calculations, weather queries, etc.",
                "2": "Use resources to get configuration, help, and logs",
                "3": "All file operations are restricted to safe directories",
                "4": "Check logs for detailed operation history"
            },
            "available_categories": {
                "calculator": "Basic mathematical operations",
                "weather": "Weather information lookup",
                "file_reader": "Safe file reading operations", 
                "text_processor": "Text manipulation utilities"
            },
            "examples": {
                "calculation": "Use add(10, 5) to add numbers",
                "weather": "Use get_weather('seoul') for Seoul weather",
                "file_reading": "Use read_file('README.md') to read files",
                "text_processing": "Use to_uppercase('hello') to convert text"
            },
            "support": {
                "documentation": "Use get_tool_help(category) for specific tool help",
                "logs": "Use get_logs() to view server activity",
                "configuration": "Use get_config() for server settings"
            }
        }
        
        logger.info("HelpResource: General help information requested")
        return help_info
    
    @resource
    def get_tool_help(self, category: Optional[str] = None) -> Dict[str, Any]:
        """
        Get detailed help for specific tool categories.
        
        Args:
            category: Tool category (calculator, weather, file_reader, text_processor)
            
        Returns:
            Dictionary containing tool-specific help
        """
        if category is None:
            result = {
                "available_categories": list(self.tool_help.keys()),
                "usage": "Specify a category to get detailed help",
                "example": "get_tool_help('calculator')"
            }
            logger.info("HelpResource: Tool categories list requested")
            return result
        
        if category not in self.tool_help:
            result = {
                "error": f"Category '{category}' not found",
                "available_categories": list(self.tool_help.keys())
            }
            logger.warning(f"HelpResource: Unknown category '{category}' requested")
            return result
        
        result = {
            "category": category,
            "tools": self.tool_help[category],
            "total_tools": len(self.tool_help[category])
        }
        
        logger.info(f"HelpResource: Help for category '{category}' requested")
        return result