# Face-recognition-login
This is an online application which detects your face and permits login only if the confidence score of your face recognition is greater than 90%

User authentication is very commonly used in most of the applications these days. It is very important for maintaining privacy and security of user data. 
It drastically reduces the chances of successful unauthorized access by verifying the identity of account users. However by traditional ways of user authentication, any other person
having your User ID and Password will easily be able to login and access your account. Hence this is a project designed with an additional feature of face recognition along with the traditional User ID and password as it is.

Working-
1. If you are a new user, you have to register yourself on this portal.
2. While registering, on clicking the submit button to submit your details, the application will capture your photographs which will be stored in an online database based on which the ML model will be trained.
3. After registering, you can login.
4. While logging in, the application will ask you for your details. It will again capture your photos and pass them to the trained model.
5. The login will be successful only if the confidence score obtained from the model is greater than 90 %.
6. Otherwise you will be asked to try again.

Hence if someone else gets your Login ID and Password by any chance, his/her login will not be permitted as the face of the user while logging won't match the face of the user during registration.

Note-
1. There is no need to install any additional packages.
2. Download the whole file and run the app.py file from the terminal using the command "streamlit run app.py"
3. Only if you face a error, try installing open cv extentions using the command "pip install opencv-contrib-python" and rerun the code.
