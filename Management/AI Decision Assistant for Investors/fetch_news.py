import requests

def fetch_news(api_key, query, page_size=10):
    url = f"https://newsapi.org/v2/everything?q={query}&pageSize={page_size}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        return [article['title'] for article in articles]
    else:
        raise Exception(f"Error fetching news: {response.status_code}")

