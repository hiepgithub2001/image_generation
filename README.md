# 🎓 Student Image Visualization Lab

A dedicated local and cloud-based tool designed for students to visualize complex concepts in **Math, Science, History, and Literature**. This project utilizes a custom **Cloudflare Worker** as a proxy to run high-performance AI models.

## 🌟 Key Features

* **Bilingual Support:** Integrated translation for English and Vietnamese prompts.
* **Subject-Specific Styles:** Automatically optimizes prompts for different academic subjects.
* **Custom AI Backend:** Powered by Cloudflare Workers AI for fast and reliable image generation.

---

## 🏗️ Backend Architecture (Cloudflare Workers)

The app does not call third-party APIs directly. Instead, it communicates with a private **Cloudflare Worker** acting as a secure API Gateway.

Link for worker deployment: dash.cloudflare.com
Guideline: https://www.youtube.com/watch?v=VliEpQl06pE


### Worker Code Logic:

The backend is built with the following logic to handle requests and generate images using the `stable-diffusion-xl-base-1.0` model:

```javascript
export default {
  async fetch(request, env) {
      const API_KEY = env.API_KEY;
      const url = new URL(request.url);
      const auth = request.headers.get("Authorization");

      // 🔐 Security: Bearer Token Check
      if (auth !== `Bearer ${API_KEY}`) {
          return json({ error: "Unauthorized" }, 401);
      }

      // 🚫 Method Validation
      if (request.method !== "POST" || url.pathname !== "/") {
          return json({ error: "Not allowed" }, 405);
      }

      try {
          const { prompt } = await request.json();
          if (!prompt) return json({ error: "Prompt is required" }, 400);

          // 🧠 AI Generation using Stable Diffusion XL
          const result = await env.AI.run(
              "@cf/stabilityai/stable-diffusion-xl-base-1.0",
              { prompt }
          );

          return new Response(result, {
              headers: { "Content-Type": "image/jpeg" },
          });
      } catch (err) {
          return json({ error: "Failed to generate image", details: err.message }, 500);
      }
  },
};

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
      status,
      headers: { "Content-Type": "application/json" },
  });
}

```

---

## 🚀 App Deployment Guide (Streamlit Community Cloud)

### 1. GitHub Setup

1. Create a repository and upload: `app.py`, `requirements.txt`, and `README.md`.
2. **Note:** Ensure your `requirements.txt` includes `deep-translator`.

### 2. Connect to Streamlit Cloud

1. Sign in at [share.streamlit.io](https://share.streamlit.io).
2. Deploy your repo and click **Advanced Settings**.
3. In **Secrets**, add your Worker token:
```toml
API_KEY = "12345678"

```
4. Command to generate image:
```
curl -X POST https://image-api.hiep622032001.workers.dev \
  -H "Authorization: Bearer 12345678" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "A cute appler cooking breakfast"}' \
  --output image.jpg
```



### 3. Updating & Rebooting

If the app environment doesn't update after a code push:

1. Click **"Manage app"** (bottom right).
2. Click the **three dots (⋮)** menu.
3. Select **"Reboot app"**.

---

## 🛠️ Usage & Authentication

The app uses a **Bearer Token** for security.

* **Default Token:** `12345678`
* If you have your own Cloudflare Worker deployment, enter your specific `API_KEY` in the sidebar input field.
* Images typically take **~30 seconds** to generate.

---

## 🔧 Requirements

* Python 3.9+
* `streamlit`
* `deep-translator`

**Local Execution:**

```bash
pip install -r requirements.txt
streamlit run app.py

```

---

### 📄 requirements.txt content:

```text
streamlit
deep-translator

```

**Would you like me to add a "Model Selector" to the sidebar so users can choose between different Cloudflare models like `dreamshaper` or `schnell`?**