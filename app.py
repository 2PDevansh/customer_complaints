from flask import Flask, render_template, request
import pickle
import re
from deep_translator import GoogleTranslator
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

complaint_keywords = [
    'not', 'unable', 'issue', 'problem', 'complaint', 'error', 'fail', 'decline',
    'blocked', 'refund', 'charged', 'wrong', 'missing', 'late', 'money','deducted',
    'service', 'support', 'monetary', 'transaction', 'account', 'banking',
    'credit', 'debit', 'loan', 'payment', 'deposit', 'withdrawal', 'transfer',
    'statement', 'fee', 'interest', 'balance', 'fraud', 'scam', 'unauthorized',
    'unauthorized transaction', 'unauthorized charge', 'unauthorized payment',
    'unauthorized withdrawal', 'unauthorized transfer', 'unauthorized deposit',
    'unauthorized account', 'unauthorized banking', 'unauthorized credit',
    'unauthorized debit', 'unauthorized loan', 'unauthorized service',
    'unauthorized support', 'unauthorized monetary', 'unauthorized transaction',
    'unauthorized issue', 'unauthorized problem', 'unauthorized complaint',
    'unauthorized error', 'unauthorized fail', 'unauthorized decline',
    'unauthorized blocked', 'unauthorized refund', 'unauthorized charged',
    'unauthorized wrong', 'unauthorized missing', 'unauthorized late', 'unauthorized money'
]

def is_invalid_input(text):
    text = text.strip()
    if len(text) < 5:
        return True, " Complaint is too short."
    if re.fullmatch(r'[^a-zA-Z0-9\s]+', text) or re.fullmatch(r'(.)\1{3,}', text):
        return True, " Complaint looks like gibberish."
    return False, ""

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    predicted_category = ""
    warning = ""
    error = ""

    if request.method == 'POST':
        complaint_text = request.form.get('complaint', '').strip()

        if not complaint_text:
            warning = "Please enter a complaint first."
        else:
            is_invalid, reason = is_invalid_input(complaint_text)
            if is_invalid:
                warning = reason
            else:
                try:

                    translated_text = GoogleTranslator(source='auto', target='en').translate(complaint_text)

                    if not any(word in translated_text.lower() for word in complaint_keywords):
                        warning = " This doesn't appear to describe a complaint. Please describe the issue clearly."
                    else:
                        X = vectorizer.transform([translated_text])
                        pred = model.predict(X)
                        predicted_category = label_encoder.inverse_transform([pred[0]])[0]

                except Exception as e:
                    error = f"Prediction failed: {e}"

    return render_template('index.html',
                           translated_text=translated_text,
                           predicted_category=predicted_category,
                           warning=warning,
                           error=error)

if __name__ == '__main__':
    app.run(debug=True)
