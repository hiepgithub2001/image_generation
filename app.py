import streamlit as st
from openai import OpenAI

# Page Config
st.set_page_config(page_title="Student Image Lab", page_icon="🎓", layout="wide")

# 1. Hidden Secrets & Setup
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
FIXED_MODEL = st.secrets["AI_MODEL"]

# 2. Sidebar for Subjects
with st.sidebar:
    st.title("📚 Study Room")
    st.info("Select your subject to help the AI understand the context.")
    
    subject = st.selectbox(
        "What are we studying?",
        ["General", "Math", "Literature", "Geography", "Physics", "Biology", "History"]
    )
    
    st.write("---")
    st.caption("This tool helps visualize complex concepts. Type your prompt in the chat to begin.")

# 3. Prompt Engineering Logic (Hidden from student)
subject_modifiers = {
    "General": "",
    "Math": "mathematical visualization, geometric perfection, clean white background, 2D vector style, ",
    "Literature": "evocative storytelling style, classic book illustration, atmospheric lighting, ",
    "Geography": "topographic map style, realistic satellite view, detailed earth features, ",
    "Physics": "scientific diagram, labeled parts, realistic physics simulation frame, ",
    "Biology": "microscopic detail, anatomical accuracy, textbook illustration style, ",
    "History": "authentic historical style, vintage photograph or classical oil painting style, "
}

# 4. Chat Interface Logic
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

# Chat Input
if raw_prompt := st.chat_input(f"Describe a {subject} concept..."):
    # Show the student's prompt in chat
    st.session_state.messages.append({"role": "user", "type": "text", "content": raw_prompt})
    with st.chat_message("user"):
        st.markdown(raw_prompt)

    # Enhance prompt based on subject
    enhanced_prompt = f"{subject_modifiers[subject]}{raw_prompt}"

    with st.chat_message("assistant"):
        with st.spinner(f"Creating your {subject} illustration..."):
            try:
                response = client.images.generate(
                    model=FIXED_MODEL,
                    prompt=enhanced_prompt,
                    n=1,
                    size="1024x1024"
                )
                image_url = response.data[0].url
                
                # Display and Save
                st.image(image_url, caption=f"Visual aid for: {raw_prompt}")
                st.session_state.messages.append({
                    "role": "assistant", 
                    "type": "image", 
                    "content": image_url
                })
            except Exception as e:
                st.error("The AI is resting right now. Please try again in a moment!")