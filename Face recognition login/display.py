import streamlit as st


def first_display_page(name_,confidence_):
    st.write("WELCOME   " , name_)
    st.write("This software detected your face with a confidence score of ", confidence_)
        

