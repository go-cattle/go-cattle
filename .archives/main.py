import joblib
import streamlit as st

# Load the trained model from the file
model = joblib.load('model.pkl')

def predict_disease(data):
  """Predicts the disease for the given data."""
  y_pred = model.predict(data)
  return y_pred

# Display the input data
st.title("Disease Prediction App")
st.write("Enter the following data:")
data = st.multiselect("Features", X_test.columns)

# Predict the disease
y_pred = predict_disease(data)

# Display the predicted disease
st.write("The predicted disease is:", y_pred)

# Display the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
st.write("The accuracy of the model is:", accuracy)
