#!/usr/bin/env python3
"""
FastMCP Basic Example Server

A simple MCP server implementation using FastMCP framework
that demonstrates basic tools and resources.
"""

import asyncio
import logging
from typing import Any, Dict, List
from fastmcp import FastMCP
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
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('server.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Create FastMCP server instance
server = FastMCP("FastMCP Basic Example")

def setup_tools():
    """Register all tools with the server"""
    # Calculator tool
    calculator = CalculatorTool()
    server.add_tool(calculator.add)
    server.add_tool(calculator.subtract)
    server.add_tool(calculator.multiply)
    server.add_tool(calculator.divide)
    
    # Weather tool
    weather = WeatherTool()
    server.add_tool(weather.get_weather)
    
    # File reader tool
    file_reader = FileReaderTool()
    server.add_tool(file_reader.read_file)
    server.add_tool(file_reader.list_files)
    
    # Text processor tool
    text_processor = TextProcessorTool()
    server.add_tool(text_processor.to_uppercase)
    server.add_tool(text_processor.to_lowercase)
    server.add_tool(text_processor.reverse_text)
    server.add_tool(text_processor.count_words)
    
    logger.info("All tools registered successfully")

def setup_resources():
    """Register all resources with the server"""
    # Configuration resource
    config_resource = ConfigResource()
    server.add_resource(config_resource.get_config)
    
    # Help resource
    help_resource = HelpResource()
    server.add_resource(help_resource.get_help)
    server.add_resource(help_resource.get_tool_help)
    
    # Logs resource
    logs_resource = LogsResource()
    server.add_resource(logs_resource.get_logs)
    
    logger.info("All resources registered successfully")

async def main():
    """Main server function"""
    logger.info("Starting FastMCP Basic Example Server...")
    
    try:
        # Setup tools and resources
        setup_tools()
        setup_resources()
        
        logger.info("Server setup completed")
        logger.info("Available tools:")
        for tool_name in server.list_tools():
            logger.info(f"  - {tool_name}")
        
        logger.info("Available resources:")
        for resource_name in server.list_resources():
            logger.info(f"  - {resource_name}")
        
        # Run the server
        await server.run()
        
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise
    finally:
        logger.info("Server shutting down...")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        exit(1)