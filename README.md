  # 🏦 Bank Complaint Classifier (Multilingual)
  
  🏦 Bank Complaint Classifier (Multilingual) – Flask Version
This web application categorizes banking and financial complaints into designated groups utilizing a trained machine learning model.

Designed with Flask for a conventional backend-server methodology, while leveraging Scikit-learn, Naive Bayes, and Deep Translator for multilingual capabilities.
  
  ---
  
  ##  Categorizes customer complaints into financial classifications

 Accepts input in various languages (automatically translated to English)

 Filters out irrelevant, courteous, or nonsensical text

 Utilizes a Naive Bayes classifier trained on actual complaint data for predictions

💻 Web interface designed with HTML/CSS (through Flask templates)  
  
  ---

##  Model Info

- **Model:** Multinomial Naive Bayes  
- **Vectorizer:** CountVectorizer  
- **Encoder:** LabelEncoder  
- **Training Data:** Custom CSV dataset of labeled bank complaints *(not uploaded due to file size limits)*  
- **Model Format:** Serialized using `pickle`  

---

##  How It Works

1. User submits a complaint (in any language)  
2. Text is translated to English (if needed)  
3. Input is vectorized and passed to a trained model  
4. The app returns the most likely complaint category  

---

## 🖥️ TechStack

Backend: Flask

Machine Learning: Scikit-learn

Translation: Deep Translator

Vectorization: CountVectorizer

---

## 🧠 Backend

- Machine learning model serialized using `pickle`  
- Translation handled via [`deep-translator`](https://pypi.org/project/deep-translator/) (Google Translate)  
- Input validation with regex and keyword filtering  

---

## Initiating the Process

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
python app.py
```

