import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np




df = pd.read_csv('dataset/augean.csv')
df_s  = df.drop(columns=['Disease'])
# Calculate the sum of each column
column_sums = df_s.sum()
del df_s
# Select the top ten columns with the highest sums
top_columns = column_sums.nlargest(10).index.tolist()

symptoms = df.columns
symptoms2 = symptoms[1:]
symptoms = sorted(symptoms[1:])

def highlight_list_elements(lst):
        highlighted_list = ""
        for item,n in enumerate(lst):
            highlighted_list += f'<span style="background-color: white;">{item+1}). {n} </span>\n'
        return highlighted_list
    
with st.sidebar:
    st.subheader(":green[List of Symptoms]")
    st.markdown("##### **Select from the Symptoms below**")
    st.markdown(f'<hr>', unsafe_allow_html=True)
    selected_items = []
    highlighted_elements = highlight_list_elements(symptoms)
        # for symptom in symptoms:
        #     st.markdown(f"<span style='color: blue; font-weight: bold; font-size: 15px;'>{symptom}</span>",unsafe_allow_html=True)
    for item in symptoms:
        checkbox = st.checkbox(item)
        if checkbox:
            selected_items.append(item)
        # st.markdown(highlighted_elements, unsafe_allow_html=True)
        
#model part
# Initialize the Random Forest Classifier
classifier = RandomForestClassifier()
st.markdown("## :green[Go-Cattle's ]:orange[ Disease Analyzer]")
model = joblib.load('model.pkl')
## Select symtoms part
st.markdown('### :green[**Select**] :red[**Symptoms:**]')
pred_symptoms=st.multiselect(label=" ", options=symptoms2)
pred_symptoms.extend(selected_items)
pred_df = pd.DataFrame(0,index=[0],columns=symptoms2)
pred_df[pred_symptoms]=1
# st.table(pred_df)
result = model.predict(pred_df)

if pred_symptoms == []:
    st.markdown(f"<span style='color: #1fd655; font-weight: 600; font-size: 19px;'>No Symptoms Selected</span><span style='color: yellow; font-weight: 500; font-size: 18px;' >{', '.join(pred_symptoms)}</span>",unsafe_allow_html=True)
    st.subheader(":red[Please Select a Symptom to begin with]")
else:
    st.markdown(f"<span style='color: #1fd655; font-weight: 600; font-size: 19px;'>Selected Symtomps are: </span><span style='color: yellow; font-weight: 500; font-size: 18px;' >{', '.join(pred_symptoms)}</span>",unsafe_allow_html=True)
    st.subheader(f":orange[Most Probable Disease:] :red[{result[0]}]")
    try :
        # Read the markdown file as plain text
        file_path = f"diseases/{result[0]}.md"
        # st.markdown(file_path)
        with open(file_path, "r") as file:
            markdown_text = file.read()

    # Display the markdown content
        st.write(markdown_text)
    except FileNotFoundError as FE:
        
        st.markdown("Information on the disease not avalable at the moment")
    top_five = model.predict_proba(pred_df)
    # Get the classes from the random forest model
    classes = model.classes_
    # Get the indices of the top five classes based on probability
    top_class_indices = np.argsort(top_five, axis=1)[:, -5:]
    # Get the top five classes and their probabilities
    top_classes = classes[top_class_indices][:, ::-1]
    top_probabilities = np.take_along_axis(top_five, top_class_indices, axis=1)[:, ::-1]



    # st.subheader(f"List of most probable Deseases ")

    # displaying the Top diseses part
    data = []
    for i, row in enumerate(top_classes):
        input_row = []
        for j, cls in enumerate(row):
            probability = top_probabilities[i][j]
            input_row.append((cls, probability))
        data.append(input_row)

    n_dis = 3
    column_names = [f'Top {i+1} Class' for i in range(5)] + [f'Top {i+1} Probability' for i in range(5)]


    df3 = pd.DataFrame(data[0], columns = ['Disease','Probability(%)'])
    df3['Probability(%)'] = df3['Probability(%)']*100
    df3.index = range(1, len(df3) + 1)

    col1,col2 = st.columns([3,1])

    with col1:
        st.text("\n")
        # st.markdown(f"<span style='color: #; font-weight: bold; font-size: 25px;'>Most Probable Diseases</span>",unsafe_allow_html=True)
        st.markdown("#### :violet[Other Probable Diseases]")
    with col2:
        n_dis = st.selectbox(" ",(3,5))

    st.dataframe(df3.head(n_dis),1000)
    # st.dataframe(st.dataframe(df3.style.highlight_max(axis=0)))
