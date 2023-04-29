#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 11:38:32 2023

@author: ajaykumarbhardwaj
"""
import numpy as np
import streamlit as st
import pickle
st.write("""
    <style>
        .special {
            color: pink;
        }
    </style>
""", unsafe_allow_html=True)
# Load the pickled model
with open('xgb.pkl', 'rb') as file:
    xgb = pickle.load(file)
#st.title('Cancer Prediction 🎗️')
st.write("""
    <h1 style='text-align: center;'>Cancer Prediction 🎗️</h1>
    """, unsafe_allow_html=True)
st.write("""
    <p class="special" style='text-align: center;'>Here is a brief description about the tumor features/parameters:</p>
    """, unsafe_allow_html=True)
st.write("""
    <p>Radius_mean: The mean distance from the center of the tumor to points on the perimeter.

Texture_mean: The mean value for texture in the image of the tumor.

Perimeter_mean: The mean perimeter of the tumor.

Area_mean: The mean area of the tumor.

Smoothness_mean: The mean value for smoothness in the tumor.

Compactness_mean: The mean value for compactness in the tumor.

Concavity_mean: The mean severity of concave portions of the tumor.

Concave_points_mean: The mean number of concave portions of the tumor.

Symmetry_mean: A measure of how symmetric the cells in the tumor are.

Fractal_dimension_mean: A measure of the complexity of the tumor's structure at a macroscopic level.

Radius_se: The standard error of the mean of distances from the center of the tumor to points on the perimeter.

Texture_se: The standard error of gray-scale values in the image of the tumor.

Perimeter_se: The standard error of the perimeter of the tumor.

Area_se: The standard error of the area of the tumor.

Smoothness_se: The standard error of the local variation in the radius lengths.

Compactness_se: The standard error of the ratio of the perimeter to the area of the tumor.

Concavity_se: The standard error of the severity of concave portions of the tumor.

Concave_points_se: The standard error of the number of concave portions of the tumor.

Symmetry_se: The standard error of the symmetry of the cells in the tumor.

Fractal_dimension_se: The standard error of the complexity of the tumor's structure.

Radius_worst: The worst (largest) distance from the center to the perimeter among all points in the tumor.

Texture_worst: The worst (most abnormal) value for texture in the image of the tumor.

Perimeter_worst: The worst (largest) perimeter of the tumor.

Area_worst: The worst (largest) area of the tumor.

Smoothness_worst: The worst (most abnormal) value for smoothness in the tumor.

Compactness_worst: The worst (most abnormal) value for compactness in the tumor.

Concavity_worst: The worst (most severe) value for concavity in the tumor.

Concave_points_worst: The worst (largest) number of concave portions of the tumor.

Symmetry_worst: The worst (most abnormal) value for symmetry in the tumor.

Fractal_dimension_worst: The worst (most complex) value for the fractal dimension of the tumor's structure.</p>
    """, unsafe_allow_html=True)
st.write("""
    <p style='text-align: center;'>These attributes are all calculated based on measurements taken from images of the tumor. They can be used to create a comprehensive picture of the tumor's characteristics and help in diagnosis and treatment planning.</p>
    """, unsafe_allow_html=True)
st.write("""
    <p class="special">Enter tumor features</p>
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

