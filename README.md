# 🎓 Student Image Visualization Lab

A dedicated local and cloud-based tool designed for students to visualize complex concepts in **Math, Science, History, and Literature**. Powered by the **Clipdrop API**, this tool transforms descriptive prompts into high-quality educational diagrams and illustrations.

## 🌟 New Feature: Bilingual Support (English & Tiếng Việt)

The app now supports **Vietnamese**. Students can type their prompts in Vietnamese, and the app will automatically:

1. Translate the prompt to English using the Google Translate API.
2. Apply the relevant subject style modifiers.
3. Generate the image via Clipdrop.
*To use this, simply change the language setting in the sidebar.*

---

## 🚀 Deployment Guide (Streamlit Community Cloud)

To make this app accessible to students via a public URL:

### 1. GitHub Setup

1. Create a **Public Repository** on GitHub.
2. Upload the following files: `app.py`, `requirements.txt`, and `README.md`.
3. **Note:** Do **not** upload the `.streamlit/` folder or `secrets.toml` to GitHub.

### 2. Connect to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in.
2. Click **"Create app"** and point it to your GitHub repository.
3. In **Advanced Settings**, add your default API key in the Secrets box:
```toml
CLIPDROP_API_KEY = "50f2b15a199dc34afc59ac2b15515b93cda5a28ea269cbf597d3cdb3bca1242e35a9ff7782fe4e63782127626d78666a"

```



### 3. How to Update the App (Manual Reboot)

If you push new changes to GitHub (like adding a new library), you **must** manually reboot to avoid errors:

1. Open your deployed app URL.
2. Click **"Manage app"** at the bottom right.
3. Click the **three dots (⋮)** menu icon and select **"Reboot app"**. This forces a fresh installation of all libraries in `requirements.txt`.

---

## 🛠️ Usage & API Keys

The app comes with a pre-configured API key. If you reach the image limit (100 credits), follow these steps to get a new one for free:

### How to get a new API Key:

1. **Get a Temp Number:** Visit [Temp-Number.com](https://temp-number.com/) and pick a number (USA/UK work best).
2. **Register at Clipdrop:** Go to [Clipdrop Cleanup API](https://clipdrop.co/apis/docs/cleanup) and sign up with a new email.
3. **Verify:** Use the number from Step 1 to receive the SMS. Enter the code on Clipdrop.
4. **Copy Key:** Copy the new API key from your dashboard.
5. **Paste in Sidebar:** Paste it into the **"Clipdrop API Key"** field in the app sidebar.

---

## 📚 Features for Students

* **Bilingual UI:** Toggle between English and Vietnamese.
* **Subject Specificity:** Automatically applies styles for Math, Biology, Physics, etc.
* **Session History:** Scroll back to see all generated images in the current session.
* **Privacy:** API keys are masked as password fields for safe classroom use.

---

## 🔧 Requirements

To run locally or deploy, the following libraries are required:

* Python 3.9+
* `streamlit`
* `deep-translator` (Required for Vietnamese support)

**Installation:**

```bash
pip install -r requirements.txt
streamlit run app.py

```

---

### 📄 Your `requirements.txt` file content:

Copy this into your `requirements.txt` file to ensure the deployment works:

```text
streamlit
deep-translator

```

**Would you like me to help you add a "Download Image" button so students can save the generated diagrams to their computers?**