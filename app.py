import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
)

# Sidebar navigations
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    selected = option_menu(
        "Navigation",
        ["Resume Analyzer", "Job Description"],
        icons=["file-earmark-text", "briefcase"],
        menu_icon="cast",
        default_index=0,
    )

st.markdown(
    """
    <style>
        .stApp { background-color: #f8fafc; }
        div[data-testid="stSidebar"] { background-color: #1e293b; color: white; }
        h1, h2, h3 { color: #1e293b; font-family: 'Poppins', sans-serif; }
        .stButton>button { background-color: #2563eb; color: white; border-radius: 10px; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

if selected == "Resume Analyzer":
    st.switch_page("pages/resume_analyzer.py")
elif selected == "Job Description":
    st.switch_page("pages/job_descriptions.py")
