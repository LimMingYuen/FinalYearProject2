import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("Y3S2.pkl","rb")
mul = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(UAMG1043,UCCA2103,UCCD2063,UCCN2213,UCCD3243,UCCD3583,Semester1_GPA,Semester1_CGPA):
   
  
    pred = np.array([UAMG1043,UCCA2103,UCCD2063,UCCN2213,UCCD3243,UCCD3583,Semester1_GPA,Semester1_CGPA])
    pred =pred.astype(np.float64)
    prediction = mul.predict([pred])
    
   
    print(prediction)
    return prediction



def app():
    st.title("Application for prediction of student performance")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction of Cumulative Grade Point Average Year 3 Semester 2 </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    UAMG1043 = st.text_input("UAMG1043","Type Here")
    UCCA2103 = st.text_input("UCCA2103","Type Here")
    UCCD2063   = st.text_input("UCCD2063","Type Here")
    UCCN2213   = st.text_input("UCCN2213","Type Here")
    UCCD3243  = st.text_input("UCCD3243","Type Here")
    UCCD3583   = st.text_input("UCCD3583","Type Here")
    Semester1_GPA  = st.text_input("Semester1_GPA","Type Here")
    Semester1_CGPA = st.text_input("Semester1_CGPA","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(UAMG1043,UCCA2103,UCCD2063,UCCN2213,UCCD3243,UCCD3583,Semester1_GPA,Semester1_CGPA)
    st.success('The output is {}'.format(result))
    



