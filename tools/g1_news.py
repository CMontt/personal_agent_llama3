import feedparser
from typing import List
from config.settings import RSS_G1, RSS_MAX_ARTICLES


def fetch_g1_news() -> List[dict]:
    feed = feedparser.parse(RSS_G1)
    articles = []
    for entry in feed.entries[:RSS_MAX_ARTICLES]:
        articles.append({
            "title": entry.get("title", ""),
            "summary": entry.get("summary", ""),
            "link": entry.get("link", "")
        })
    
    return articles

def g1_news(notices: None) -> str:
    news_list = fetch_g1_news()
    
    if not news_list:
        return "Nenhuma notícia encontrada no G1"
    
    return "\n".join([f"{i+1}. {n['title']}\n{n['summary']}\n{n['link']}" for i, n in enumerate(news_list)])
    