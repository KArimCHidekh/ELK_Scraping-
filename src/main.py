from fastapi import FastAPI, Request, Response
from fastapi import FastAPI, Body, HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
from src.SentimentAnalyzer import SentimentAnalyzer

app = FastAPI()


class Post(BaseModel):
    text: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Define a GET endpoint for performing sentiment analysis
@app.get("/sentiment_analysis")
async def get_sentiment_analysis(post: Post = Body(...)):
    """Performs sentiment analysis on the given text and returns a JSON response with the sentiment score."""
    print(post)
    return SentimentAnalyzer().analyze_sentiment(post.text)
