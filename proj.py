import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd


df = pd.read_csv("complaints.csv")
df = df[['Consumer complaint narrative', 'Product']].dropna()
df.columns = ['text', 'label']


label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['label'])


vectorizer = CountVectorizer(stop_words='english', max_features=3000)
X = vectorizer.fit_transform(df['text'])


model = MultinomialNB()
model.fit(X, y)


pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(label_encoder, open("label_encoder.pkl", "wb")) 
