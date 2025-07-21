"""
Configuration Resource

Provides server configuration information.
"""

from fastmcp import resource
from typing import Dict, Any
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class ConfigResource:
    """Configuration resource for server settings"""
    
    @resource
    def get_config(self) -> Dict[str, Any]:
        """
        Get server configuration information.
        
        Returns:
            Dictionary containing server configuration
        """
        config = {
            "server_name": "FastMCP Basic Example",
            "version": "1.0.0",
            "description": "A basic MCP server implementation using FastMCP framework",
            "features": [
                "Calculator tools",
                "Weather information", 
                "File reading",
                "Text processing"
            ],
            "supported_operations": {
                "tools": [
                    "add", "subtract", "multiply", "divide",
                    "get_weather",
                    "read_file", "list_files", 
                    "to_uppercase", "to_lowercase", "reverse_text", "count_words"
                ],
                "resources": [
                    "get_config", "get_help", "get_tool_help", "get_logs"
                ]
            },
            "security": {
                "file_access": "restricted_to_allowed_directories",
                "logging": "enabled",
                "error_handling": "graceful"
            },
            "runtime_info": {
                "startup_time": datetime.now().isoformat(),
                "python_version": "3.8+",
                "framework": "FastMCP"
            }
        }
        
        logger.info("ConfigResource: Configuration information requested")
        return config