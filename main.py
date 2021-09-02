import streamlit as st
from multipage import MultiApp
from apps import multigrade,passfail,Y1S2,Y1S3,Y2S1,Y2S2,Y3S1,Y3S2,Y3S3,home,Subjects # import app modules here

app = MultiApp()

st.markdown("""
# Welcome to the main page of the application, to go another page please click the dropdown menu.

""")

# Add all application here

app.add_app("Home", home.app)
app.add_app("Subject consist pass and fail only", passfail.app)
app.add_app("Subject consist multiple grade", multigrade.app)
app.add_app("Year 1 Semester 2 CGPA", Y1S2.app)
app.add_app("Year 1 Semester 3 CGPA", Y1S3.app)
app.add_app("Year 2 Semester 1 CGPA", Y2S1.app)
app.add_app("Year 2 Semester 2 CGPA", Y2S2.app)
app.add_app("Year 3 Semester 1 CGPA", Y3S1.app)
app.add_app("Year 3 Semester 2 CGPA", Y3S2.app)
app.add_app("Year 3 Semester 3 CGPA", Y3S3.app)
app.add_app("Subject Analysis", Subjects.app)
# The main app
app.run()