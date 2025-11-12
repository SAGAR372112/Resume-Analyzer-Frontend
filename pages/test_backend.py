import streamlit as st
from utils.api_client import test_backend

st.title("🧩 Checking Health of Backend")
st.caption("This page checks whether our backend API is up and running.")

# Run health check
check_health = test_backend()

if check_health:
    st.success("✅ Backend is healthy and reachable!")
    st.json(check_health)  # Optionally display the JSON response from backend
else:
    st.error("❌ Backend is not responding. Please check your Render service.")
    st.info("Tip: If you are using Render free tier, the service might be waking up from sleep.")
