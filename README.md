This `README.md` is designed to help your students get set up and provides a clear "bypass" guide for when they hit the 100-credit free limit on Clipdrop.

---

# 🎓 Student Image Visualization Lab

A dedicated Streamlit application designed for students to visualize complex concepts in **Math, Science, History, and Literature**. Powered by the **Clipdrop API**, this tool transforms descriptive prompts into high-quality educational diagrams and illustrations.


## 🚀 Quick Start

### 1. Installation

Ensure you have Python installed, then run:

```bash
bash run.sh

```

### 2. Configure Secrets

Create a file at `.streamlit/secrets.toml` and add your API key:

```toml
CLIPDROP_API_KEY = "your_clipdrop_api_key_here"

```

### 3. Run the App

```bash
streamlit run app.py

```

---

## 📚 Subject-Specific Features

The app includes a sidebar to select your study topic. Each topic automatically applies a "hidden" style to ensure the AI creates educational content:

* **Physics/Biology:** Focuses on textbook-style accuracy and labeling.
* **Math:** Prioritizes clean, geometric, and 2D vector styles.
* **Literature:** Uses evocative, storytelling-focused oil painting styles.

---

## ⚠️ Reached the Image Limit? (Free Tier Guide)

GUIDELINE VIDEO: https://www.youtube.com/watch?v=71yKQoC_zKo

Clipdrop provides **100 free credits** per account. If you see a "Quota Exceeded" error, follow these steps to generate a new API key for free:

### Step 1: Get a Temporary Phone Number

Since Clipdrop requires phone verification for a new account, use a disposable number service to keep your private number safe.

1. Go to **[Temp-Number.com](https://temp-number.com/)**.
2. Select a country (e.g., USA or UK) and look for an active number.
3. Keep this tab open; you will need to come back here to read the incoming SMS code.

### Step 2: Sign Up for a New Clipdrop Account

1. Open an Incognito/Private browser window.
2. Go to the **[Clipdrop API Signup](https://clipdrop.co/apis/docs/cleanup)**.
3. Register with a new email address (you can use a temporary email if needed).
4. When asked for a phone number, enter the number you found on **Temp-Number.com**.

### Step 3: Verify and Retrieve Key

1. Click "Send Code" on Clipdrop.
2. Switch back to the **Temp-Number.com** page and refresh it until you see the SMS from Clipdrop.
3. Enter the code into Clipdrop to verify.
4. Once logged in, go to your **Account Settings** to copy your new **API Key**.
5. Update your `.streamlit/secrets.toml` file with this new key.

---

## 🛠️ Troubleshooting

* **429 Error:** You have sent too many requests too quickly. Wait 60 seconds.
* **401 Error:** Your API key is invalid or has run out of credits. Follow the "Free Tier Guide" above.
* **No Image Found:** Ensure your prompt is descriptive. Clipdrop works best when you describe colors, styles, and specific objects.

---

**Would you like me to add a script that automatically checks if your API key still has credits remaining?**