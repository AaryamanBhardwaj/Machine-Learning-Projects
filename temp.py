# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
data=pd.read_csv('/Users/ajaykumarbhardwaj/Downloads/Suicide_Detection/Suicide_Detection.csv')
data = data.drop(data.columns[0], axis=1)
data['class']=data['class'].replace({'suicide': 'depressed', 'non-suicide': 'not depressed'})
data=data.iloc[:10000,:]
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
vectorizer=TfidfVectorizer()
from sklearn.model_selection import train_test_split
training ,test = train_test_split(data, test_size=0.3, random_state=42)
X_train=training['text'].values
X_train_final=vectorizer.fit(X_train)
with open('/Users/ajaykumarbhardwaj/Downloads/depression_detection_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Create a main function
def main():
    # Display a header
    st.header('Depression detection using social media posts')
    

    # Get input data from the user
    input_data = st.text_input('Enter input data')
    #vectorizer.fit(input_data)
    nt=vectorizer.transform([input_data])
   
        # Make a prediction using the model
    prediction = loaded_model.predict(nt)[0]
    
    st.write(f'Prediction: {prediction}')

# Run the main function
if __name__ == '__main__':
    main()


