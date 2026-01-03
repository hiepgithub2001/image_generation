import streamlit as st
from openai import OpenAI

# 1. Setup & Styling
st.set_page_config(page_title="Image Chat AI", page_icon="🖼️", layout="centered")
st.title("🖼️ Image Generation Chat")

# Sidebar for API Key
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    model = st.selectbox("Model", ["dall-e-3", "dall-e-2"])

# 2. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["type"] == "text":
            st.markdown(message["content"])
        elif message["type"] == "image":
            st.image(message["content"], caption="Generated Image")

# 4. Chat Input Logic
if prompt := st.chat_input("What should I draw for you?"):
    if not api_key:
        st.error("Please provide an API key in the sidebar.")
    else:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "type": "text", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate Image
        try:
            client = OpenAI(api_key=api_key)
            with st.chat_message("assistant"):
                with st.spinner("Brushing the canvas..."):
                    response = client.images.generate(
                        model=model,
                        prompt=prompt,
                        n=1,
                        size="1024x1024"
                    )
                    image_url = response.data[0].url
                    
                    # Display the image
                    st.image(image_url)
                    
                    # Save to history
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "type": "image", 
                        "content": image_url
                    })
        except Exception as e:
            st.error(f"Error: {str(e)}")