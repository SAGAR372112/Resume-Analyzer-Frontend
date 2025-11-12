import requests

BASE_URL = st.secrets["BACKEND_URL"]

def analyze_resume(file, job_description_id=None):
    files = {"resume": file}
    data = {}
    if job_description_id:
        data["job_description"] = job_description_id
    response = requests.post(f"{BASE_URL}/resume-analyze/", files=files, data=data)
    return response.json()

def get_job_descriptions():
    response = requests.get(f"{BASE_URL}/job-descriptions/")
    return response.json() if response.status_code == 200 else []

def test_backend():
    """Check if backend is reachable and returns a valid response."""
    try:
        response = requests.get(BASE_URL + "test/")
        if response.status_code == 200:
            return response.json()  
        else:
            return None
    except requests.exceptions.RequestException:
        return None
