import streamlit as st
from utils.api_client import analyze_resume, get_job_descriptions
import plotly.express as px

st.title("📄 Resume Analyzer")
st.caption("Upload your resume and select a job to get AI-powered insights.")

# Step 1: Fetch Job Descriptions from backend
jobs = get_job_descriptions()
if not jobs:
    st.warning("⚠️ No job descriptions available. Make sure backend is running.")
    st.stop()

# Step 2: Let user select a job
job_options = {f"{job['job_title']}": job['id'] for job in jobs}
selected_job = st.selectbox("Select Job Description", list(job_options.keys()))

# Step 3: Upload Resume
uploaded_file = st.file_uploader("Upload your resume (PDF/DOCX)", type=["pdf", "docx"])

# Step 4: Analyze Resume
if uploaded_file and st.button("Analyze Resume"):
    job_id = job_options[selected_job]
    with st.spinner("Analyzing resume..."):
        result = analyze_resume(uploaded_file, job_description_id=job_id)

    if result.get("status"):
        message = result["message"]
        st.success(f"✅ Analysis Complete — Rank: {message['rank']}%")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🧠 Skills Extracted")
            st.write(", ".join(message["skills"]))

            st.subheader("💼 Project Categories")
            st.write(", ".join(message["project_category"]))

        with col2:
            st.subheader("🎓 Total Experience")
            st.metric("Years", message["total_experience"])

            # Visualize Rank as Bar Chart
            fig = px.bar(
                x=["Resume Rank"],
                y=[message["rank"]],
                text=[message["rank"]],
                range_y=[0, 100],
                color=["Resume Rank"]
            )
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.error(f"❌ {result.get('message', 'Analysis failed.')}")
