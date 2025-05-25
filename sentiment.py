
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiments(reviews):
    results = []
    for review in reviews:
        score = analyzer.polarity_scores(review)
        if score['compound'] >= 0.05:
            sentiment = 'Positive'
        elif score['compound'] <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        results.append({
            "review": review,
            "sentiment": sentiment,
            "compound": score["compound"]
        })
    return results
