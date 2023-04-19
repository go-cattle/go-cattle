import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load data from file
df = pd.read_csv("examples.txt", delimiter=":", header=None, names=["label", "text"])

# Clean data
df["text"] = df["text"].str.lower().str.strip()

# Extract features from text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Train the model
clf = MultinomialNB()
clf.fit(X, y)

# Test the model
input_text = "fever, anemia, decreased milk production"
input_features = vectorizer.transform([input_text.lower().strip()])
predicted_label = clf.predict(input_features)[0]

print("Predicted Disease: ", predicted_label)
