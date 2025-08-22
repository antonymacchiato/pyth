### **Repository 4: Weather App**
```python
# Repository: python-weather-app
# Description: Fetch weather data using an external API.

import requests
from cachetools import cached, TTLCache
cache = TTLCache(maxsize=100, ttl=300)  

@cached(cache)
def get_weather(city, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        print(f"Weather in {city}: {weather}, Temperature: {temp}°C")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather  {e}")

# Example usage
get_weather("London", "your_api_key_here")
