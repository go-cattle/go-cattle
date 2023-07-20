
## model training part ####
#import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import joblib

# Load the formatted data from the CSV file
data = pd.read_csv('dataset/augean.csv')

# Separate the input features (X) and target variable (y)
X = data.drop('Disease', axis=1)
y = data['Disease']

# Initialize the Random Forest Classifier
classifier = RandomForestClassifier()

# Perform cross-validation
cv_scores = cross_val_score(classifier, X, y, cv=2)

# Fit the model on the entire dataset
classifier.fit(X, y)

# Save the trained model to a file
joblib.dump(classifier, 'model.pkl')

print("Cross-Validation Scores:", cv_scores)
print("Mean Accuracy:", cv_scores.mean())
print("Model saved to 'model.pkl' successfully.")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the trained model from the file
model = joblib.load('model.pkl')

y_pred2 = model.predict(X_train)
accuracy = accuracy_score(y_train, y_pred2)
print(f"Accuracy: {accuracy}")

# Predict the disease for the test data
y_pred = model.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

