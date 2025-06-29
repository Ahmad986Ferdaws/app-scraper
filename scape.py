# app/scraper.py

import requests
from bs4 import BeautifulSoup
import praw
import tweepy
import os

# Reddit setup
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="MarketPulseBot/0.1"
)

# Twitter setup
client = tweepy.Client(bearer_token=os.getenv("TWITTER_BEARER_TOKEN"))

def scrape_reddit(subreddit_name="wallstreetbets", limit=10):
    posts = []
    for submission in reddit.subreddit(subreddit_name).hot(limit=limit):
        posts.append({
            "title": submission.title,
            "selftext": submission.selftext,
            "score": submission.score
        })
    return posts

def scrape_twitter(query="stock market", max_results=10):
    tweets = client.search_recent_tweets(query=query, max_results=max_results)
    results = []
    for tweet in tweets.data:
        results.append({
            "text": tweet.text,
            "id": tweet.id
        })
    return results

def scrape_news(url="https://finance.yahoo.com"):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    headlines = []
    for item in soup.find_all("h3"):
        headlines.append(item.get_text())
    return headlines

if __name__ == "__main__":
    reddit_posts = scrape_reddit()
    twitter_posts = scrape_twitter()
    news_headlines = scrape_news()

    print("Reddit Posts:", reddit_posts)
    print("Twitter Posts:", twitter_posts)
    print("News Headlines:", news_headlines)
