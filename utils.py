from difflib import get_close_matches

# Placeholder matcher using string similarity
def match_input_to_response(user_input, case_data):
    questions = list(case_data.get("responses", {}).keys())
    match = get_close_matches(user_input.lower(), questions, n=1, cutoff=0.4)
    if match:
        return case_data["responses"][match[0]]
    return "I'm sorry, could you ask that another way?"

# Dummy TTS (Streamlit Cloud can't play audio yet, placeholder for future)
def text_to_speech(response_text):
    print(f"VSP says: {response_text}")
