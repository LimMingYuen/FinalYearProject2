import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

def app():
  st.title("Analysis of subject")

  uploaded_file = st.file_uploader("Choose a file")
  if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    df.sort_values('Year', ascending=True, ignore_index=True, inplace=True)
    st.header("This is a table to perform statiscal calculation on the data")
    st.write(df.describe())
    st.header("This is interactive table that display the student grade in each year")
    fig = px.bar(df, x ="Grade",color='Grade',animation_frame='Year',title="Every year student's grade")
    fig.update_layout(width=800)
    st.write(fig)
    st.header("This is interactive table that display the student grade in each year for each state")
    state_options =df['State'].unique().tolist()
    year_options = df['Year'].unique().tolist()
    year = st.selectbox('Which year would like to see?', year_options,0)
    state = st.selectbox('Which state would you like to see?',state_options,0)

    df = df[df['State']==state]
    df = df[df['Year']==year]
    fig2 = px.bar(df, x ='Grade',color='Grade',title="Student's grade in each year for each state")
    fig2.update_layout(width=800)
    st.write(fig2)
    fig3 = plt.figure()
    sns.countplot(df['Assignment'], label='count')
    st.pyplot(fig3)
    fig4 = plt.figure()
    sns.countplot(df['Midterm1'], label='count')
    st.pyplot(fig4)
    fig5 = plt.figure()
    sns.countplot(df['Midterm2'], label='count')
    st.pyplot(fig5)
    fig6 = plt.figure()
    sns.countplot(df['Quiz'], label='count')
    st.pyplot(fig6)