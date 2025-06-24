import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Feedback Sentiment Dashboard", layout="wide")
st.title("🧠 Sentiment & Clustering Dashboard")
st.caption("Created by Arihant Singh | Data Science Project")

# Upload or enter data
st.subheader("1️⃣ Load Feedback")
option = st.radio("Select input method:", ["Upload CSV", "Manual Entry", "Load Sample Data"])

if option == "Upload CSV":
    uploaded_file = st.file_uploader("Upload a CSV with a 'feedback' column", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
elif option == "Manual Entry":
    text_input = st.text_area("Enter feedbacks (one per line)", height=200)
    if text_input:
        data = text_input.strip().split("\n")
        df = pd.DataFrame({'feedback': data})
elif option == "Load Sample Data":
    df = pd.read_csv("large_feedback_sample.csv")  # Make sure to place this file in the same folder

if 'df' in locals():
    # Sentiment classification using TextBlob
    def get_sentiment(text):
        return "Positive" if TextBlob(text).sentiment.polarity > 0 else "Negative"
    df['sentiment'] = df['feedback'].apply(get_sentiment)

    # Vectorize and classify
    tfidf = TfidfVectorizer(stop_words='english')
    X = tfidf.fit_transform(df['feedback'])
    y = df['sentiment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    # Clustering
    kmeans = KMeans(n_clusters=2, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)

    # Dimensionality reduction
    reduced = PCA(n_components=2).fit_transform(X.toarray())
    df['pca1'] = reduced[:, 0]
    df['pca2'] = reduced[:, 1]

    # Show metrics
    st.metric("🔍 Sentiment Model Accuracy", f"{acc * 100:.2f}%")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 Sentiment Distribution")
        sentiment_counts = df['sentiment'].value_counts()
        fig1, ax1 = plt.subplots(figsize=(4, 3))
        sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, ax=ax1, palette="viridis")
        ax1.set_ylabel("Count")
        st.pyplot(fig1)

    with col2:
        st.subheader("📊 Cluster Scatter (PCA)")
        fig2, ax2 = plt.subplots(figsize=(4, 3))
        sns.scatterplot(data=df, x='pca1', y='pca2', hue='cluster', style='sentiment', palette="Set2", ax=ax2)
        ax2.set_title("Cluster View (2D)")
        st.pyplot(fig2)

    st.subheader("📋 Feedback Table")
    st.dataframe(df[['feedback', 'sentiment', 'cluster']])

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Results", csv, "feedback_classified.csv", "text/csv")

else:
    st.info("Please upload or enter feedback to begin.")
