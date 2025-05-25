
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def display_sentiment_chart(results):
    df = pd.DataFrame(results)
    sentiment_counts = df['sentiment'].value_counts()
    st.subheader("Sentiment Distribution")
    fig, ax = plt.subplots()
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="coolwarm", ax=ax)
    st.pyplot(fig)

def display_reviews_table(results):
    st.subheader("All Reviews")
    df = pd.DataFrame(results)
    st.dataframe(df[['review', 'sentiment']])
