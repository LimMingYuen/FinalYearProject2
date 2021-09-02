import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("MultipleGrade.pkl","rb")
mul = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(Assignment,Midterm1,Midterm2,Quiz):
   
    pred = np.array([Assignment,Midterm1,Midterm2,Quiz])
    pred =pred.astype(np.float64)
    prediction = mul.predict([pred])
  
    print(prediction)
    return prediction



def app():
    st.title("Application for prediction of student performance")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction for subject that consist multiple grade </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Assignment = st.text_input("Assignment","Type Here")
    Midterm1= st.text_input("Midterm1","Type Here")
    Midterm2   = st.text_input("Midterm2","Type Here")
    Quiz       = st.text_input("Quiz","Type Here")
    result=""
    st.text("If value = 0, grade = A, if value = 1, grade = B" )
    st.text("If value = 2, grade = C, if value = 3, Grade = F")
    if st.button("Predict"):
        result=predict_note_authentication(Assignment,Midterm1,Midterm2,Quiz)
    st.success('The output is {}'.format(result))
    

