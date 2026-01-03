import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Page Config
st.set_page_config(page_title="Student Image Lab", page_icon="🎓", layout="wide")

# 1. Sidebar Configuration
with st.sidebar:
    st.title("⚙️ App Settings")
    
    # User Input for API Key with your provided default
    default_key = "50f2b15a199dc34afc59ac2b15515b93cda5a28ea269cbf597d3cdb3bca1242e35a9ff7782fe4e63782127626d78666a"
    api_key = st.text_input(
        "Clipdrop API Key", 
        value=default_key, 
        type="password",
        help="Paste your new API key here if the default one runs out of credits."
    )
    
    st.divider()
    st.title("📚 Study Room")
    subject = st.selectbox(
        "What are we studying?",
        ["General", "Math", "Literature", "Geography", "Physics", "Biology", "History"]
    )
    st.info("The AI will adapt its drawing style based on your subject.")

# 2. Subject Prompt Modifiers
subject_modifiers = {
    "General": "",
    "Math": "mathematical visualization, geometric diagram, clean background, 2d vector, ",
    "Literature": "classic book illustration style, atmospheric lighting, oil painting, ",
    "Geography": "topographic satellite view, detailed map style, realistic, ",
    "Physics": "scientific physics diagram, labeled parts, high resolution, ",
    "Biology": "microscopic biological detail, anatomical accuracy, textbook style, ",
    "History": "authentic historical style, vintage photograph or classical painting, "
}

# 3. Chat Logic
st.title(f"🎨 {subject} Visualization Lab")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["type"] == "text":
            st.markdown(message["content"])
        else:
            st.image(message["content"])

# 4. Image Generation Logic
if raw_prompt := st.chat_input(f"Describe a {subject} concept..."):
    st.session_state.messages.append({"role": "user", "type": "text", "content": raw_prompt})
    with st.chat_message("user"):
        st.markdown(raw_prompt)

    enhanced_prompt = f"{subject_modifiers[subject]}{raw_prompt}"

    with st.chat_message("assistant"):
        with st.spinner("Visualizing your concept..."):
            try:
                # API Call using the key from the sidebar input
                response = requests.post(
                    "https://clipdrop-api.co/text-to-image/v1",
                    headers={"x-api-key": api_key},
                    files={"prompt": (None, enhanced_prompt, "text/plain")}
                )

                if response.ok:
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption=f"Aid for: {raw_prompt}")
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "type": "image", 
                        "content": img
                    })
                elif response.status_code == 401:
                    st.error("API Key is invalid or expired. Please update the key in the sidebar.")
                elif response.status_code == 429:
                    st.warning("Daily limit reached! Follow the guide in the README to get a new key.")
                else:
                    st.error(f"Error {response.status_code}: {response.text}")

            except Exception as e:
                st.error(f"Technical error: {e}")