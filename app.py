import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Page Config
st.set_page_config(page_title="Student Image Lab", page_icon="🎓", layout="wide")

# 1. API Configuration
CLIPDROP_API_URL = "https://clipdrop-api.co/text-to-image/v1"
API_KEY = st.secrets["CLIPDROP_API_KEY"]

# 2. Sidebar for Subjects
with st.sidebar:
    st.title("📚 Study Room")
    subject = st.selectbox(
        "What are we studying?",
        ["General", "Math", "Literature", "Geography", "Physics", "Biology", "History"]
    )
    st.divider()
    st.info("Clipdrop is now powering our visuals!")

# 3. Subject-Specific Modifiers
subject_modifiers = {
    "General": "",
    "Math": "mathematical visualization, geometric perfection, clean, 2d, ",
    "Literature": "classic book illustration, oil painting style, atmospheric, ",
    "Geography": "topographic satellite view, realistic map, high detail, ",
    "Physics": "scientific physics diagram, labeled parts, high resolution, ",
    "Biology": "microscopic biological detail, textbook illustration, anatomical, ",
    "History": "authentic historical style, vintage photograph, classic painting, "
}

# 4. Chat UI Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["type"] == "text":
            st.markdown(message["content"])
        else:
            st.image(message["content"])

# 5. Handle Chat Input
if raw_prompt := st.chat_input(f"Describe a {subject} concept..."):
    # Show user prompt
    st.session_state.messages.append({"role": "user", "type": "text", "content": raw_prompt})
    with st.chat_message("user"):
        st.markdown(raw_prompt)

    # Enhance prompt
    enhanced_prompt = f"{subject_modifiers[subject]}{raw_prompt}"

    with st.chat_message("assistant"):
        with st.spinner(f"Clipdrop is sketching your {subject} aid..."):
            try:
                # CLIPDROP API CALL
                # Note: Clipdrop expects 'multipart/form-data'
                response = requests.post(
                    CLIPDROP_API_URL,
                    headers={"x-api-key": API_KEY},
                    files={"prompt": (None, enhanced_prompt, "text/plain")}
                )

                if response.ok:
                    # Convert bytes to Image
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption=f"Visual: {raw_prompt}")
                    
                    # Save to session history
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "type": "image", 
                        "content": img
                    })
                else:
                    st.error(f"Clipdrop Error ({response.status_code}): {response.text}")

            except Exception as e:
                st.error(f"A technical error occurred: {e}")