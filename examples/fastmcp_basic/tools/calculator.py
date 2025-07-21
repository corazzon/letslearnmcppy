"""
Calculator Tool

Provides basic mathematical operations for the MCP server.
"""

from fastmcp import tool
from typing import Union
import logging

logger = logging.getLogger(__name__)

class CalculatorTool:
    """Calculator tool providing basic math operations"""
    
    @tool
    def add(self, a: float, b: float) -> float:
        """
        Add two numbers together.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        result = a + b
        logger.info(f"Calculator: {a} + {b} = {result}")
        return result
    
    @tool  
    def subtract(self, a: float, b: float) -> float:
        """
        Subtract second number from first number.
        
        Args:
            a: First number (minuend)
            b: Second number (subtrahend)
            
        Returns:
            The difference of a and b
        """
        result = a - b
        logger.info(f"Calculator: {a} - {b} = {result}")
        return result
    
    @tool
    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        result = a * b
        logger.info(f"Calculator: {a} × {b} = {result}")
        return result
    
    @tool
    def divide(self, a: float, b: float) -> Union[float, str]:
        """
        Divide first number by second number.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            The quotient of a and b, or error message if division by zero
        """
        if b == 0:
            error_msg = "Error: Division by zero is not allowed"
            logger.warning(f"Calculator: {a} ÷ {b} - {error_msg}")
            return error_msg
        
        result = a / b
        logger.info(f"Calculator: {a} ÷ {b} = {result}")
        return result