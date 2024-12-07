import pandas as pd
import streamlit as st
from database import connect_db

def fetch_data():
    db = connect_db()
    query = "SELECT * FROM news_articles"
    df = pd.read_sql(query, db)
    db.close()
    return df

def dashboard():
    st.title("Дашборд анализа новостей")
    data = fetch_data()
    st.dataframe(data)

    sentiment_counts = data['sentiment'].value_counts()
    st.bar_chart(sentiment_counts)

if __name__ == "__main__":
    dashboard()
