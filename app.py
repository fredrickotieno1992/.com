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
lottie_coding = load_lottieurl("https://lottie.host/27f376b2-adf3-4e4d-9c83-36727cf8bf95/iHTboRmxTQ.json")
img_lottie_animation = Image.open("project.png")
img_contact_form = Image.open("fred.png")

# ---- HEADER SECTION ----
st.subheader("Hi, I am Fredrick :wave:")
st.title("A Data Analyst/Monitoring, Evaluation and Learning Officer")
# Add your content here...

# ---- WHAT I DO ----
st.write("---")
st.header("What I do")
# Add your content here...

# ---- PROJECTS ----
st.write("---")
st.header("My Projects")
# Add your content here...

# ---- CONTACT ----
st.write("---")
st.header("Get In Touch With Me!")

# Contact Form
contact_form = """
<form action="https://formsubmit.co/cc2b563a270fb267e9cfffb8163cbf4d" method="POST">
<input type="hidden" name="_captcha" value="false">
<input type="text" name="name" placeholder="Your name" required>
<input type="email" name="email" placeholder="Your email" required>
<textarea name="message" placeholder="Your message here" required></textarea>
<button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)