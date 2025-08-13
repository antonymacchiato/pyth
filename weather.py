### **Repository 4: Weather App**
```python
# Repository: python-weather-app
# Description: Fetch weather data using an external API.

import requests

def get_weather(city, api_key):
    """Fetch weather data for a city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        print(f"Weather in {city}: {weather}, Temperature: {temp}°C")
    else:
        print("Failed to fetch weather data.")

# Example usage
get_weather("London", "your_api_key_here")
