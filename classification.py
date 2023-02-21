import datetime
import streamlit as st
import config
from db import classify_patient

def app():
    classify_btn = st.button("Classify")
    if classify_btn:
        prob = classify_patient(config.id)
        if prob > 0.5:
            classification = "Malignant"
            clf_prob = str(round(prob * 100), 2)
        else:
            classification = "Benign"
            clf_prob = str(round(((1 - prob) * 100), 2))

        st.header('Summary of Classification:')
        st.write("Patient ID: ", str(config.id))
        st.write("Date of Exam: ", str(datetime.date.today()))
        st.write("Classification Probability: ", clf_prob,"%")
        st.write("Classification: ", classification)

