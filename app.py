import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from deep_translator import GoogleTranslator

# Page Config
st.set_page_config(page_title="Student Image Lab", page_icon="🎓", layout="wide")

# 1. Sidebar Configuration
with st.sidebar:
    st.title("📚 Study Room")
    
    # Language Selection
    lang_choice = st.selectbox(
        "Select your language / Chọn ngôn ngữ:",
        ["English", "Tiếng Việt"]
    )
    
    st.divider()
    
    # Subject Selection
    subject = st.selectbox(
        "What are we studying?",
        ["General", "Math", "Literature", "Geography", "Physics", "Biology", "History"]
    )
    st.info("The AI style adapts to your subject choice.")

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

# 4. Translation & Image Generation Logic
input_label = "Describe a concept..." if lang_choice == "English" else "Mô tả một khái niệm..."

if raw_prompt := st.chat_input(input_label):
    st.session_state.messages.append({"role": "user", "type": "text", "content": raw_prompt})
    with st.chat_message("user"):
        st.markdown(raw_prompt)

    with st.chat_message("assistant"):
        loading_text = "Generating image (this takes ~30s)..." if lang_choice == "English" else "Đang tạo hình ảnh (mất khoảng 30 giây)..."
        with st.spinner(loading_text):
            try:
                # STEP A: Handle Translation
                if lang_choice == "Tiếng Việt":
                    english_prompt = GoogleTranslator(source='vi', target='en').translate(raw_prompt)
                    st.caption(f"Translated: {english_prompt}")
                else:
                    english_prompt = raw_prompt

                # STEP B: Apply modifiers
                enhanced_prompt = f"{subject_modifiers[subject]}{english_prompt}"

                # STEP C: Call Cloudflare Worker API (Token is now completely hidden)
                url = "https://image-api.hiep622032001.workers.dev"
                api_token = "12345678"  # Hardcoded hidden token
                
                headers = {
                    "Authorization": f"Bearer {api_token}",
                    "Content-Type": "application/json"
                }
                payload = {"prompt": enhanced_prompt}

                response = requests.post(url, headers=headers, json=payload, timeout=60)

                if response.ok:
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption=f"Result for: {raw_prompt}")
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "type": "image", 
                        "content": img
                    })
                elif response.status_code == 401:
                    st.error("Authentication Error: The internal token is incorrect.")
                else:
                    st.error(f"Error {response.status_code}")

            except requests.exceptions.Timeout:
                st.error("The AI Worker took too long. Please try a simpler prompt.")
            except Exception as e:
                st.error(f"Error: {e}")