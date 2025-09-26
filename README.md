# Financial-Sentiment-Analyzer
Financial Sentiment Analyzer for tcsai hackathon
Financial Sentiment Analyzer
🧠 Project Overview
  The Financial Sentiment Analyzer is an AI-powered web application that
  analyzes the sentiment of financial news headlines for selected stock tickers.
  It uses Natural Language Processing (NLP) to determine whether the
  sentiment of each headline is positive, negative, or neutral, and visualizes
  the sentiment trend over time.
  This tool is ideal for traders, analysts, and financial enthusiasts who want to
  gauge market sentiment and make informed decisions.
🚀 Features
  • Select stock tickers (e.g., AAPL, TSLA, MSFT)
  • View mocked financial news headlines
  • Perform sentiment analysis using TextBlob
  • Visualize sentiment scores with interactive Plotly charts
  • Simple and intuitive Streamlit interface 🛠️
Installation Guide
  Prerequisites
  • Python 3.7 or higher
  • pip (Python package installer)
Steps
  1. Clone or download the project files.
  2. Open a terminal and navigate to the project directory.
  3. (Optional) Create and activate a virtual environment:
  a. python -m venv venv
  b. venv\Scripts\activate # On Windows
  c. source venv/bin/activate # On macOS/Linux
4.Install required dependencies:
  a) pip install streamlit textblob plotly pandas▶️
How to Run the App
  After installation, run the app using:
  a) streamlit run sentiment_app.py
  📋 Usage Instructions
    1. Launch the app in your browser.
    2. Select a stock ticker from the dropdown (AAPL, TSLA, MSFT).
    3. View the mocked financial headlines.
    4. The app will analyze each headline and assign a sentiment score.
    5. A line chart will display sentiment trends over time.
