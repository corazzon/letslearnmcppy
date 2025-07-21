"""
Logs Resource

Provides access to server logs and activity history.
"""

from fastmcp import resource
from typing import Dict, Any, List
import os
import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

class LogsResource:
    """Logs resource for accessing server activity"""
    
    def __init__(self):
        self.log_file = Path("server.log")
    
    @resource
    def get_logs(self, max_lines: int = 50, level: str = "all") -> Dict[str, Any]:
        """
        Get recent server logs.
        
        Args:
            max_lines: Maximum number of log lines to return (default: 50)
            level: Log level filter (all, info, warning, error)
            
        Returns:
            Dictionary containing log entries
        """
        try:
            if not self.log_file.exists():
                return {
                    "message": "No log file found yet",
                    "log_file": str(self.log_file),
                    "logs": []
                }
            
            # Read log file
            with open(self.log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Get recent lines
            recent_lines = lines[-max_lines:] if len(lines) > max_lines else lines
            
            # Filter by log level if specified
            if level.lower() != "all":
                level_upper = level.upper()
                recent_lines = [
                    line for line in recent_lines 
                    if level_upper in line
                ]
            
            # Parse log entries
            log_entries = []
            for line in recent_lines:
                line = line.strip()
                if line:
                    log_entries.append({
                        "timestamp": self._extract_timestamp(line),
                        "level": self._extract_level(line),
                        "message": line
                    })
            
            result = {
                "log_file": str(self.log_file),
                "total_lines": len(lines),
                "returned_lines": len(log_entries),
                "filter_level": level,
                "logs": log_entries,
                "file_size": self.log_file.stat().st_size if self.log_file.exists() else 0,
                "last_modified": datetime.fromtimestamp(
                    self.log_file.stat().st_mtime
                ).isoformat() if self.log_file.exists() else None
            }
            
            logger.info(f"LogsResource: Retrieved {len(log_entries)} log entries (filter: {level})")
            return result
            
        except Exception as e:
            error_result = {
                "error": f"Failed to read logs: {str(e)}",
                "log_file": str(self.log_file)
            }
            logger.error(f"LogsResource: Error reading logs: {e}")
            return error_result
    
    def _extract_timestamp(self, log_line: str) -> str:
        """Extract timestamp from log line"""
        try:
            # Assuming format: "2025-07-21 10:30:00,123 - ..."
            if " - " in log_line:
                return log_line.split(" - ")[0]
            return "unknown"
        except:
            return "unknown"
    
    def _extract_level(self, log_line: str) -> str:
        """Extract log level from log line"""
        try:
            levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
            for level in levels:
                if level in log_line:
                    return level
            return "UNKNOWN"
        except:
            return "UNKNOWN"