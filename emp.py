import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
employee_promote = pickle.load(open("C:/Users/Rahul/Downloads/AI ML/employee_prom.sav", 'rb'))

    
# page title
st.title('Employee Promotion using ML')


# getting the input data from the user
col1, col2 = st.columns(2)

with col1:
    subject_employee_id = st.number_input('Employee ID')
    
with col2:
    subject_department = st.text_input('Department')

with col1:
    subject_region = st.text_input('region')

with col2:
    subject_education = st.text_input('Education')

with col1:
    subject_gender = st.radio("Select Gender: ", ('Male', 'Female'))
    if (subject_gender == 'Male'):
        #st.success("Male")
        subject_gender='m'
    else:
       # st.success("Female")
        subject_gender='f'
        
with col2:
    subject_recruitment_channel = st.text_input('Recruitment channel')

with col1:
    subject_no_of_trainings = st.number_input('number of trainings')

with col2:
    subject_age = st.number_input('Age')

with col1:
    subject_previous_year_rating = st.number_input('previous year rating')
    
with col2:
    subject_length_of_service = st.number_input('length of service')

with col1:
    subject_awards_won = st.number_input('awards won last year')

with col2:
    subject_KPI = st.radio("Key Performance Index >80%: ", ('Yes', 'No'))
    if (subject_KPI == 'Yes'):
        subject_KPI='1'
    else:
        subject_KPI='0'

with col1:
    subject_avg_training_score = st.number_input('average training score')
    

# code for Prediction
is_promoted = ''

# creating a button for Prediction

if st.button('Check'):
    prediction = employee_promote.predict([[subject_employee_id, subject_department, subject_region, subject_education, subject_gender, subject_recruitment_channel, subject_no_of_trainings, subject_age, subject_previous_year_rating, subject_length_of_service, subject_KPI, subject_awards_won, subject_avg_training_score]])
    
    if (prediction[0] == 1):
      is_promoted = 'We predict that your promotion is possible'
    else:
      is_promoted = 'We predict that your promotion is NOT possible'
    
st.success(is_promoted)



