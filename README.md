---
title: BioSense AI
emoji: 🔬
colorFrom: cyan
colorTo: blue
sdk: docker
app_port: 8000
---

# 🔬 BioSense AI - Intelligent Biomedical Research Engine

BioSense AI is a state-of-the-art, evidence-based research platform designed to search through millions of PubMed articles and Clinical Trials. Powered by **OpenClaw RAG** and **Llama 3.3 70B**, it provides lightning-fast semantic search and precise medical question-answering.

[![Website](https://img.shields.io/badge/Website-biomed--scholar.web.app-blue?style=for-the-badge&logo=firebase)](https://biomed-scholar.web.app/)
[![AI Powered](https://img.shields.io/badge/AI--Agent-Groq%20%2F%20Llama%203-orange?style=for-the-badge)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 🚀 Key Features

### 🧠 Advanced AI Agent & RAG
- **Llama 3.3 70B (Via Groq)**: Blazing fast responses (up to 800 tokens/sec) for biomedical Q&A.
- **OpenClaw Integration**: A robust agentic framework that handles complex reasoning and knowledge retrieval.
- **Evidence-Based Answers**: Every answer is grounded in actual PubMed or ClinicalTrials.gov data with direct citations.

### 🔍 Search & Discovery
- **Hybrid Semantic Search**: Combines traditional keyword matching with deep semantic understanding using **BioBERT**.
- **Real-time Analytics**: Trending topics and publication charts to visualize the latest medical breakthroughs.
- **Search Highlighting**: Instant visual feedback on why a result matches your query.

### 📚 Researcher Tools
- **Personal Reading List**: Save articles and sync them locally for later reading.
- **Citation Generator**: Instant support for APA, MLA, Chicago, and BibTeX.
- **Multi-Format Export**: Export your curated research as CSV or BibTeX files.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **AI Architecture** | OpenClaw, RAG (Retrieval-Augmented Generation) |
| **LLM Inference** | **Groq** (Llama 3.3 70B Versatile) |
| **Backend** | Python 3.10+, FastAPI, Uvicorn |
| **Search Engine** | Elasticsearch 8, BioBERT Embeddings |
| **Frontend** | Vanilla JavaScript (ES6+), CSS3 (Modern Glassmorphism Design) |
| **Hosting** | Firebase (Frontend), Hugging Face Spaces (Backend API) |
| **Database/Cache** | PostgreSQL, Redis |

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- Docker & Docker Compose
- Python 3.10+
- [Groq API Key](https://console.groq.com/) (Required for AI Agent)

### 2. Configure Environment
Create a `.env` file in the root directory:
```bash
GROQ_API_KEY=your_groq_key_here
OPENCLAW_API_BASE=https://api.groq.com/openai/v1
ELASTICSEARCH_HOST=localhost
ELASTICSEARCH_PORT=9201
```

### 3. Run Services (Docker)
```powershell
# Start Elasticsearch, Redis, and PostgreSQL
cd docker
docker-compose up -d
```

### 4. Start Backend & Frontend
```powershell
# Install dependencies
pip install -r requirements.txt

# Run API
uvicorn src.api.app:app --reload

# Run Frontend (Simple Server)
cd frontend
python -m http.server 8080
```

---

## 🌐 Deployment

### Frontend (Firebase)
BioSense AI is deployed to Firebase Hosting.
```powershell
firebase deploy
```

### Backend (Hugging Face)
The backend is containerized and hosted on Hugging Face Spaces.
- **Space URL**: [sasidhara123-biomed-scholar-api](https://huggingface.co/spaces/sasidhara123/biomed-scholar-api)
- Uses a Docker SDK for seamless integration.

---

## ⌨️ Keyboard Shortcuts
| Key | Action |
|-----|--------|
| `Ctrl + K` | Focus Search Bar |
| `B` | Toggle Reading List |
| `D` | Toggle Dark Mode |
| `?` | Help / Shortcuts |
| `1 / 2 / 3`| Switch Tabs (Search / QA / Trends) |

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---

**Developed with ❤️ by Sasidhara Kashyap Ch**
