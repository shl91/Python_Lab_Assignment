import requests

api_key= '51ba1b6b5e584b1f8e6c7be21d7fd729'

def get_latest_news():
    print('Please wait a moment.')
    base_url = f'https://newsapi.org/v2/top-headlines'
    parameters = {
        'apiKey': api_key,
        'sources': 'bbc-news',  
        'pageSize': 5,
    }

    response = requests.get(base_url, params=parameters)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])

        if articles:
            print("Latest News Headlines:")
            for idx, article in enumerate(articles, start=1):
                title = article.get('title', 'N/A')
                print(f"{idx}. {title}")
        else:
            print("No news articles found.")
    else:
        print("Failed to fetch news data.")