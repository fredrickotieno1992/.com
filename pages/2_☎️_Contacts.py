import streamlit as st
from streamlit_geolocation import streamlit_geolocation
import pandas as pd

st.set_page_config(page_title="fredrick nyangacha", page_icon="🌍", layout="wide")

with st.container():
    st.write("---")
    st.subheader("Click on the button to get the latitude and longitude")
location = streamlit_geolocation()
if location and location['latitude'] is not None and location['longitude'] is not None:
    st.write(f"My location: Latitude {location['latitude']}, Longitude {location['longitude']}")
    st.map(pd.DataFrame({'lat': [location['latitude']], 'lon': [location['longitude']]}), zoom=12)
else:
    st.write("If you require my physical presence, please click the button to share your location with me.")

with st.container():
    st.write("---")
st.subheader("Call me or send me mail on;")
st.write("📞: 0701884577")
st.write("📩: otienofredrickn@gmail.com")
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.write("If you need me in person,you can send me a message using the form below.Click on the location icon to get the Latitudes and Longitudes")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/cc2b563a270fb267e9cfffb8163cbf4d" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
     <input type="number" Longitude="Longitude" placeholder="Longitude" required>
    <input type="number" name="Latitude" placeholder="Latitude" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
with st.container():
    st.write("---")