import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("Y2S2.pkl","rb")
mul = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(MPU3123,UCCD2003,UCCD2044,UCCD2203,UCCD2223,UCCN2243,Semester1_GPA,Semester1_CGPA):
   
    pred = np.array([MPU3123,UCCD2003,UCCD2044,UCCD2203,UCCD2223,UCCN2243,Semester1_GPA,Semester1_CGPA])
    pred =pred.astype(np.float64)
    prediction = mul.predict([pred])
  
    print(prediction)
    return prediction



def app():
    st.title("Application for prediction of student performance")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction of Cumulative Grade Point Average Year 2 Semester 2 </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    MPU3123 = st.text_input("MPU3123","Type Here")
    UCCD2003 = st.text_input("UCCD2003","Type Here")
    UCCD2044   = st.text_input("UCCD2044","Type Here")
    UCCD2203   = st.text_input("UCCD2203","Type Here")
    UCCD2223   = st.text_input("UCCD2223","Type Here")
    UCCN2243   = st.text_input("UCCN2243","Type Here")
    Semester1_GPA     = st.text_input("Semester1_GPA","Type Here")
    Semester1_CGPA    = st.text_input("Semester1_CGPA","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(MPU3123,UCCD2003,UCCD2044,UCCD2203,UCCD2223,UCCN2243,Semester1_GPA,Semester1_CGPA)
    st.success('The output is {}'.format(result))
    


