import pandas as pd
from collections import defaultdict

# Read data from file
with open('example.txt', 'r') as f:
    data = f.read()

# Split data into disease records
records = data.strip().split('\n\n')

# Parse records into a dictionary
diseases = defaultdict(dict)
for record in records:
    lines = record.strip().split('\n')
    for line in lines:
        key, value = line.split(':')
        diseases[lines[0].split(':')[1].strip()][key.strip()] = value.strip()

# Create dictionary mapping symptoms to their frequency in each disease
symptoms = {}
for disease, data in diseases.items():
    symptoms[disease] = {}
    for symptom in data['Symptoms'].split(','):
        symptoms[disease][symptom.strip()] = 1

# Create feature matrix X and target vector y
X = pd.DataFrame(symptoms).fillna(0)
y = pd.Series(list(symptoms.keys()))

# Define the Naive Bayes Classifier
class NaiveBayesClassifier:
    
    def __init__(self):
        self.priors = None
        self.likelihoods = None
    
    def fit(self, X, y):
        # Calculate priors
        self.priors = y.value_counts(normalize=True)
        # Calculate likelihoods
        self.likelihoods = {}
        for feature in X.columns:
            self.likelihoods[feature] = {}
            for class_val in y.unique():
                self.likelihoods[feature][class_val] = (X.loc[y == class_val, feature].sum() + 1) / (y == class_val).sum() # Add-one smoothing
    
    def predict(self, X):
        # Calculate posterior probabilities
        posteriors = pd.DataFrame(index=X.index, columns=self.priors.index)
        for disease, prior in self.priors.items():
            posteriors[disease] = prior * X.apply(lambda x: self.likelihoods[x.name][disease]**x, axis=0).prod(axis=1)
        # Normalize posteriors
        posteriors = posteriors.div(posteriors.sum(axis=1), axis=0)
        # Return class with highest posterior probability
        return posteriors.idxmax(axis=1)

# Train the Naive Bayes Classifier
clf = NaiveBayesClassifier()
clf.fit(X, y)

# Function to predict disease based on user input
def predict_disease(input_str):
    input_symptoms = input_str.lower().split(',')
    input_symptoms = [s.strip() for s in input_symptoms]
    input_vector = pd.Series([1 if s in input_symptoms else 0 for s in X.columns])
    predicted_disease = clf.predict(pd.DataFrame([input_vector], columns=X.columns))[0]
    predicted_remedies = diseases[predicted_disease]['Remedies'].split(',')
    return predicted_disease, [r.strip() for r in predicted_remedies]

# Example usage
input_str = input("Enter symptoms (comma separated): ")
predicted_disease, predicted_remedies = predict_disease(input_str)
print(f"Predicted disease: {predicted_disease}")
print(f"Remedies: {', '.join(predicted_remedies)}")
