# Set page configuration
st.set_page_config(page_title="fredrick nyangacha", page_icon="🌍", layout="wide")

# ---- HOME BUTTON ----
st.markdown(
    """
    <style>
    .home-button {
        position: fixed;
        top: 10px;
        right: 10px;
        display: inline-block;
        padding: 10px 20px;
        background-color: brown;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        z-index: 1; /* Ensure the button is above other content */
    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown('<a href="/" class="home-button">Home</a>', unsafe_allow_html=True)

# Get location information
location = streamlit_geolocation()

# Position location information at the top right corner
st.markdown(
    """
    <style>
    .top-right {
        position: fixed;
        top: 10px;
        right: 10px;
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    </style>
    """
    , unsafe_allow_html=True
)

if location and 'latitude' in location and 'longitude' in location:
    st.markdown(f"My location: Latitude {location['latitude']}, Longitude {location['longitude']}", unsafe_allow_html=True, className="top-right")
    st.map(pd.DataFrame({'lat': [location['latitude']], 'lon': [location['longitude']]}), zoom=12)
else:
    st.write("Please click the button to share with me your location.")

# ---- HEADER SECTION ----
with st.container():
    col1, col2 = st.columns([0.5, 1.5])
    with col1:
        st.image("logo.png", width=250)  # Adjust the width as needed
    with col2:
        st.subheader("Hi, I am Fredrick Nyangácha 🧑‍💼")
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

            If this sounds interesting to you, you can contact me using the contact form provided at the bottom of the page.
            """
        )
    with right_column:
        st.image("project.png")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((2, 1))
    with image_column:
        st.image("project.png")
    with text_column:
        st.subheader("Monitor Your KPIs in Real Time")
        st.write(
            """
            Build a dashboard that tracks your KPI targets in real time!
            A shareable dashboard that shows your progress towards your targets in real time.
            """
        )
with st.container():
    text_column, image_column = st.columns((1.75, 0.92))
    with image_column:
        st.image("best.png")
    with text_column:
        st.subheader("Fully functional Recommender Systems")
        st.write(
            """
            Recommend the best for your customers.
            I have experience in building and deploying recommender systems that can help your company or organization realize its goals and objectives. The contact form is provided at the bottom of the page.
            """
        )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Contact form
    name = st.text_input("Your name", max_chars=50)
    email = st.text_input("Your email", max_chars=50)
    message = st.text_area("Your message", max_chars=500)
    submitted = st.button("Send")

    if submitted:
        if name and email and message:
            # Handle form submission here (e.g., send email, store in database)
            st.success("Message sent successfully!")
        else:
            st.error("Please fill out all fields before sending.")