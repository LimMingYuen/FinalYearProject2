import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("Y1S3.pkl","rb")
mul = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(UALE1083,UCCD2103,UALF1003,UBMM1011,Semester2_GPA,Semester2_CGPA):
   
   
    pred = np.array([UALE1083,UCCD2103,UALF1003,UBMM1011,Semester2_GPA,Semester2_CGPA])
    pred =pred.astype(np.float64)
    prediction = mul.predict([pred])
   
    print(prediction)
    return prediction



def app():
    st.title("Application for prediction of student performance")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction of Cumulative Grade Point Average Year 1 Semester 3 </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    UALE1083 = st.text_input("UALE1083","Type Here")
    UCCD2103 = st.text_input("UCCD2103","Type Here")
    UALF1003   = st.text_input("UALF1003","Type Here")
    UBMM1011   = st.text_input("UBMM1011","Type Here")
    Semester2_GPA     = st.text_input("Semester2_GPA","Type Here")
    Semester2_CGPA    = st.text_input("Semester2_CGPA","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(UALE1083,UCCD2103,UALF1003,UBMM1011,Semester2_GPA,Semester2_CGPA)
    st.success('The output is {}'.format(result))
    



