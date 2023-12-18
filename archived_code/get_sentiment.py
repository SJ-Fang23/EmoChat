import spacy
from typing import Optional
from enum import Enum
import spacytextblob


nlp: Optional[spacy.language.Language] = None
def get_nlp() -> spacy.language.Language:
    global nlp
    if nlp is None:
        nlp = spacy.load('en_core_web_sm')
        nlp.add_pipe('spacytextblob')
    return nlp


Sentiment = Enum("Polarity", ["POSITIVE", "NEUTRAL", "NEGATIVE"])

def get_sentiment(
        text: str,
        negative_threshold: float = -0.2,
        positive_threshold: float = 0.2,
        debug: bool = False
) -> Sentiment:
    nlp = get_nlp()

    doc = nlp(text)
    polarity = doc._.blob.polarity
    if debug:
        print("Polarity: {0}".format(polarity))
    if polarity < negative_threshold:
        return Sentiment.NEGATIVE
    elif polarity > positive_threshold:
        return Sentiment.POSITIVE
    else:
        return Sentiment.NEUTRAL
