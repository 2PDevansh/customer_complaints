# 🏦 Bank Complaint Classifier (Multilingual)

This web application classifies banking and financial complaints into specific categories using a trained machine learning model.

Built with **Streamlit** for a fast and interactive frontend, and powered by **Scikit-learn** and **Naive Bayes** on the backend.

---

## 🔍 Features

- ✅ Classifies customer complaints into predefined financial categories  
- 🌐 Accepts input in **multiple languages** (auto-translated to English)  
- 🛡 Filters irrelevant, polite, or gibberish text  
- ☁️ Provides real-time prediction with confidence  
- ⚡ Built with Python, Scikit-learn, and Streamlit  

---

## 🧠 Model Info

- **Model:** Multinomial Naive Bayes  
- **Vectorizer:** CountVectorizer  
- **Encoder:** LabelEncoder  
- **Training Data:** Custom CSV dataset of labeled bank complaints *(not uploaded due to file size limits)*  
- **Model Format:** Serialized using `pickle`  

---

## 🎯 How It Works

1. User submits a complaint (in any language)  
2. Text is translated to English (if needed)  
3. Input is vectorized and passed to a trained model  
4. The app returns the most likely complaint category  

---

## 🖥️ Frontend

The UI is built with **Streamlit**, providing a simple, responsive, and user-friendly interface.  
Users can paste their complaints directly into a text area and get results instantly.

---

## 🧠 Backend

- Machine learning model serialized using `pickle`  
- Translation handled via [`deep-translator`](https://pypi.org/project/deep-translator/) (Google Translate)  
- Input validation with regex and keyword filtering  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/2PDevansh/customer_complaints.git
cd customer_complaints
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run The App
```bash
streamlit run app.py
```

