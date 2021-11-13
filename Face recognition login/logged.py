#import display
import streamlit as st
import Trained_model

def welcome():
    confidence_score = 0
    st.title('Welcome to the portal!')
    st.title('')
    input_name = st.text_input("Enter your name : ")
    input_password = st.text_input("Enter your password : ")
    st.text("Click on this button to verify your face and Login.")

    if st.button("Verify and Login"):
        confidence = Trained_model.trained_face_model(input_name,input_password)

        if confidence > 90:
            st.write("WELCOME", input_name )
            st.write("This software detected your face with a confidence score of ", confidence)
        else:
            st.write("Could'nt verify your login credentials or face. Try again.")
        

