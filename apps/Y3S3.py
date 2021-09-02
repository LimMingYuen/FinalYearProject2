import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("Y3S3.pkl","rb")
mul = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(UBTM1013,UCCD1113,UCCD3033,Semester2_GPA,Semester2_CGPA):
   
    pred = np.array([UBTM1013,UCCD1113,UCCD3033,Semester2_GPA,Semester2_CGPA])
    pred =pred.astype(np.float64)
    prediction = mul.predict([pred])
   
    print(prediction)
    return prediction



def app():
    st.title("Application for prediction of student performance")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction of Cumulative Grade Point Average Year 3 Semester 3 </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    UBTM1013 = st.text_input("UBTM1013","Type Here")
    UCCD1113 = st.text_input("UCCD1113","Type Here")
    UCCD3033   = st.text_input("UCCD3033","Type Here")
    Semester2_GPA     = st.text_input("Semester2_GPA","Type Here")
    Semester2_CGPA    = st.text_input("Semester2_CGPA","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(UBTM1013,UCCD1113,UCCD3033,Semester2_GPA,Semester2_CGPA)
    st.success('The output is {}'.format(result))
    


