Here is a professional `README.md` for your project. It includes setup instructions, a feature list, and clear guidance on how to use the application.

---

# 🎨 AI Image Generation Chatroom

A sleek, modern **Streamlit** web application that transforms text prompts into high-quality images using OpenAI's DALL-E models. Featuring a native chat-style interface, it allows for a seamless creative flow where users can view their prompt history and generated artwork in a single conversation thread.

---

## ✨ Features

* **Chat-Based UX:** Familiar messaging interface using `st.chat_message` and `st.chat_input`.
* **Persistent Session:** Your session state keeps track of the conversation, so images don't disappear when you send a new prompt.
* **Model Selection:** Choose between **DALL-E 3** (High quality/Detail) and **DALL-E 2** (Faster/Classic).
* **Secure API Handling:** Input your OpenAI API key directly through the sidebar; it is never hardcoded.
* **Responsive Design:** Works on desktops, tablets, and mobile browsers.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/hiepgithub2001/image_generation.git
cd image_generation

```

### 2. Install Dependencies

Ensure you have Python 3.8+ installed. Install the required libraries via pip:

```bash
pip install streamlit openai

```

### 3. Run the Application

Start the Streamlit server:

```bash
streamlit run app.py

```

---

## 🛠️ Usage

1. **Launch the App:** Once running, your browser should open to `http://localhost:8501`.
2. **Enter API Key:** Expand the sidebar on the left and paste your **OpenAI API Key**.
> *Note: Your key is only stored in the local session and is not saved to any database.*


3. **Select Model:** Choose `dall-e-3` for the best results.
4. **Start Chatting:** Type a descriptive prompt in the chat box at the bottom (e.g., *"A cyberpunk samurai cat in a rain-slicked Tokyo alleyway"*).
5. **Wait for Generation:** The "Assistant" will show a loading spinner while the AI brushes your canvas.

---

## 📦 Project Structure

```text
.
├── app.py              # Main Streamlit application code
├── requirements.txt    # List of Python dependencies
└── README.md           # Project documentation

```

---

## 📝 Tips for Best Results

* **Be Descriptive:** Instead of "a dog," try "a golden retriever wearing a space suit on Mars, digital art style."
* **Specify Style:** Mention artists or styles like "Oil painting," "Unreal Engine 5 render," or "Minimalist vector art."
* **DALL-E 3:** Use DALL-E 3 for complex prompts involving specific text or intricate detail.

---

**Would you like me to add a section to this README explaining how to deploy this to the web for free using Streamlit Cloud?**