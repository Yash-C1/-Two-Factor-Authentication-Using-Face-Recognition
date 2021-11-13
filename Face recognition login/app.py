import streamlit as st
import logged
from register import input_data
# from pymongo import MongoClient, collection


# client = MongoClient("mongodb+srv://Yash:FaceRecognition@cluster0.kczxo.mongodb.net/Users_data?retryWrites=true&w=majority")
# db = client['Users_data']
# Registered_users = db['Registered users']


  


st.sidebar.title('Face recognition login')
st.sidebar.title('')
st.sidebar.write("Welcome to face recognition login. If you have not yet registered, please select the register option and fill your name and password.")
st.sidebar.write("This software will save your details and capture your photograph for authentication.")
st.sidebar.write("If you have already registered, choose the login option and fill the details to login.")

choices = ['Register','Login']
st.sidebar.write("\n\n")
option = st.sidebar.radio("Registration or Login?",choices)


st.text(" \n\n")

if option == "Register":
    input_data()
    

elif option == "Login":
    logged.welcome()



