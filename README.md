#  Bank Complaint Classifier (Multilingual)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-WebApp-black.svg)
![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange.svg)
![NLP](https://img.shields.io/badge/NLP-Text%20Classification-green.svg)
![Translation](https://img.shields.io/badge/Multilingual-Deep%20Translator-blueviolet.svg)
![Status](https://img.shields.io/badge/Project-Completed-success.svg)

A **multilingual banking complaint classification web application** that automatically categorizes customer complaints into predefined financial categories using **Machine Learning and NLP**.

Built with **Flask** for a traditional backend-driven architecture and powered by **Scikit-learn, Naive Bayes**, and **Deep Translator** to support inputs in **multiple languages** .

---

##  Project Highlights

- Multilingual Complaint Classification  
- Real-world Financial NLP Use Case  
- Lightweight & Fast Inference  
- Server-side ML Deployment using Flask  

---

##  Features

- Categorizes banking & financial complaints into defined groups  
- Accepts **complaints in multiple languages**  
- Automatically translates text to English  
- Filters irrelevant, polite, or nonsensical inputs  
- Uses a **Naive Bayes classifier trained on real complaint data**  
- Simple & clean web interface using **HTML/CSS + Flask templates**  
- Lightweight model with fast predictions  

---

##  Machine Learning Details

- **Model**: Multinomial Naive Bayes  
- **Vectorizer**: CountVectorizer  
- **Label Encoding**: LabelEncoder  
- **Training Data**: Custom CSV dataset of labeled bank complaints  
  > *(Dataset not uploaded due to file size constraints)*  
- **Model Format**: Serialized using `pickle`  

---

##  How It Works

- User submits a complaint (any language)  
- Text is translated to English (if required)  
- Input is cleaned and vectorized  
- Trained ML model predicts complaint category  
- Most probable classification is returned to the user  

---

##  Project Structure
```
customer_complaints/
│
├── templates/ # HTML templates (Flask UI)
├── static/ # CSS / assets
├── model/
│ ├── complaint_model.pkl # Trained ML model
│ ├── vectorizer.pkl # CountVectorizer
│ └── encoder.pkl # LabelEncoder
│
├── app.py # Flask application
├── requirements.txt # Dependencies
└── README.md # Project documentation

```

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

