import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon="🌍", layout="wide")

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
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json")
img_lottie_animation = Image.open("project.png")
img_contact_form = Image.open("fred.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Fredrick :wave:")
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

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((2, 1))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Monitor Your KPIs in Real Time")
        st.write(
            """
            Build a dashboard that track your KPI targets in real time!
            Sharable dashboard that shows where you are from reaching your targets,it is fun and shows in real time
            """
        )
with st.container():
    text_column, image_column = st.columns((2, 0.5))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("More will be shown when contacted")
        st.write(
            """
            To be added?
            I have several projects that can help your company or oganization realise its goals and objectives,the contact form is provided at the bottom of the page'.
            """
        )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/cc2b563a270fb267e9cfffb8163cbf4d" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()