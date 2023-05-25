import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer

# Load the data from the .txt file
with open('data.txt', 'r') as file:
    lines = file.readlines()

diseases = []
symptoms_list = []

# Process each line in the file
for line in lines:
    line = line.strip()  # Remove leading/trailing whitespaces
    if line.startswith('Disease:'):
        disease = line.replace('Disease:', '').strip()
        diseases.append(disease)
    elif line.startswith('Symptoms:'):
        symptoms = line.replace('Symptoms:', '').strip().split(',')
        symptoms_list.append(symptoms)

# Create a DataFrame from the processed data
data = pd.DataFrame({'Disease': diseases, 'Symptoms': symptoms_list})

# Perform one-hot encoding on the symptoms
mlb = MultiLabelBinarizer()
symptoms_encoded = mlb.fit_transform(data['Symptoms'])
symptoms_df = pd.DataFrame(symptoms_encoded, columns=mlb.classes_)

# Concatenate the one-hot encoded symptoms with the original DataFrame
data_encoded = pd.concat([data['Disease'], symptoms_df], axis=1)

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(symptoms_df, data['Disease'], test_size=0.25)

# Train the SVM model on the training set
svm = SVC()
svm.fit(X_train, y_train)

# Evaluate the SVM model on the test set
accuracy = svm.score(X_test, y_test)
print(accuracy)

# Use the SVM model to make predictions
new_symptoms = ['fever', 'anemia', 'jaundice']
new_symptoms_encoded = mlb.transform([new_symptoms])
prediction = svm.predict(new_symptoms_encoded)
print(prediction)
