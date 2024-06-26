import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_geolocation import streamlit_geolocation

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="fredrick nyangacha", page_icon="🌍", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/52d10e39-fd41-4515-981c-1646df08a2a8/FrJzpFHSe4.json")
img_lottie_animation = Image.open("project.png")
img_contact_form = Image.open("best.png")
logo = Image.open("fred.png") 

# ---- HEADER SECTION ----
with st.container():
    st.write("---")
    col1, col2 = st.columns([0.5, 1.5])
    with col1:
        st.image(logo, width=150)  # Adjust the width as needed
    with col2:
        st.subheader("Hi, I am Fredrick Nyangácha 🙋🏾‍♂️")
        st.title("A Data Analyst/Monitoring,Evaluation and Learning  Officer")
    st.write(
        "I am a data-driven professional with expertise in data analysis, monitoring, evaluation, and learning. My skills include:\n"
        "- Proficient in Python, SQL, and data visualization tools like Tableau\n"
        "- Experience in data cleaning, processing, and analysis to derive actionable insights\n"
        "- Skilled in developing interactive dashboards and reports to communicate findings effectively\n"
        "- Knowledge of monitoring and evaluation frameworks to track project progress and impact\n"
        "- Ability to design and implement learning systems to capture and share knowledge\n"
        "- Strong problem-solving and critical thinking abilities to tackle complex data challenges\n"
        "I am passionate about leveraging data to drive informed decision-making and improve organizational performance. My goal is to contribute to data-driven solutions that create positive change."
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            These are some of the things I do:
            - Ensuring proper planning, monitoring, evaluation, and learning initiatives to provide better information for decision-making and strategic planning.
            - Conducting routine monitoring visits to project sites, data quality assessments, and maintaining databases of assessment results.
            - Developing and implementing Monitoring, Evaluation, and Learning (MEL) frameworks for programs and interventions, ensuring that MEL processes are embedded in program design.
            - Conducting data analysis to track project progress, identify trends, assess performance against targets and indicators, and improve data collection, reporting, analysis, and visualization."

            If this sounds interesting to you,you can contact me using the contact form provided at the bottom of the page.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=600, key="coding")

with st.container():
    st.write("---")
    st.write("If this sounds interesting to you,you can contact me using the phone number or the mail provided on the contact page.You can as well share with me your location using the form provided on the contact page if I am needed phisically.")