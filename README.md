# Sentiment Analyzer & Dashboard

---

## 🚀 Overview

This project is an interactive Streamlit dashboard that:

* Classifies sentiment (Positive / Negative) of user feedback using NLP
* Clusters users based on feedback content
* Visualizes data with charts and 2D PCA scatter plots
* Supports CSV upload, manual entry, or sample data
* Allows CSV export of results

All features are packaged in a single file (`app.py`) and run via a clean graphical interface.

---

## 🌐 Live App

Try the deployed app here: [https://feedbackanalyzer.streamlit.app/](https://feedbackanalyzer.streamlit.app/)

---

## 🧠 Concepts Used

| Module                       | Feature in Project                      |
| ---------------------------- | --------------------------------------- |
| Python + Pandas              | Data processing                         |
| NLP (TextBlob)               | Sentiment polarity detection            |
| Classification (Naive Bayes) | Predicting sentiment                    |
| Clustering (KMeans)          | User behavior grouping                  |
| Dimensionality Reduction     | PCA used to visualize feedback clusters |
| Streamlit                    | GUI for interaction and visualization   |
| Matplotlib & Seaborn         | For visual plots and insights           |
| Git & GitHub                 | Project version control and portfolio   |

---

## 🗂️ Project Structure

```
📁 sentiment-clustering-dashboard
├── app.py                   # Full working Streamlit app
├── large_feedback_sample.csv  # Sample dataset for testing
├── README.md               # Project documentation
├── requirements.txt              # Project Libraries
```

---

## 📸 Screenshots

> Include screenshots of:

## ![s1](https://github.com/user-attachments/assets/c9616824-3ab0-43df-9fb4-5f65904663b9)


## ![s2](https://github.com/user-attachments/assets/f551bb5e-832c-440d-8fad-ec346b3be924)


## ![s3](https://github.com/user-attachments/assets/e1f5fb6e-8eb3-489b-8451-75c43b95c0dd)


---

## ▶️ How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/sentiment-clustering-dashboard.git
cd sentiment-clustering-dashboard
```

### 2. Install Dependencies

```bash
pip install streamlit
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 📁 Sample CSV Format

```csv
feedback
"The product is amazing!"
"Worst experience ever."
"Great support and fast delivery."
```

---

## 📝 Features

* 📤 CSV Upload / 📄 Manual Entry / 🔁 Sample Load
* 📊 Sentiment Analysis
* 🧠 KMeans Clustering
* 🧮 PCA Visualization
* 📈 Charts with Seaborn
* 📥 Result CSV Export
* 🎓 Clean GUI using streamlit

---

#### 🧮 Author:

**Name:** Arihant Singh
**Roll No.:** 2300320130063
**Branch:** IT-B
**Semester:** 4
**Academic Year:** 2024–25

**Course Code:** VACS043
**Course Title:** Emerging Technology and Data Science Training
**Course Project:** Data Science with Python & Machine Learning
**Guided By:** Ms. Shalini Singh
