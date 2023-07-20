### the following code was a legacy code, back when tabs existed.

```py
## Predictions Tab
with tab2:
    #model part
    # Initialize the Random Forest Classifier
    classifier = RandomForestClassifier()
    st.markdown("## :green[Go-Cattle's ]:orange[ Disease Analyzer]")
    model = joblib.load('model.pkl')
    selected_items = []
    ## Select symtoms part
    st.markdown('### :green[**Select**] :red[**Symptoms:**]')
    pred_symptoms=st.multiselect(label=" ", options=symptoms2)
    pred_symptoms.extend(selected_items)
    st.markdown(f"<span style='color: #1fd655; font-weight: 600; font-size: 19px;'>Selected Symtomps are: </span><span style='color: yellow; font-weight: 500; font-size: 18px;' >{', '.join(pred_symptoms)}</span>",unsafe_allow_html=True)
    
    pred_df = pd.DataFrame(0,index=[0],columns=symptoms2)
    pred_df[pred_symptoms]=1
    # st.table(pred_df)
    result = model.predict(pred_df)
    st.subheader(f"Most probable Disease: :red[{result[0]}]")
    top_five = model.predict_proba(pred_df)
    # Get the classes from the random forest model
    classes = model.classes_
    # Get the indices of the top five classes based on probability
    top_class_indices = np.argsort(top_five, axis=1)[:, -5:]
    # Get the top five classes and their probabilities
    top_classes = classes[top_class_indices][:, ::-1]
    top_probabilities = np.take_along_axis(top_five, top_class_indices, axis=1)[:, ::-1]

    


    # disaplying the Top diseses part
    data = []
    for i, row in enumerate(top_classes):
        input_row = []
        for j, cls in enumerate(row):
            probability = top_probabilities[i][j]
            input_row.append((cls, probability))
        data.append(input_row)

    n_dis = 3
    column_names = [f'Top {i+1} Class' for i in range(5)] + [f'Top {i+1} Probability' for i in range(5)]
    # st.subheader(f"List of most probable Deseases ")
    
    df3 = pd.DataFrame(data[0],columns = ['Disease','Probability(%)'])
    df3['Probability(%)'] = df3['Probability(%)']*100
    df3.index = range(1, len(df3) + 1)

    col1,col2 = st.columns([3,1])

    with col1:
        st.text("\n")
        st.markdown(f"<span style='color: #; font-weight: bold; font-size: 25px;'>Most Probable Diseases</span>",unsafe_allow_html=True)
    with col2:
        st.text("\n")
        n_dis = st.selectbox(" ",(3,5))

    st.dataframe(df3.head(n_dis),1000)
    # st.dataframe(st.dataframe(df3.style.highlight_max(axis=0)))
    
with tab3:
    st.subheader(f"Most probable Disease: :red[{result[0]}] :green[(Fetched From the Predictions Tab)]")
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
```

this code was used to populate the sidebar with symptoms:

```py
        highlighted_elements = highlight_list_elements(symptoms)
        # for symptom in symptoms:
        #     st.markdown(f"<span style='color: blue; font-weight: bold; font-size: 15px;'>{symptom}</span>",unsafe_allow_html=True)
        selected_items = []
        for item in symptoms:
            checkbox = st.checkbox(item)
            if checkbox:
                selected_items.append(item)

        st.markdown(highlighted_elements, unsafe_allow_html=True)
```
this code was used to display the top 10 diseases:

```py
df = pd.read_csv('dataset/augean.csv') # read the dataset
df_s  = df.drop(columns=['Disease']) # dataset without the diseases name
column_sums = df_s.sum() # Calculate the sum of each column
del df_s #drop no-diseases
top_columns = column_sums.nlargest(10).index.tolist() # Select the top ten columns with the highest sums

    col_1,col_2  = st.columns(2)

    with col_1:
        for item in top_columns[:5]:
            st.markdown(f"<span style='color: blue; font-weight: bold;'>{item}</span>", unsafe_allow_html=True)
    with col_2:
        
        for item in top_columns[5:]:
            st.markdown(f"<span style='color: blue; font-weight: bold;'>{item}</span>", unsafe_allow_html=True)


    symptoms = df.columns
    symptoms2 = symptoms[1:]
    symptoms = sorted(symptoms[1:])

    del df

```