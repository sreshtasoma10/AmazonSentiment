
import streamlit as st
from amazon_scraper import extract_reviews
from sentiment import analyze_sentiments
from utils import display_sentiment_chart, display_reviews_table

st.title("Amazon Product Review Sentiment Analysis")

url = st.text_input("Enter Amazon Product Review URL")

if url:
    with st.spinner("Scraping reviews..."):
        reviews = extract_reviews(url)
    if not reviews:
        st.warning("No reviews found. Please check the URL.")
    else:
        with st.spinner("Analyzing sentiments..."):
            results = analyze_sentiments(reviews)
        display_sentiment_chart(results)
        display_reviews_table(results)
