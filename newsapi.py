import requests
import secrets

NEWSAPI_KEY = 'd93fe74021514b0d96897aa6725cf6be' 
base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "country": "us",
    "apiKey": secrets.NEWSAPI_KEY,
    "q": "new hampshire"
}

response = requests.get(base_url, params)
result = response.json()
for item in result["articles"]:
    print(item["title"], "-", item["source"]["name"])
