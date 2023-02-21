import os
import streamlit as st
from db import search_patient
import datetime
from PIL import Image
import config

@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    print(type(img))
    return img


def calculate(birth):
    days_in_year = 365.2425
    age = int((datetime.date.today() - birth).days / days_in_year)
    return age
    return str(age)


def save_uploadedfile(uploadedfile, patient_id):
    with open(os.path.join("images", str(patient_id)), "wb") as f:
        f.write(uploadedfile.getbuffer())


st.markdown("""
        <style>
               .block-container {
                    padding-top: 3rem;
                    padding-bottom: 3rem;
                    padding-left: 3rem;
                    padding-right: 3rem;
                }

                .css-91z34k{
                    width: 100%;
                    max-width: 100%;
                {

        </style>
        """, unsafe_allow_html=True)


def app():
    col1, col2 = st.columns(2)
    with col1:
        file = st.file_uploader("Upload Ultrasound Image")
        if file is not None:
            # Display Image
            image = load_image(file)
            st.image(image)

            st.success("File Uploaded")

    with col2:
        id = st.text_input("Search Patient's ID")
        patient_consent = st.radio("Patient consents the use os their images in MEBS Research", ["Yes", "No"])
        search_btn = st.button("Search Patient")
        if search_btn:
            try:
                info = search_patient(id)
                config.id = str(info[0][0])
                today_date = datetime.date.today()
                patient_id = st.write('Patient ID: ', str(info[0][0]))
                f_name = st.write('First Name: ', info[0][1])
                l_name = st.write('Last Name: ', info[0][2])
                birth = st.write('Birth Date: ', info[0][3])
                birth_split = (str(info[0][3])).split("-")
                age_text = str(calculate(datetime.date(int(birth_split[0]), int(birth_split[1]), int(birth_split[2]))))
                age = st.write('Age: ', age_text, ' years')
                cpf = st.write('CPF: ', info[0][4])
                gender = st.write('Gender: ', info[0][5])
                st.success("Successfully Fetched Patient's Information")

                # Store Image in Folder
                filetype = (file.name).split(".")
                filename = str(info[0][0]) + "." + filetype[1]
                save_uploadedfile(file, filename)
            except:
                st.error("Enter a valid Patient's ID")