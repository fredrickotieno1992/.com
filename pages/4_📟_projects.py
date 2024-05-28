import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_geolocation import streamlit_geolocation
st.set_page_config(page_title="fredrick nyangacha", page_icon="🌍", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

st.title("Projects that might interest you")
img_lottie_animation = Image.open("project.png")
img_contact_form = Image.open("best.png")
log = Image.open("dat.png") 
chun = Image.open("churn.png")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.subheader("Performance dashboard")
    st.write("##")
    image_column, text_column = st.columns((2, 1))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Monitor Interventions in Real Time")
        st.write(
            """
            Build a dashboard that track your interventions' targets in real time!
            Sharable dashboard that shows you where you are from reaching your targets,it is interactive and shows in real time
            """
        )
        st.write("For more information,visit.https://dashboard-evidenceaction.streamlit.app/")





with st.container():
    st.write("---")
    st.subheader("Recommender")
    image_column, text_column = st.columns((2, 1))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Fully built and deployed recommender Systems")
        st.write(
            """
            I build fully functional recommender systems the can help customers choose their best products'.
            """
        )

with st.container():
    st.write("---")
    st.subheader("Cross Tabulation")
    image_column, text_column = st.columns((2, 1))
    with image_column:
        st.image(log)
    with text_column:
        st.subheader("Cloud based data collection systems with automatic cross tabs")
        st.write(
            """
            I have built user friendly data collection forms with automatic cross tabs'.
            """
        )

with st.container():
    st.write("---")
    st.subheader("Churn Prediction")
    image_column, text_column = st.columns((2, 1))
    with image_column:
        st.image(chun)
    with text_column:
        st.subheader("Fully deployed customer churn models")
        st.write(
            """
            I build fully functional customer churn models.This can help in reduction of the number of customers leaving the organization.
            """
        )
with st.container():
    st.write("---")