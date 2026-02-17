---
title: BioSense AI API
emoji: 🔬
colorFrom: indigo
colorTo: blue
sdk: docker
app_port: 7860
---

# 🔬 BioSense AI - Biomedical Search Engine

An intelligent, Google Scholar-style semantic search engine for biomedical literature and clinical trials powered by BioBERT and AI.

![BioSense AI](https://img.shields.io/badge/BioSense-AI-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-green?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=flat-square)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-8.11-yellow?style=flat-square)

## 📊 What's Inside

- **1,800+ Documents**: PubMed articles + clinical trials indexed
- **20+ Medical Topics**: COVID-19, cancer, diabetes, Alzheimer's, HIV, cardiovascular, and more
- **Smart Search**: Hybrid keyword + semantic search with BioBERT embeddings
- **Question Answering**: Ask medical questions and get evidence-based answers
- **Trending Topics**: Explore what's popular in biomedical research

---

## ✨ Features

### 🔍 Search Capabilities
| Feature | Description |
|---------|-------------|
| **Semantic Search** | AI-powered search understands medical context and synonyms |
| **Hybrid Search** | Combines keyword matching with semantic understanding |
| **Search History** | Quick access to your recent searches |
| **Autocomplete** | Smart suggestions as you type |
| **Advanced Search** | Boolean operators, exact phrases, author/journal filters |
| **Search Highlighting** | Matching terms highlighted in results |

### 📚 Results & Export
| Feature | Description |
|---------|-------------|
| **Save/Bookmark** | Save articles to your reading list |
| **Export Results** | Download as CSV or BibTeX |
| **Citation Generator** | One-click citations in APA, MLA, Chicago, BibTeX |
| **Share Article** | One-click sharing via Web Share API or clipboard |
| **Pagination** | Navigate through results with keyboard arrows |
| **View Modes** | List view or compact view |

### 🎛️ Filters
| Filter | Options |
|--------|---------|
| **Source Type** | All Sources, PubMed, Clinical Trials |
| **Date Range** | Any time, Since 2024/2023/2020, Custom range |
| **Article Type** | Research, Review, Meta-analysis, Case Study, Clinical Trial |
| **Language** | English, Spanish, German, French, Chinese, Japanese |
| **Sort By** | Relevance, Date (newest/oldest), Most Cited |

### 📈 Analytics
- **Trending Topics**: See what's popular in biomedical research
- **Publication Trends**: Visualize research trends over time
- **Related Searches**: Discover related search terms

### ⌨️ Keyboard Shortcuts
| Shortcut | Action |
|----------|--------|
| `Ctrl + K` | Focus search bar |
| `Ctrl + Shift + F` | Open advanced search |
| `1` / `2` / `3` | Switch to Articles / Q&A / Trends tab |
| `B` | Toggle reading list |
| `D` | Toggle dark mode |
| `←` / `→` | Navigate pages |
| `?` | Show keyboard shortcuts |
| `Escape` | Close modals |

---

## 🚀 Quick Start

### 1. Start Docker Services

```powershell
cd docker
docker-compose up -d
```

This starts:
- Elasticsearch (port 9201)
- Redis (port 6380)
- PostgreSQL (port 5433)

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Start Backend API

Open a **new terminal**:

```powershell
uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload
```

Wait for: `✅ API ready to accept requests`

### 4. Start Frontend

Open **another new terminal**:

```powershell
cd frontend
python -m http.server 8080
```

### 5. Open in Browser

Go to: **http://localhost:8080**

---

## 🎯 How to Use

### 📖 Search Tab
1. Type your query (e.g., "COVID-19 treatment")
2. Use filters on the left sidebar:
   - Select source: PubMed, Clinical Trials, or Both
   - Choose date range
   - Adjust search mode slider (keyword ↔ semantic)
3. View results with:
   - Article details, authors, publication date
   - Save to reading list
   - Generate citations
   - View on PubMed/ClinicalTrials.gov

### ❓ Ask Questions Tab
1. Type a medical question (e.g., "What are the symptoms of diabetes?")
2. Select source and number of answers (1, 3, or 5)
3. Get evidence-based answers with:
   - Confidence scores
   - Source citations
   - Supporting evidence passages

### 📈 Trends Tab
- Explore trending research topics
- See growth percentages
- Click topics to search
- View publication trend charts

### 📚 Reading List
- Click bookmark icon on any article to save
- Access from the 🔖 icon in header
- Export as CSV or BibTeX
- Generate citations for saved articles

---

## 🛑 How to Stop

```powershell
# Stop Docker services
cd docker
docker-compose down

# Stop API & Frontend: Press Ctrl+C in their terminals
```

---

## 🔧 Troubleshooting

### Port already in use?
```powershell
# Kill process on port 8000
Stop-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess -Force

# Kill process on port 8080
Stop-Process -Id (Get-NetTCPConnection -LocalPort 8080).OwningProcess -Force
```

### Elasticsearch not connecting?
```powershell
# Check if Docker is running
docker ps

# Restart Docker services
cd docker
docker-compose restart
```

### Need to reindex data?
```powershell
python scripts/ingest_full_dataset.py
```

---

## 📁 Project Structure

```
kash_proj/
├── src/                    # Source code
│   ├── api/               # FastAPI backend
│   ├── search_engine/     # Hybrid search
│   ├── qa_module/         # Question answering
│   └── nlp_engine/        # BioBERT models
├── frontend/              # Web interface
│   ├── index.html         # Main HTML with all components
│   ├── app.js             # JavaScript (search, bookmarks, citations)
│   └── styles.css         # Google Scholar-style CSS
├── docker/                # Docker services
│   └── docker-compose.yml
├── scripts/               # Utility scripts
│   ├── ingest_full_dataset.py
│   └── check_index_status.py
├── data/                  # Cached data
└── tests/                 # Integration tests
```

---

## 🧪 Run Tests

```powershell
pytest tests/test_integration.py -v
```

All tests should pass ✅

---

## 📊 Check System Status

```powershell
# Check indexed documents
python scripts/check_index_status.py

# Check API health
curl http://localhost:8000/api/v1/health

# Check statistics
curl http://localhost:8000/api/v1/statistics
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3.9+, FastAPI, Uvicorn |
| **NLP/AI** | PyTorch, Transformers, BioBERT |
| **Search** | Elasticsearch 8.11.0 |
| **Cache** | Redis 7 |
| **Database** | PostgreSQL |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+) |
| **Deployment** | Docker, Docker Compose |

---

## 📝 Sample Queries to Try

### Search Queries
- `COVID-19 vaccine efficacy`
- `cancer immunotherapy`
- `diabetes treatment 2024`
- `CRISPR gene editing`
- `mRNA vaccine technology`

### Questions
- What are the symptoms of COVID-19?
- How is diabetes treated?
- What causes Alzheimer's disease?
- What are the side effects of chemotherapy?
- How does HIV affect the immune system?

---

## 🌙 Theme Support

BioSense AI supports both **Light** and **Dark** themes:
- Toggle with the sun/moon icon in the header
- Or press `D` key
- Preference is saved automatically

---

## 📱 Responsive Design

The UI is fully responsive and works on:
- 🖥️ Desktop (full sidebar, all features)
- 💻 Laptop (adaptive layout)
- 📱 Mobile (collapsed sidebar, touch-friendly)

---

## 🔒 Privacy

- **No account required** - works without login
- **Local storage only** - reading list and preferences saved in your browser
- **No tracking** - your searches stay private

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sasidhara Kashyap Ch**

Made with ❤️ using BioBERT, Elasticsearch, and FastAPI

---

## 🙏 Acknowledgments

- [BioBERT](https://github.com/dmis-lab/biobert) - Biomedical language model
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/) - Biomedical literature database
- [ClinicalTrials.gov](https://clinicaltrials.gov/) - Clinical trials registry
- [Elasticsearch](https://www.elastic.co/) - Search engine
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
