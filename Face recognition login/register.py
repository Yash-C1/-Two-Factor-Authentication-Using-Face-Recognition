import streamlit as st
from pymongo import MongoClient, collection
import ssl
import json
from json import JSONEncoder
import numpy as np
#import sample_generator
from sample_generator import main_function
# from app import Registered_users


client = MongoClient("mongodb+srv://Yash:FaceRecognition@cluster0.kczxo.mongodb.net/Users_data?retryWrites=true&w=majority")
db = client['Users_data']
#print(db['Registered users'].name)

def input_data():
    st.title("Welcome to the registration page!")
    st.title(" ")

    st.write("Please fill the following details-")

    name = st.text_input("Enter your name : ")
    password = st.text_input("Enter your password : ")
    rep_password = st.text_input("Re-enter the password : ")
    
    if st.button("Submit and click photos"):
        if(password == rep_password):
            samples_ = main_function()
            
            #------------------------------------------------------

            class NumpyArrayEncoder(json.JSONEncoder):
                def default(self, obj):
                    if isinstance(obj, np.integer):
                        return int(obj)
                    elif isinstance(obj, np.floating):
                        return float(obj)
                    elif isinstance(obj, np.ndarray):
                        return obj.tolist()
                    else:
                        return super(NumpyArrayEncoder, self).default(obj)

            encoded_samples = json.dumps(samples_, cls=NumpyArrayEncoder)

            #------------------------------------------------------

            data = {
                "name" : name,
                "password" : password,
                "photos" : encoded_samples,
            }


            st.text("Registration successful. Now try login.")
            

            db['Registered users'].insert_one(data)
        else:
            st.text("Passwords don't match! Please try again.")