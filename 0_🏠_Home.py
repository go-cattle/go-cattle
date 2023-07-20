# Import required libraries
import streamlit as st #to run the webpage ofcourse
import pandas as pd #to read the dataset
from PIL import Image #to render the gcb.jpg image 
import datetime
from streamlit_option_menu import option_menu

#Congifuring the Streamlit Page (the same thing is done in the /.streamlit/config.toml)

st.set_page_config(
    page_title="Go-Cattle // Cattle Healthcare",
    page_icon="🐄",
    layout="wide",
    #menu_items={'Get Help': 'https://www.extremelycoolapp.com/help','Report a bug': "https://www.extremelycoolapp.com/bug",'About': "# This is a header. This is an *extremely* cool app!"}
)
#logo=Image.open('logo.png')
#st.image(logo,width=300)
## Defining tabs
tab1,tab2,tab3,tab4,tab5 = st.tabs(["Home","Details","Credits","Feedback", "Legal"])

# h - i just added this h and was wondering why error

## Linking the Style.css (just in case)
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

## tab 1, home
with tab1:
    st.title(":green[Go-Cattle]")
    st.markdown(f"<h3><i><ins>A Cattle Healthcare Platform</ins></i></h3>", unsafe_allow_html=True)
    image=Image.open('gcb.jpg')
    st.image(image)
    st.markdown('### :red[**What is Go Cattle?**]')
    st.markdown("Go Cattle is a :green[**Cattle Healthcare Platform**]. India is the Home to about 17% of the World's Cows and For Every 1 Registered Vet in India, There are about 50,000 cows. Due To These Reasons, About 65% of The Cows Cannot Get Proper Healthcare and Treatments. It is Very Important to increase awareness about this topic because This Leads to Thousands if Not Hundreds of Thousands of Cattle Dying Every Year.")
    st.markdown("Go Cattle Provides a Variety of Resources for The Welfare of Cattles. One of The Main Features is an advanced web application designed to **analyze** :red[diseases] in cattle based on the :yellow[**symptoms**] provided. With its cutting-edge ML-model analyzer, Go Cattle ensures accurate and efficient diagnosis, empowering cattle owners and veterinarians to make informed decisions about their livestock's health.")
    st.markdown("Our ML-model boasts an outstanding :green[**accuracy rate of 95%+**], surpassing the required medical standards" f"<sup>#</sup>" " Developed using a vast dataset of *20,499 parameters* sourced from reliable and up-to-date information gathered through web crawling & web scraping, Go Cattle provides a robust foundation for precise disease identification.", unsafe_allow_html=True)
    st.markdown("Equipped with an extensive range of 123 unique symptoms and a comprehensive list of 163 unique diseases, Go Cattle covers a wide spectrum of ailments that can affect cattle. By inputting the observed symptoms, the system swiftly processes the information and generates a reliable diagnosis, enabling prompt action to be taken. :violet[ *The Dataset has been gone through Vigorous Changes Recently and There's A High Possibility that our team might have messed up something in the Process (as of 10th July 2023)*]")
    
    
    with st.sidebar:
       ## fil_val="This value was used to fill the sidebar" #they wont let me just yk, use the sidebar without anything
       st.empty() #okay, i discovered something better. LOL
          
with tab2:
    st.title(":red[//] :orange[**Details**]")
    #tdet,clog,manl=st.tabs(["Technical Details","Changelog","Medical Analysis"])
    
    selected2 = option_menu(None, [ "Technicalities", "Changelog", 'Medical Analysis'], 
    icons=['robot', 'clock-history', "activity" ], 
    menu_icon="cast", default_index=0, orientation="horizontal")
    
    
    if selected2 == "Technicalities":
        st.markdown("## Technical Details")
        st.markdown("""
                #### :green[ML Model Disease Analyzer]
                The Disease Analyzer works on Providing the Symptom
                """)
        st.markdown("Our ML-model boasts an outstanding :green[**accuracy rate of 95%+**], surpassing the required medical standards" f"<sup>#</sup>" " Developed using a vast dataset of *20,499 parameters* sourced from reliable and up-to-date information gathered through web crawling & web scraping, Go Cattle provides a robust foundation for precise disease identification.", unsafe_allow_html=True)
        st.markdown("Equipped with an extensive range of 123 unique symptoms and a comprehensive list of 163 unique diseases, Go Cattle covers a wide spectrum of ailments that can affect cattle. By inputting the observed symptoms, the system swiftly processes the information and generates a reliable diagnosis, enabling prompt action to be taken. :violet[ *The Dataset has been gone through Vigorous Changes Recently and There's A High Possibility that our team might have messed up something in the Process (as of 10th July 2023)*]")
        st.markdown("### :orange[Workings of The Model]")
        st.markdown("""
                    The first step is to load the data (cattle diseases and their symptoms) from a CSV file. The data is then split into two sets: a training set and a test set. The training set is used to train the model, and the test set is used to evaluate the model's accuracy.
Next, a random forest classifier is initialized. The random forest classifier is a type of machine learning algorithm that can be used for classification tasks. It works by creating a number of decision trees, and then making a prediction by taking a majority vote of the predictions from the decision trees.
The next step is to perform cross-validation. Cross-validation is a technique for evaluating the accuracy of a machine learning model. It works by splitting the data into a number of folds, and then training the model on a subset of the folds and evaluating the model on the remaining folds. This process is repeated multiple times, and the average accuracy across all folds is reported.
In this case, the cross-validation is performed using two folds. The mean accuracy of the model is 97.5%.
The next step is to fit the model on the entire training set. This means that the model will learn the relationships between the input features and the target variable.
Once the model is fitted, it can be saved to a file. This is done using the joblib library.
The next step is to load the trained model from the file. This is done using the joblib library as well.
The next step is to predict the disease for the training set. This is done by passing the training set to the model's predict() method.
The accuracy of the model is then evaluated by comparing the predicted values to the actual values. The accuracy in this case is 98.7%.
The final step is to predict the disease for the test set. This is done by passing the test set to the model's predict() method.
The accuracy of the model is then evaluated by comparing the predicted values to the actual values. The accuracy in this case is 97.5%.
Overall, the random forest classification model achieves an accuracy of 97.5% on the test set. This means that the model is able to correctly predict the disease for 97.5% of the test data.
                    """)
    elif selected2 == "Changelog":
        st.subheader("Changelog")
        st.markdown("""
                    ### 17th July:
- :green[Added a Streamlit Option Menu to Details tab that has the following Options which may change in the future:]
  - Changelogs
  - Technical Details
  - Medical Analysis
- :green[Content Update (Phase V2) continuously updating the contents and Improving the present content in terms of grammar.]

### 15th and 16th July:
- :orange[Fixed the Multi-page Navigation System by an Interesting Approach]
>> I moved the predicted disease information to the prediction tab so it doesn't need to fetch a variable from a different python file anymore.
- :green[Content Update - since the home page was empty as the tabs were redistributed to pages, added **credits** and details in place of those two lost tabs]
- :violet[Deprecated feedback and legal pages to tabs in the home page]

### 14th July: (THE :red[D-DAY])
- :red[Deleted 'Change Theme' Feature]
- :red[Deleted support.py (We Wont Import Functions from a different file)]
- :red[Removed The Top 10 Symptoms from Homepage]
- :red[Removed Unnecessary Texts]
- :red[Removed the Just-in-Case Style.css]
- :red[Cleared the Saved pyCache and now its **BROKE**]
- :red[Removed requirements :green[(added `requirements.txt` in its place)]]


### 13th July:
- :green[Made Multi-page Navigation System on Request. The UI became really easy because everything can be controlled using the sidebar. We can also Use Links like [Prediction](https://gocattle.site/Prediction) which lands us Directly on the Prediction Webpage.
This Introduces leftover Tab Spaces which can be used as Content. (The Styling will mostly remain the same as I believe that Farmers don't really care about Stylish Interfaces. The thing is about being simple and I am trying my best.)]
    >> However, The Multi-page stuff Introduced 2 Interesting Problems and I can't do anything because Python works that way. First of all, The Diseases page requests a variable from the Prediction page. The variable is named "result" and displays the most probable disease. To import the result variable from the Prediction page, I import it into my disease page but the disease page insists on running the whole code instead of just fetching the variable, It runs the complete program. That is stupid. Another Problem I've encountered is that Python cannot import files that have a special character in their name. Like the Prediction file is saved as ```1_🐮_Prediction.py```
And I just can't include Special Characters. I will figure a workaround soon.
- :orange[Reworked on the Diseases Buttons, They Only Display Diseases when Requested.]
- :orange[Initial Sidebar State now set to expand as Sidebar is the main form of navigation]

### 12th July:
- :green[Added Diseases Tab]
- :orange[Reworked on Buttons by Implementing Buttons]
- :green[Created Two Distinct Models on :blue[Augean] and :blue[Manhattan].]
  - :blue[Arjun] Model - Based on :blue[Augean], Provides Medical Grade Accuracy but is Overcomplicated and Contains Duplicate Data
  - :blue[Enigma] Model - Based on :blue[Manhattan], Focuses on Simplicity and doesn't provide Medical Grade Accuracy.
- :green[Made a Github Organization named **go-cattle** (https://github.com/go-cattle) and all the details about the go-cattle app with all technical details.]
  > Please Expect a Change every Fortnight and Not Any Sooner.
- :green[Organized 'Diseases' Tab and Added 'Learn About Predicted Disease']

### 11th July
- :green[Hosted on Hugging Face because [Owehost](https://owehost.com) will take time]
- :green[Made 2 Discreet Datasets]
  - :blue[Augean] - Over complicated with numerous duplicates but Great Accuracy
  - :blue[Manhattan] - Over Simplified for use by a simple man but No way of achieving medical grade Accuracy
- :green[Linked the domain (https://gocattle.site) and the subdomain (www.gocattle.site) to the hugging face space. The domains are technically a **masked redirect**, but they work so Idgaf]
- :orange[(Almost) Completed the Diseases Tab and Countered The Previous Glitches]

### 10th July
- :orange[Made the Website Colorful, By Adding Text Colors and Essence]
- :green[Added Legal sections]
- :orange[Simplified UI]
- :green[Content Addition including Introduction]

                    """)
    else:
        st.write("You selected Medical Analysis")  
        
with tab3:
    st.title("Credits")
    st.markdown("### :red[//] :green[Founded by] [:orange[Sarthak] :blue[Sidhant]](https://sarthaksidhant.me/)")
    st.markdown("""
As an Indian, I've had early experiences with cows in my village.
I've seen firsthand how important it is to keep cows healthy, and I've also seen the challenges
that farmers face in providing quality healthcare to their animals.\n
I also got the inspiration for this idea from Sarvagya's [Nandini](https://drive.google.com/file/d/1WZvZB5TyjJgR_XD3yzxT0hc6nUFMFbfd/view?usp=sharing) project.
I was really impressed by the idea and wanted to make something similar but with a more modern approach.
Initially, I just wanted to see how fast it would take me to collect the data and make a model,
but I ended up making a full-fledged healthcare platform.\n
I really hope that this project helps
the farmers and the cattle in some way or another.
Thanks to all the people that helped along the way and contributed towards this project.
I really hope that machine learning and artificial intelligence contribute toward
society and nature in a beneficial way like this. (I'm looking at you, Cambridge Analytica)\n
I hope to make projects like [:green[Go-Cattle]](#) and [:orange[Rellekk-Z]](https://rellekk-z.github.io/Rellekk-Z)
and [:orange[Decodificate]](https://decodificate.tech) in the future that aim to seamlessly blend in with the cause of social benefit,
and I hope that you'll be there to support me. Thank you for using Go Cattle.""")
    st.subheader(":red[//] :orange[Contributors]")
    st.markdown("##### [:blue[Abhijith KS]](https://www.fiverr.com/abhijith_k_s) - Helped in Developing the Model and the Web-App")
    st.markdown("##### [:blue[AshTired11s]](https://www.kaggle.com/ashtired11/) - Dataset Engineer, Helped in Devloping the Vast Dataset")
    st.markdown("##### [:orange[Yasharth Gautam]](github.com/yasharth1) - Team Member, Helped with Suggestions and '👍' ")
    st.markdown("##### [:orange[Aayushman Utkrisht]](https://www.google.com/search?q=aayushman+utkrisht&client=opera-gx&hs=yPD&sxsrf=AB5stBgq-WWcuh2JWtN7a7tjge0BaZfhCA%3A1689542431457&ei=H1-0ZKrEG9So4-EPpeS9yA4&ved=0ahUKEwjqz9aDlJSAAxVU1DgGHSVyD-kQ4dUDCA4&uact=5&oq=aayushman+utkrisht&gs_lp=Egxnd3Mtd2l6LXNlcnAiEmFheXVzaG1hbiB1dGtyaXNodDIHEAAYgAQYCjIHEAAYgAQYCjIJEAAYigUYChhDMgYQABgeGAoyCBAAGIoFGIYDMggQABiKBRiGAzIIEAAYigUYhgMyCBAAGIoFGIYDMggQABiKBRiGA0jIA1AAWABwAHgBkAEAmAHaAaAB2gGqAQMyLTG4AQPIAQD4AQHiAwQYACBBiAYB&sclient=gws-wiz-serp) - Team Member, Helped with Suggestions and UI ")
    st.markdown("##### [:green[Layered, OweHost]](Owehost.com) - Sponsors the Hosting of the Go Cattle Web-App")
    st.markdown("##### [:green[Sidhant Hyperspace]](sarthaksidhant.me/sidhant-hyperspace) - Umbrella Organisation for Go Cattle")

with tab4:
    
    def save_feedback(name,email,feedback):
        # Generate a unique filename using the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"./feedbacks/feedback_{name}_{email}_{timestamp}.txt"

        # Save the feedback to a file
        with open(filename, 'w') as file:
            file.write(f'name : {name}\nemail : {email}\nfeedback : {feedback}')

        return filename

    st.subheader("Feedback Portal")
    colFB1,colFB2 = st.columns([1,3])
    with colFB1:
        name  = st.text_input("Enter your name")
        email = st.text_input("Enter your email id")
    with colFB2:
        feedback = st.text_area("Enter your feedback here")
    

    if st.button("Submit"):
        if (feedback and name and email):
            # Save feedback as a file
            filename = save_feedback(name,email,feedback)
            st.success(f"Thank you for your feedback! Your feedback has been saved.")
        else:
            st.warning("Please enter your details before submitting.")

with tab5: #legal section (dangerous)
    st.title("Legal")
    st.markdown("### :green[**Terms of Service**]")
    st.markdown("""Disclaimer: 

The advice or results generated by the Go Cattle app are derived from an artificial intelligence machine learning model. While efforts are made to ensure accuracy levels of 95% or higher, it is crucial to note that these outcomes may be subject to inaccuracies and should not be regarded as medical information. Therefore, the advice provided by the app should never be solely relied upon without seeking the guidance of a qualified veterinarian. 

It is important to understand that:

1. The Go Cattle app is not a substitute for professional veterinary care.
2. The results obtained from the app should not be used as a means to diagnose or treat any medical condition.
3. If you have concerns about the health of your cattle, it is imperative that you consult a veterinarian without delay.

By utilizing the Go Cattle app, you expressly acknowledge and agree that:

1. Go Cattle shall not be held liable or accountable for any mishaps, damages, injuries, or losses arising from the use of the advice or results provided by the app.
2. The app's advice and results are not a replacement for personalized veterinary care and should be considered as supplementary information only.

We hope this disclaimer serves to clarify the limitations of the Go Cattle app and the need for professional veterinary consultation. Your understanding and compliance with these terms are greatly appreciated.

Thank you for choosing and using Go Cattle!""")