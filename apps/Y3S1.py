import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("Y3S1.pkl","rb")
mul = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(MPU34012,UCCD2502,UCCD2513,UCCN1213,Semester3_GPA,Semester3_CGPA):
   
    pred = np.array([MPU34012,UCCD2502,UCCD2513,UCCN1213,Semester3_GPA,Semester3_CGPA])
    pred =pred.astype(np.float64)
    prediction = mul.predict([pred])
    print(prediction)
    return prediction



def app():
    st.title("Application for prediction of student performance")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction of Cumulative Grade Point Average Year 3 Semester 1 </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    MPU34012 = st.text_input("MPU34012","Type Here")
    UCCD2502 = st.text_input("UCCD2502","Type Here")
    UCCD2513   = st.text_input("UCCD2513","Type Here")
    UCCN1213   = st.text_input("UCCN1213","Type Here")
    Semester3_GPA     = st.text_input("Semester3_GPA","Type Here")
    Semester3_CGPA    = st.text_input("Semester3_CGPA","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(MPU34012,UCCD2502,UCCD2513,UCCN1213,Semester3_GPA,Semester3_CGPA)
    st.success('The output is {}'.format(result))
    



