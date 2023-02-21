import streamlit as st
st.set_page_config(page_title="MEBS | MebsP3")
import datetime
import os
from PIL import Image
import preparation, classification
import warnings


warnings.filterwarnings("ignore")


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

tab1, tab2 = st.tabs(["Preparation", "Classification"])

with tab1:
    st.title("MebsP3 | Preparation")
    preparation.app()

with tab2:
    st.title("MebsP3 | Classification")
    classification.app()







