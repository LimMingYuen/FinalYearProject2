import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("Y1S2.pkl","rb")
mul = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(UCCD1004,UCCD1203,UCCM2233,UCCN1004,MPU3301,Semester1_GPA,Semester1_CGPA):
   
    pred = np.array([UCCD1004,UCCD1203,UCCM2233,UCCN1004,MPU3301,Semester1_GPA,Semester1_CGPA])
    pred =pred.astype(np.float64)
    prediction = mul.predict([pred])
    print(prediction)
    return prediction
    
   


def app():
    st.title("Application for prediction of student performance")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction of Cumulative Grade Point Average Year 1 Semester 2 </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    UCCD1004 = st.text_input("UCCD1004","Type Here")
    UCCD1203 = st.text_input("UCCD1203","Type Here")
    UCCM2233   = st.text_input("UCCM2233","Type Here")
    UCCN1004   = st.text_input("UCCN1004","Type Here")
    MPU3301   = st.text_input("MPU3301","Type Here")
    st.text("Please insert the same value for Semester1_GPA and Semester1_CGPA")
    Semester1_GPA     = st.text_input("Semester1_GPA","Type Here")
    Semester1_CGPA    = st.text_input("Semester1_CGPA","Type Here")
   
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(UCCD1004,UCCD1203,UCCM2233,UCCN1004,MPU3301,Semester1_GPA,Semester1_CGPA)
    st.success('The output is {}'.format(result))
    



