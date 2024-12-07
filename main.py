import os
from data_scraping import scrape_news
from text_preprocessing import summarize_and_analyze
from database import save_to_db

# Отключаем многозадачность для токенизаторов
os.environ["TOKENIZERS_PARALLELISM"] = "false"

if __name__ == "__main__":
    country = "us"  
    news = scrape_news(country)

    if news:
        for article in news:
            title = article['title']
            content = article.get('content') 

            # Проверяем, что контент не None и достаточно длинный
            if content is None or len(content) < 10:
                print(f"Skipping article due to insufficient content or None: {title}")
                continue

            # Создание резюме и прогноз тональности
            summary, sentiment = summarize_and_analyze(content)

            
            save_to_db(title, content, summary, sentiment)

            
            print("Title:", title)
            print("Summary:", summary)
            print("Sentiment:", sentiment)
            print("------")
    else:
        print("No news found.")
