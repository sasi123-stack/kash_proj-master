# Deploying Backend to Hugging Face Spaces

This guide explains how to host your backend on **Hugging Face Spaces** for free.
**Why Hugging Face Spaces?** It offers **16GB RAM** on the free tier, which is essential for running the BioBERT and ClinicalBERT models that standard free tiers (like Render/Vercel) cannot handle.

---

## 🚀 Step 1: Create Free Database Services

Since Hugging Face Spaces (like Heroku/Render) does not have persistent storage, you need external databases. These services offer generous **Free Tiers**:

### 1. Elasticsearch (Search Engine)
*   **Service**: [Bonsai.io](https://bonsai.io/)
*   **Action**: Sign up and create a free "Sandbox" cluster.
*   **Copy**: The "Full Access URL" (looks like `https://user:pass@cluster-name.bonsai.io`).

### 2. Redis (Cache)
*   **Service**: [Upstash](https://upstash.com/) or [Redis Cloud](https://redis.com/try-free/)
*   **Action**: Create a free Redis database.
*   **Copy**: `REDIS_HOST`, `REDIS_PORT`, and `REDIS_PASSWORD`.

### 3. PostgreSQL (Database)
*   **Service**: [Neon.tech](https://neon.tech/) or [Supabase](https://supabase.com/)
*   **Action**: Create a free project.
*   **Copy**: The `DATABASE_URL`.

---

## 🛰️ Step 2: Create Hugging Face Space

1.  Go to [Hugging Face Spaces](https://huggingface.co/spaces).
2.  Click **"Create new Space"**.
3.  **Name**: `biomed-scholar-api` (or similar).
4.  **License**: `MIT`.
5.  **SDK**: Select **Docker**.
6.  **Space Hardware**: Select **CPU Basic (Free)** (2 vCPU, 16GB RAM).
7.  Click **"Create Space"**.

---

## 🔗 Step 3: Connect Code

1.  In your new Space, go to **"Settings"**.
2.  Scroll to **"Repository secrets"** (Environment Variables).
3.  Add the following secrets (values from Step 1 & your keys):

| Secret Name | Value Example |
|-------------|---------------|
| `ELASTICSEARCH_HOST` | `your-cluster.bonsai.io` |
| `ELASTICSEARCH_PORT` | `443` |
| `ELASTICSEARCH_SCHEME` | `https` |
| `ELASTICSEARCH_USERNAME` | `(from Bonsai URL)` |
| `ELASTICSEARCH_PASSWORD` | `(from Bonsai URL)` |
| `REDIS_HOST` | `your-db.upstash.io` |
| `REDIS_PORT` | `6379` |
| `REDIS_PASSWORD` | `your-password` |
| `DATABASE_URL` | `postgresql://user:pass@host/db` |
| `GROQ_API_KEY` | `gsk_...` |
| `GEMINI_API_KEY` | `...` |
| `APP_ENV` | `production` |
| `LOW_MEMORY_MODE` | `false` (We have 16GB RAM!) |

---

## 🚢 Step 4: Deploy

You have two options to deploy the code:

### Option A: Push to Hugging Face (Easiest)
1.  In your local project folder:
    ```bash
    git remote add space https://huggingface.co/spaces/YOUR_USERNAME/biomed-scholar-api
    git push space master:main
    ```
    *(You may need to generate a Hugging Face Access Token first)*

### Option B: Mirror GitHub (Sync)
1.  In Space **Settings**, go to **"Git"** or **"Repository"**.
2.  Connect your GitHub repository to automatically sync changes.

---

## ⌛ Step 5: Wait & Verify

1.  The "Building" status will appear. It may take **10-15 minutes** to build the Docker container and download dependency models.
2.  Once "Running", you will see a public URL (e.g., `https://username-biomed-scholar-api.hf.space`).
3.  **Update your Frontend**:
    *   Open `frontend/app.js`.
    *   Change the API base URL to your new HF Space URL:
        ```javascript
        // const API_BASE_URL = 'http://localhost:8000/api/v1';
        const API_BASE_URL = 'https://username-biomed-scholar-api.hf.space/api/v1';
        ```
    *   Redeploy frontend.

---

## ⚠️ Important Note on Data
Your new cloud Elasticsearch index will be **empty**. You must run the ingestion script from your local machine (pointing to the cloud) or upload data to populate the search engine.
