# MarketPulse

MarketPulse tracks real-time market sentiment by analyzing financial news, tweets, and Reddit posts, then visualizes trends for traders.

## Features
- Automated scraping and NLP
- Sentiment correlation with stock prices
- Interactive dashboards with Plotly
- Daily Slack/email summaries

## Tech Stack
Python, FastAPI, Celery, PostgreSQL, Transformers, Plotly Dash

## Setup
1. Clone the repo
2. Add API keys to `.env`
3. Install dependencies: `pip install -r requirements.txt`
4. Run Celery worker: `celery -A app.main worker --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler`
5. Start FastAPI: `uvicorn app.main:app --reload`
6. Open dashboard at `/dashboard`
