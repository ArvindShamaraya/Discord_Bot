import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

def get_weather(city: str) -> str:
    """Fetches weather data from OpenWeatherMap API."""
    # Construct the API URL with the city and API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    
    # Send the GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response into a dictionary
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        description = weather['description']
        
        # Return a formatted string with the weather information
        return f"The weather in {city} is {description} with a temperature of {temperature}°C."
    else:
        # If the request failed, return a helpful error message
        return f"Sorry, I couldn't find the weather for {city}. Please check the city name and try again."
