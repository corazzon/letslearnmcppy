"""
Text Processor Tool

Provides various text manipulation and processing utilities.
"""

from fastmcp import tool
from typing import Dict, Any
import re
import logging

logger = logging.getLogger(__name__)

class TextProcessorTool:
    """Text processor tool for string manipulation"""
    
    @tool
    def to_uppercase(self, text: str) -> Dict[str, Any]:
        """
        Convert text to uppercase.
        
        Args:
            text: Text to convert
            
        Returns:
            Dictionary containing original and converted text
        """
        result = {
            "original": text,
            "converted": text.upper(),
            "operation": "to_uppercase"
        }
        logger.info(f"TextProcessor: Converted text to uppercase (length: {len(text)})")
        return result
    
    @tool
    def to_lowercase(self, text: str) -> Dict[str, Any]:
        """
        Convert text to lowercase.
        
        Args:
            text: Text to convert
            
        Returns:
            Dictionary containing original and converted text
        """
        result = {
            "original": text,
            "converted": text.lower(),
            "operation": "to_lowercase"
        }
        logger.info(f"TextProcessor: Converted text to lowercase (length: {len(text)})")
        return result
    
    @tool
    def reverse_text(self, text: str) -> Dict[str, Any]:
        """
        Reverse the order of characters in text.
        
        Args:
            text: Text to reverse
            
        Returns:
            Dictionary containing original and reversed text
        """
        result = {
            "original": text,
            "converted": text[::-1],
            "operation": "reverse_text"
        }
        logger.info(f"TextProcessor: Reversed text (length: {len(text)})")
        return result
    
    @tool
    def count_words(self, text: str) -> Dict[str, Any]:
        """
        Count words, characters, and lines in text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary containing text statistics
        """
        lines = text.split('\n')
        words = re.findall(r'\b\w+\b', text)
        characters = len(text)
        characters_no_spaces = len(text.replace(' ', ''))
        
        result = {
            "text": text,
            "word_count": len(words),
            "character_count": characters,
            "character_count_no_spaces": characters_no_spaces,
            "line_count": len(lines),
            "words": words,
            "operation": "count_words"
        }
        
        logger.info(f"TextProcessor: Analyzed text - {len(words)} words, {characters} chars, {len(lines)} lines")
        return result