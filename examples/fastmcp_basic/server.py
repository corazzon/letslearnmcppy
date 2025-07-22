#!/usr/bin/env python3
"""
FastMCP Basic Server

A simple MCP server demonstrating basic tools and resources.
"""

import logging
from datetime import datetime
from fastmcp import FastMCP

# Import tool and resource classes
from tools.calculator import CalculatorTool
from tools.weather import WeatherTool
from tools.file_reader import FileReaderTool
from tools.text_processor import TextProcessorTool
from resources.config import ConfigResource
from resources.help import HelpResource
from resources.logs import LogsResource

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create the FastMCP server
server = FastMCP("FastMCP Basic Server")

# Initialize tool instances
calculator = CalculatorTool()
weather = WeatherTool()
file_reader = FileReaderTool()
text_processor = TextProcessorTool()

# Initialize resource instances
config_resource = ConfigResource()
help_resource = HelpResource()
logs_resource = LogsResource()

# Register calculator tools
@server.tool
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return calculator.add(a, b)

@server.tool
def subtract(a: float, b: float) -> float:
    """Subtract second number from first number."""
    return calculator.subtract(a, b)

@server.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return calculator.multiply(a, b)

@server.tool
def divide(a: float, b: float) -> float:
    """Divide first number by second number."""
    return calculator.divide(a, b)

# Register weather tool
@server.tool
def get_weather(city: str) -> dict:
    """Get current weather information for a city."""
    return weather.get_weather(city)

# Register file reader tools
@server.tool
def list_files(directory_path: str = ".") -> dict:
    """List files and directories in a given path."""
    return file_reader.list_files(directory_path)

@server.tool
def read_file(file_path: str, max_lines: int = 100) -> dict:
    """Read contents of a text file safely."""
    return file_reader.read_file(file_path, max_lines)

# Register text processor tools
@server.tool
def count_words(text: str) -> dict:
    """Count words, characters, and lines in text."""
    return text_processor.count_words(text)

@server.tool
def reverse_text(text: str) -> str:
    """Reverse the order of characters in text."""
    return text_processor.reverse_text(text)

@server.tool
def to_uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text_processor.to_uppercase(text)

@server.tool
def to_lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text_processor.to_lowercase(text)

# Register resources
@server.resource("config://server")
def get_config() -> str:
    """Get server configuration information."""
    return config_resource.get_config()

@server.resource("help://tools/{tool_name}")
def get_help(tool_name: str = "all") -> str:
    """Get help information for tools."""
    return help_resource.get_help(tool_name)

@server.resource("logs://server/{log_type}")
def get_logs(log_type: str = "all") -> str:
    """Get server logs."""
    return logs_resource.get_logs(log_type)

def main():
    """Main function to run the server."""
    logger.info("Starting FastMCP Basic Server...")
    
    # Let FastMCP handle the event loop
    server.run()

if __name__ == "__main__":
    main()
