import requests

def get_forecast(city, api_key, days=3):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather forecast for {city}:")
        for i, item in enumerate(data['list'][:days * 8:8]):
            date = item['dt_txt'].split()[0]
            weather = item['weather'][0]['description']
            temp = item['main']['temp']
            print(f"Day {i + 1} ({date}): {weather}, Temperature: {temp}°C")
    else:
        print("Failed to fetch weather data.")

# Example usage
get_forecast("London", "your_api_key_here", days=3)
