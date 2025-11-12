import streamlit as st
from utils.api_client import get_job_descriptions

st.title("🧩 Available Job Descriptions")
st.caption("Browse current job openings in the company.")

jobs = get_job_descriptions()

if jobs:
    for job in jobs:
        with st.expander(f"{job['job_title']}"):
            st.text(job["job_description"])
else:
    st.info("No job descriptions available at the moment.")
