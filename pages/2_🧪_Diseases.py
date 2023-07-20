import streamlit as st
import os

st.title("Learn About Diseases")
def get_diseases():
    diseases = []
    for file in os.listdir("diseases"):
        if file.endswith(".md"):
            disease_name = file[:-3]
            diseases.append(disease_name)
    return diseases

def show_disease(disease_name):
    with open(f"diseases/{disease_name}.md", "r") as f:
        content = f.read()
    st.markdown(content)

diseases = get_diseases()

for disease in diseases:
    but1 = st.button(disease)
    if but1:
        show_disease(disease)
