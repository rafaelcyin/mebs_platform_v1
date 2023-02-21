import streamlit as st
from db import create_patient_table, register_patient

st.set_page_config(page_title="MEBS | Register")

st.title("Register Patient")
f_name = st.text_input("First Name")
l_name = st.text_input("Last Name")
birth = str(st.date_input("Birth Date"))
cpf = st.text_input("CPF")
gender = st.radio("Gender", ['M', "F"])
check_reg = st.checkbox("Reviewed Registration Information")
button = st.button("Register")
if button and (f_name and l_name and birth and cpf and gender and check_reg) == True:
    create_patient_table()
    register_patient(f_name, l_name, birth, cpf, gender)
    st.success("Patient Registered")
    print(type(birth))




