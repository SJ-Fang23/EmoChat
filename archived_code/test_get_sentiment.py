from main_driver.get_sentiment import get_sentiment
import sys
import os

text = sys.argv[1] or "It was the best of times, it was the worst of times."

sentiment = get_sentiment(text, debug=not not os.environ.get("DEBUG"))

print("Sentiment: {0}".format(sentiment))