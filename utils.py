import os
from difflib import get_close_matches, SequenceMatcher

try:
    import openai
except ImportError:  # pragma: no cover - optional dependency
    openai = None

import config

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


def compute_diagnosis_similarity(user_diag: str, true_diag: str) -> float:
    """Return a similarity score between 0 and 1 for two diagnoses."""
    return SequenceMatcher(None, user_diag.lower(), true_diag.lower()).ratio()


def generate_feedback(similarity: float, case_data: dict, asked: list[str]) -> str:
    """Create end-of-case feedback in plain English."""
    feedback = []
    if similarity >= config.DIAGNOSIS_THRESHOLD:
        feedback.append("You're on the right track with your diagnosis.")
    else:
        feedback.append("Your diagnosis was not quite accurate. Consider the key features below.")

    # Note any missed key features
    missed = [k for k in case_data.get("key_features", []) if not any(k.lower() in q.lower() for q in asked)]
    if missed:
        feedback.append("You did not ask about: " + ", ".join(missed))

    summary = "\n".join(feedback)
    summary += f"\n\n**Correct Diagnosis:** {case_data.get('diagnosis', 'Unknown')}\n"
    if case_data.get("key_features"):
        summary += "**Key Features:** " + ", ".join(case_data["key_features"]) + "\n"
    return summary


def get_patient_response(user_input: str, case_data: dict, conversation: list[dict]) -> str:
    """Return a patient response using GPT when available, otherwise simple matching."""
    if openai and os.getenv("OPENAI_API_KEY"):
        if not conversation:
            conversation.append({
                "role": "system",
                "content": (
                    f"You are roleplaying a patient named {case_data['name']}. "
                    "Answer in plain, clear English. Keep replies short (1-3 sentences)."
                )
            })
        conversation.append({"role": "user", "content": user_input})
        resp = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
        reply = resp["choices"][0]["message"]["content"].strip()
        conversation.append({"role": "assistant", "content": reply})
        return reply

    return match_input_to_response(user_input, case_data)
