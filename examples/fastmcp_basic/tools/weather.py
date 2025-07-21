"""
Weather Tool

Provides weather information using mock data for demonstration purposes.
"""

from fastmcp import tool
from typing import Dict, Any
import random
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class WeatherTool:
    """Weather tool providing mock weather data"""
    
    # Mock weather data for different cities
    WEATHER_DATA = {
        "seoul": {
            "city": "Seoul",
            "country": "South Korea",
            "conditions": ["Sunny", "Cloudy", "Rainy", "Snow"],
            "temp_range": (-10, 35)
        },
        "tokyo": {
            "city": "Tokyo", 
            "country": "Japan",
            "conditions": ["Sunny", "Cloudy", "Rainy"],
            "temp_range": (0, 40)
        },
        "newyork": {
            "city": "New York",
            "country": "United States", 
            "conditions": ["Sunny", "Cloudy", "Rainy", "Snow"],
            "temp_range": (-20, 40)
        },
        "london": {
            "city": "London",
            "country": "United Kingdom",
            "conditions": ["Cloudy", "Rainy", "Sunny"],
            "temp_range": (-5, 30)
        }
    }
    
    @tool
    def get_weather(self, city: str) -> Dict[str, Any]:
        """
        Get current weather information for a city.
        
        Args:
            city: Name of the city (seoul, tokyo, newyork, london)
            
        Returns:
            Dictionary containing weather information
        """
        city_key = city.lower().replace(" ", "")
        
        if city_key not in self.WEATHER_DATA:
            available_cities = ", ".join(self.WEATHER_DATA.keys())
            error_result = {
                "error": f"City '{city}' not found",
                "available_cities": available_cities
            }
            logger.warning(f"Weather: City '{city}' not found")
            return error_result
        
        city_data = self.WEATHER_DATA[city_key]
        
        # Generate random weather data
        condition = random.choice(city_data["conditions"])
        temp_min, temp_max = city_data["temp_range"]
        temperature = random.randint(temp_min, temp_max)
        humidity = random.randint(30, 90)
        
        weather_result = {
            "city": city_data["city"],
            "country": city_data["country"],
            "temperature": f"{temperature}°C",
            "condition": condition,
            "humidity": f"{humidity}%",
            "timestamp": datetime.now().isoformat(),
            "note": "This is mock data for demonstration purposes"
        }
        
        logger.info(f"Weather: Retrieved data for {city_data['city']}")
        return weather_result