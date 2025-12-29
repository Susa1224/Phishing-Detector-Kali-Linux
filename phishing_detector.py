from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Training Data (Standard Phishing Patterns)
data = [
    "Your account is suspended. Click here to verify.",
    "Meeting reminder for tomorrow at 2 PM.",
    "Urgent: You won a gift card! Claim now.",
    "Please review the attached invoice.",
    "Action required: Security breach detected on your login."
]
labels = ["Phishing", "Safe", "Phishing", "Safe", "Phishing"]

# 2. Process and Train
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data)
model = MultinomialNB()
model.fit(X, labels)

# 3. User Interface
print("\n" + "="*40)
print(" KALI LINUX: AI PHISHING DETECTOR ")
print("="*40)
email_text = input("Enter email content to scan: ")
prediction = model.predict(vectorizer.transform([email_text]))

print(f"\n[+] SCAN RESULT: {prediction[0]}")
print("="*40)