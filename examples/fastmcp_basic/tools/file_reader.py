"""
File Reader Tool

Provides safe file reading capabilities within allowed directories.
"""

from fastmcp import tool
from typing import List, Dict, Any
import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class FileReaderTool:
    """File reader tool for safe file operations"""
    
    def __init__(self):
        # Define allowed directories for security
        self.allowed_dirs = [
            Path(__file__).parent.parent,  # fastmcp_basic directory
            Path(__file__).parent.parent.parent.parent,  # project root
        ]
    
    def _is_path_allowed(self, file_path: str) -> bool:
        """Check if the file path is within allowed directories"""
        try:
            abs_path = Path(file_path).resolve()
            return any(
                abs_path.is_relative_to(allowed_dir.resolve()) 
                for allowed_dir in self.allowed_dirs
            )
        except Exception:
            return False
    
    @tool
    def read_file(self, file_path: str, max_lines: int = 100) -> Dict[str, Any]:
        """
        Read contents of a text file safely.
        
        Args:
            file_path: Path to the file to read
            max_lines: Maximum number of lines to read (default: 100)
            
        Returns:
            Dictionary containing file contents and metadata
        """
        if not self._is_path_allowed(file_path):
            error_result = {
                "error": "File path not allowed for security reasons",
                "file_path": file_path
            }
            logger.warning(f"FileReader: Unauthorized access attempt to {file_path}")
            return error_result
        
        try:
            path = Path(file_path)
            
            if not path.exists():
                return {
                    "error": "File not found",
                    "file_path": file_path
                }
            
            if not path.is_file():
                return {
                    "error": "Path is not a file",
                    "file_path": file_path
                }
            
            # Read file contents
            with open(path, 'r', encoding='utf-8') as f:
                lines = []
                for i, line in enumerate(f):
                    if i >= max_lines:
                        break
                    lines.append(line.rstrip())
            
            result = {
                "file_path": file_path,
                "content": lines,
                "lines_read": len(lines),
                "file_size": path.stat().st_size,
                "truncated": len(lines) == max_lines
            }
            
            logger.info(f"FileReader: Read {len(lines)} lines from {file_path}")
            return result
            
        except UnicodeDecodeError:
            return {
                "error": "File contains non-text data or unsupported encoding",
                "file_path": file_path
            }
        except Exception as e:
            logger.error(f"FileReader: Error reading {file_path}: {e}")
            return {
                "error": f"Failed to read file: {str(e)}",
                "file_path": file_path
            }
    
    @tool
    def list_files(self, directory_path: str = ".") -> Dict[str, Any]:
        """
        List files and directories in a given path.
        
        Args:
            directory_path: Path to the directory to list (default: current directory)
            
        Returns:
            Dictionary containing list of files and directories
        """
        if not self._is_path_allowed(directory_path):
            error_result = {
                "error": "Directory path not allowed for security reasons",
                "directory_path": directory_path
            }
            logger.warning(f"FileReader: Unauthorized access attempt to {directory_path}")
            return error_result
        
        try:
            path = Path(directory_path)
            
            if not path.exists():
                return {
                    "error": "Directory not found",
                    "directory_path": directory_path
                }
            
            if not path.is_dir():
                return {
                    "error": "Path is not a directory", 
                    "directory_path": directory_path
                }
            
            files = []
            directories = []
            
            for item in sorted(path.iterdir()):
                if item.is_file():
                    files.append({
                        "name": item.name,
                        "size": item.stat().st_size,
                        "type": "file"
                    })
                elif item.is_dir():
                    directories.append({
                        "name": item.name,
                        "type": "directory"
                    })
            
            result = {
                "directory_path": directory_path,
                "files": files,
                "directories": directories,
                "total_files": len(files),
                "total_directories": len(directories)
            }
            
            logger.info(f"FileReader: Listed {len(files)} files and {len(directories)} directories in {directory_path}")
            return result
            
        except Exception as e:
            logger.error(f"FileReader: Error listing {directory_path}: {e}")
            return {
                "error": f"Failed to list directory: {str(e)}",
                "directory_path": directory_path
            }