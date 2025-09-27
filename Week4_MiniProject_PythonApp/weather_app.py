import requests

city = input("Enter city name: ")
api_key = "YOUR_API_KEY"  # Use OpenWeatherMap API key
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        print(f"Weather in {city}: {data['weather'][0]['description']}, Temp: {data['main']['temp']}°C")
    else:
        print(data["message"])
except Exception as e:
    print("Error fetching weather:", e)
