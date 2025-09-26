from textblob import TextBlob
import streamlit as st
import pandas as pd
import plotly.express as px

# Mocked financial headlines for demonstration
mock_headlines = {
    "AAPL": [
        "Apple reports record quarterly earnings",
        "iPhone sales decline amid global slowdown",
        "Apple announces new AI features in iOS",
        "Investors optimistic about Apple’s future",
        "Apple faces regulatory scrutiny in Europe"
    ],
    "TSLA": [
        "Tesla stock surges after strong delivery numbers",
        "Elon Musk teases new autonomous driving update",
        "Tesla faces production delays in China",
        "Analysts downgrade Tesla amid valuation concerns",
        "Tesla expands into new markets"
    ],
    "MSFT": [
        "Microsoft launches new AI-powered Copilot",
        "Azure growth slows down in Q2",
        "Microsoft acquires cybersecurity firm",
        "Windows 11 adoption exceeds expectations",
        "Microsoft faces antitrust probe"
    ]
}

st.title("📈 Financial Sentiment Analyzer")
st.write("Analyze sentiment of mocked financial headlines for selected stock tickers.")

ticker = st.selectbox("Select a stock ticker:", options=["AAPL", "TSLA", "MSFT"])

st.subheader(f"Recent Headlines for {ticker}")
headlines = mock_headlines[ticker]
for i, headline in enumerate(headlines, 1):
    st.write(f"{i}. {headline}")

sentiment_scores = []
for headline in headlines:
    blob = TextBlob(headline)
    sentiment_scores.append(blob.sentiment.polarity)

df = pd.DataFrame({
    "Headline": headlines,
    "Sentiment Score": sentiment_scores,
    "Index": list(range(1, len(headlines) + 1))
})

fig = px.line(df, x="Index", y="Sentiment Score", markers=True,
              title=f"Sentiment Trend for {ticker}",
              labels={"Index": "Headline Index", "Sentiment Score": "Polarity Score"})

st.plotly_chart(fig, use_container_width=True)
