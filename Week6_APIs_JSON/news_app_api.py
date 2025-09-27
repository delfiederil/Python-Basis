import requests

api_key = "YOUR_NEWSAPI_KEY"  # Get from newsapi.org
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

try:
    response = requests.get(url)
    data = response.json()
    
    if data["status"] == "ok":
        articles = data["articles"][:5]  # Show top 5 headlines
        for idx, article in enumerate(articles, start=1):
            print(f"{idx}. {article['title']}")
    else:
        print("Error:", data["message"])
except Exception as e:
    print("Error fetching news:", e)
