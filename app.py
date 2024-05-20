import streamlit as st
import pandas as pd
import requests
from PIL import Image
from streamlit_geolocation import streamlit_geolocation

# Function to load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Streamlit configuration
st.set_page_config(page_title="fredrick nyangacha", page_icon="🌍", layout="wide")

# Streamlit code for location information
location = streamlit_geolocation()

if location and location['latitude'] is not None and location['longitude'] is not None:
    st.write(f"My location: Latitude {location['latitude']}, Longitude {location['longitude']}")
    st.map(pd.DataFrame({'lat': [location['latitude']], 'lon': [location['longitude']]}), zoom=12)
else:
    st.write("Please click the button to share with me your location.")

# Load assets and define CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Load Lottie animation and images
lottie_coding = load_lottieurl("https://lottie.host/52d10e39-fd41-4515-981c-1646df08a2a8/FrJzpFHSe4.json")
img_lottie_animation = Image.open("project.png")
img_contact_form = Image.open("best.png")
logo = Image.open("logo.png")

# Display header section
with st.container():
    col1, col2 = st.columns([0.5, 1.5])
    with col1:
        st.image(logo, width=250)
    with col2:
        st.subheader("Hi, I am Fredrick Nyangácha 🧑‍💼")
        st.title("A Data Analyst/Monitoring, Evaluation and Learning Officer")
    st.write("Your introduction text here...")

# Display other sections and content as needed

# HTML and CSS for the location icon at the middle top of the page
st.markdown(
    """
    <style>
    #location-icon-container {
      position: fixed;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      padding: 10px;
      background-color: #f8f9fa;
      border-bottom: 1px solid #ccc;
    }

    #location-icon-container i {
      font-size: 24px;
      color: #007bff;
    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown(
    """
    <div id="location-icon-container">
      <i class="fas fa-map-marker-alt"></i>
    </div>
    """
    , unsafe_allow_html=True
)

# Display contact form
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Contact form
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