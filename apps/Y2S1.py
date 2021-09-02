import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("Y2S1.pkl","rb")
mul = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(MPU3113,MPU32143,UCCD1013,UCCD1024,UCCD1133,UCCM1363,Semester3_GPA,Semester3_CGPA):
   
   
    pred = np.array([MPU3113,MPU32143,UCCD1013,UCCD1024,UCCD1133,UCCM1363,Semester3_GPA,Semester3_CGPA])
    pred =pred.astype(np.float64)
    prediction = mul.predict([pred])
 
    print(prediction)
    return prediction



def app():
    st.title("Application for prediction of student performance")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction of Cumulative Grade Point Average Year 2 Semester 1  </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    MPU3113 = st.text_input("MPU3113","Type Here")
    MPU32143 = st.text_input("MPU32143","Type Here")
    UCCD1013   = st.text_input("UCCD1013","Type Here")
    UCCD1024   = st.text_input("UCCD1024","Type Here")
    UCCD1133   = st.text_input("UCCD1133","Type Here")
    UCCM1363   = st.text_input("UCCM1363","Type Here")
    Semester3_GPA     = st.text_input("Semester3_GPA","Type Here")
    Semester3_CGPA    = st.text_input("Semester3_CGPA","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(MPU3113,MPU32143,UCCD1013,UCCD1024,UCCD1133,UCCM1363,Semester3_GPA,Semester3_CGPA)
    st.success('The output is {}'.format(result))
    



