# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:16:52 2024

@author: Asus
"""

import numpy as np
import pickle
import streamlit as st
import requests 

loaded_model = pickle.load(open('ModelSchemaUpdated.sav', 'rb'))
# model_url = 'https://github.com/IshrakHamim/futurefit/blob/main/ModelSchema.sav'
# response = requests.get(model_url)
# with open('ModelSchema.sav', 'wb') as f:
#     f.write(response.content)

# loaded_model = pickle.load(open('ModelSchema.sav', 'rb'))
def footer():
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    <div class="footer">
      <p>Copyright &copy; Ishrak and Hemel. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

def feeder(arr):
  for i in range(len(arr)):
    if arr[i] == "Yes":
      arr[i] = 1
    if arr[i] == "No":
      arr[i] = 0
    if arr[i] == "Computer Science":
      arr[i] = 1
    if arr[i] == "Electrical Engineering":
      arr[i] = 2
    if arr[i] == "Mechanical Engineering":
      arr[i] = 3
    if arr[i] == "Civil Engineering":
      arr[i] =  0  
      
      
#creating a function for prediction
def future_fit(input_data):
    feeder(input_data)
    input_data_np = np.asarray(input_data)

    input_data_reshaped = input_data_np.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == "Great":
        return "Great"
    elif prediction[0] == "Decent":
        return "Decent"
    else:
        return "Poor"   

def cgcon(cg):
    try:
        cg_float = float(cg)  # Convert cg to float
        result = np.float64(cg_float * 2.5)  # Perform the calculation
        return str(result)  # Convert the result back to string if needed
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

    
def main():
    st.title('FutureFit')
    st.title('Job Salary Prediction Web App') 
    
    dsa = st.text_input('How many DSA Questions have you solved so far?')
    cgpa = st.text_input('What is your CGPA?')
    ml = st.selectbox(label = 'Do you know Machine Learning?', options = ["Yes", "No"])
    kdsa = st.selectbox(label = 'Do you know Data Structures and Algorithms?', options = ["Yes", "No"])
    python = st.selectbox(label = 'Do you know Python?', options = ["Yes", "No"])
    js = st.selectbox(label = 'Do you know JavaScript?', options = ["Yes", "No"])
    html = st.selectbox(label = 'Do you know HTML?', options = ["Yes", "No"])
    css = st.selectbox(label = 'Do you know CSS?', options = ["Yes", "No"])
    club = st.selectbox(label = 'Were you active in any coding club?', options = ["Yes", "No"])
    backlog = st.text_input('How many backlogs do you have?')
    age = st.text_input('What is your Age?')
    major = st.selectbox(label = 'What is your branch of ? Select from the dropdown menu', options = ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering"])
    
    forecast = ''
    
    st.write('If your package is _lower than **10LPA**_ then it will be classified as **Poor**')
    st.write('If your package is _between **10LPA** to **20LPA**_ then it will be classified as **Decent**')
    st.write('If your package is _higher than **20LPA**_ then it will be classified as **Great**')

    cgpa = cgcon(cgpa)
    if st.button('Predict Placement Catagory'):
        forecast = future_fit([dsa, cgpa, ml , kdsa , python, js , html, css, club , backlog, age, major])
        
    st.success(forecast)
    footer()
    
if __name__ == '__main__':
    main() 
