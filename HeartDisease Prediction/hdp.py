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
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
#st.title('Heart Disease Prediction ')
st.write("""
    <h1 style='text-align: center;'>Heart Disease Prediction </h1>
    """, unsafe_allow_html=True)

st.write("""
    <p class="special">Enter features</p>
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
    rm=st.number_input("Enter Body Mass Index (BMI)")
    tm=st.number_input("Smoking(1 for yes ,0 for no)")
    pm=st.number_input("Drinking(1 for yes ,0 for no)")
    am=st.number_input("Stroke(1 for yes ,0 for no)")
    sm=st.number_input("Enter physical activity (in days) for past 30 days")
    com_m=st.number_input("Thinking about your mental health, for how many days during the past 30 days was your mental health not good?")
    con_m=st.number_input("Do you have serious difficulty walking or climbing stairs?(1 for yes ,0 for no)")
    cp=st.number_input("Are you male or female?(1 for male ,0 for female)")
    symmetry_mean=st.number_input("Age category(7. 55-59,12. 80 or older,9.  65-69,11.  75-79, 4. 40-44,10. 70-74, 8. 60-64,6. 50-54,5. 45-49, 0. 18-24,3. 35-39, 2. 30-34, 1. 25-29)")
    fractal_dimension_mean=st.number_input("Race(1.White 2.Black 3.Asian 4.American Indian or Alaskan Native 5.Other 6.Hispanic)")
    radius_se=st.number_input("(Ever told) (you had) diabetes?(1 for yes ,0 for no)")
    texture_se=st.number_input("Are you physically active?(1 for yes ,0 for no)")
    perimeter_se=st.number_input("How is your general health?(on a scale of 1-5)")
    area_se=st.number_input("On average, how many hours of sleep do you get in a 24-hour period?")
    smoothness_se=st.number_input("(Ever told) (you had) asthma?(1 for yes ,0 for no)")
    compactness_se=st.number_input("Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?(1 for yes ,0 for no)")
    concavity_se=st.number_input("(Ever told) (you had) skin cancer?(1 for yes ,0 for no)")
    
    # Process the user input and make a prediction using the loaded model
    if st.button("Predict"):
        input_list = [rm,tm,pm,am,sm,com_m,con_m,cp,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,
                      smoothness_se,compactness_se,concavity_se]
        input_list = np.array(input_list).reshape(1, -1)
        #encoded_list = [item.encode('utf-8') for item in data_arr]
        prediction = model.predict(input_list)[0]
        # Display the prediction to the user
        if prediction == 1:
            st.write('<span class="big-font">There is a chance of heart disease</span>', unsafe_allow_html=True)

        else:
            st.write('<span class="big-fonts">There is no chance of heart disease</span>', unsafe_allow_html=True)
            

# Run the app
if __name__ == "__main__":
    main()