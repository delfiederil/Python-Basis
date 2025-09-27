import requests
import json

city = input("Enter city name: ")
api_key = "YOUR_API_KEY"  # Get from OpenWeatherMap or any free weather API
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("Error:", data["message"])
except Exception as e:
    print("Error fetching data:", e)
