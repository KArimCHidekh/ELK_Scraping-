
from typing import Dict

from textblob import TextBlob


class SentimentAnalyzer:
    """A class that performs sentiment analysis on text."""

    def __init__(self):
        self.textblob = TextBlob

    def analyze_sentiment(self, text: str) -> Dict[float, float]:
        """Analyzes the sentiment of the given text and returns a dictionary containing the following keys:

            * `polarity`: A float between -1 and 1, where -1 represents a highly negative sentiment and 1 represents a highly positive sentiment.
            * `subjectivity`: A float between 0 and 1, where 0 represents an objective sentiment and 1 represents a subjective sentiment.

        Args:
            text: The text to analyze.

        Returns:
            A dictionary containing the polarity and subjectivity of the given text.
        """

        sentiment_analysis = self.textblob(text)
        sentiment_score = sentiment_analysis.sentiment.polarity
        sentiment_subjectivity = sentiment_analysis.sentiment.subjectivity
        return {
            "polarity": sentiment_score ,
            "subjectivity":  sentiment_subjectivity,
            "result": ("Positive" if(sentiment_score > 0) else "Neutral" if(sentiment_score == 0) else "Negative")
        }

