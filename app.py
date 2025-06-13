import streamlit as st
import json

import config
from utils import (
    get_patient_response,
    text_to_speech,
    compute_diagnosis_similarity,
    generate_feedback,
)

st.set_page_config(page_title="Virtual Simulated Patient MVP")
st.title("🩺 Virtual Simulated Patient")

# Load Case
st.sidebar.header("🗂️ Load a Case File")
case_file = st.sidebar.file_uploader("Upload JSON Case File", type="json")

if case_file:
    case_data = json.load(case_file)
    st.sidebar.success(
        f"Loaded patient: {case_data.get('name', 'Unknown')}, age {case_data.get('age', '?')}"
    )

    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
    if 'questions' not in st.session_state:
        st.session_state.questions = []

    st.write(f"Talking to patient: **{case_data['name']}**")
    st.write("Ask about their symptoms or concerns in plain English.")

    user_input = st.text_input("Ask your question:")

    if user_input:
        st.session_state.questions.append(user_input)
        response = get_patient_response(user_input, case_data, st.session_state.conversation)
        st.text_area("Patient Response:", response, height=100)
        text_to_speech(response)

    st.markdown("---")
    final_diag = st.text_input("Your final diagnosis:")
    if st.button("Submit Diagnosis") and final_diag:
        similarity = compute_diagnosis_similarity(final_diag, case_data.get('diagnosis', ''))
        st.write(f"Diagnosis match: {similarity*100:.0f}%")
        feedback = generate_feedback(similarity, case_data, st.session_state.questions)
        st.markdown(feedback)

else:
    st.info("Upload a case file in the sidebar to begin.")
