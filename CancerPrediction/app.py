#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 11:38:32 2023

@author: ajaykumarbhardwaj
"""
import numpy as np
import streamlit as st
import pickle

# Load the pickled model
with open('xgb.pkl', 'rb') as file:
    xgb = pickle.load(file)
#st.title('Cancer Prediction 🎗️')
st.write("""
    <h1 style='text-align: center;'>Cancer Prediction 🎗️</h1>
    """, unsafe_allow_html=True)
st.write("""
    <p style='text-align: center;'>Enter tumor features</p>
    """, unsafe_allow_html=True)
st.write("""
<style>
    .big-font {
        font-size:50px !important;
        color: red;
    }
    .big-fonts {
        font-size:50px !important;
        color: green;
    }
</style>
""", unsafe_allow_html=True)

# Define the Streamlit app
def main():
    # Define the input field(s) for the user
    rm=st.number_input("Enter the radius mean")
    tm=st.number_input("Enter the texture mean")
    pm=st.number_input("Enter the perimeter mean",step=0.000001)
    am=st.number_input("Enter the area mean",step=0.000001)
    sm=st.number_input("Enter the smoothness mean",step=0.000001)
    com_m=st.number_input("Enter the compactness mean",step=0.000001)
    con_m=st.number_input("Enter the concavity mean",step=0.000001)
    cp=st.number_input("Enter the concave points",step=0.000001)
    symmetry_mean=st.number_input("Enter the symmetry_mean",step=0.000001)
    fractal_dimension_mean=st.number_input("Enter the fractal_dimension_mean",step=0.000001)
    radius_se=st.number_input("Enter the radius_se",step=0.000001)
    texture_se=st.number_input("Enter the texture_se",step=0.000001)
    perimeter_se=st.number_input("Enter the perimeter_se ",step=0.000001)
    area_se=st.number_input("Enter the area_se",step=0.000001)
    smoothness_se=st.number_input("Enter the smoothness_se",step=0.000001)
    compactness_se=st.number_input("Enter the compactness_se",step=0.000001)
    concavity_se=st.number_input("Enter the concavity_se",step=0.000001)
    concave_points_se=st.number_input("Enter the concave_points_se",step=0.000001)
    symmetry_se=st.number_input("Enter the symmetry_se",step=0.000001)
    fractal_dimension_se=st.number_input("Enter the fractal_dimension_se",step=0.000001)
    radius_worst=st.number_input("Enter the radius_worst",step=0.000001)
    texture_worst=st.number_input("Enter the texture_worst",step=0.000001)
    perimeter_worst=st.number_input("Enter the perimeter_worst",step=0.000001)
    area_worst=st.number_input("Enter the area_worst",step=0.000001)
    smoothness_worst=st.number_input("Enter the smoothness_worst",step=0.000001)
    compactness_worst=st.number_input("Enter the compactness_worst",step=0.000001)
    concavity_worst=st.number_input("Enter the concavity_worst",step=0.000001)
    concave_points_worst=st.number_input("Enter the concave_points_worst",step=0.000001)
    symmetry_worst=st.number_input("Enter the symmetry_worst",step=0.000001)
    fractal_dimension_worst=st.number_input("Enter the fractal_dimension_worst",step=0.000001)
   
    # Process the user input and make a prediction using the loaded model
    if st.button("Predict"):
        input_list = [rm,tm,pm,am,sm,com_m,con_m,cp,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,
                      smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,
                      texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,
                      symmetry_worst,fractal_dimension_worst]
        input_list = np.array(input_list).reshape(1, -1)
        #encoded_list = [item.encode('utf-8') for item in data_arr]
        prediction = xgb.predict(input_list)[0]
        # Display the prediction to the user
        if prediction == 1:
            st.write('<span class="big-font">The tumor is malignant</span>', unsafe_allow_html=True)

        else:
            st.write('<span class="big-fonts">The tumor is benign</span>', unsafe_allow_html=True)
            

# Run the app
if __name__ == "__main__":
    main()

