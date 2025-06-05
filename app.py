import streamlit as st
import json
from utils import match_input_to_response, text_to_speech

st.set_page_config(page_title="Virtual Simulated Patient MVP")
st.title("🩺 Virtual Simulated Patient")

# Load Case
st.sidebar.header("🗂️ Load a Case File")
case_file = st.sidebar.file_uploader("Upload JSON Case File", type="json")

if case_file:
    case_data = json.load(case_file)
    st.sidebar.success(f"Loaded patient: {case_data.get('name', 'Unknown')}, age {case_data.get('age', '?')}")

    st.write(f"Talking to patient: **{case_data['name']}**")
    st.write("You can ask questions about their symptoms. Try typing one below:")

    user_input = st.text_input("Ask your question:")

    if user_input:
        response = match_input_to_response(user_input, case_data)
        st.text_area("Patient Response:", response, height=100)
        text_to_speech(response)

else:
    st.info("Upload a case file in the sidebar to begin.")
