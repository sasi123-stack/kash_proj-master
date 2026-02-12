
import requests
import json
import time
import xml.etree.ElementTree as ET

# --- CONFIGURATION ---
ES_HOST = "assertive-mahogany-1m2hcasg.us-east-1.bonsaisearch.net"
ES_USER = "0204784e62"
ES_PASS = "38aa998d6c5c2891232c"
ES_BASE_URL = f"https://{ES_HOST}:443"

PUBMED_API_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def make_es_request(method, path, data=None):
    url = f"{ES_BASE_URL}/{path}"
    headers = {"Content-Type": "application/json"}
    auth = (ES_USER, ES_PASS)
    
    try:
        if method == "PUT":
            return requests.put(url, auth=auth, headers=headers, json=data)
        elif method == "POST":
            return requests.post(url, auth=auth, headers=headers, json=data)
        elif method == "DELETE":
            return requests.delete(url, auth=auth, headers=headers)
        elif method == "HEAD":
            return requests.head(url, auth=auth, headers=headers)
        elif method == "GET":
             return requests.get(url, auth=auth, headers=headers)
    except Exception as e:
        print(f"ES Request Error: {e}")
    return None

def fetch_pubmed_ids(query, max_results=20):
    """Search PubMed for IDs."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json",
        "email": "student@university.edu"
    }
    try:
        resp = requests.get(f"{PUBMED_API_BASE}/esearch.fcgi", params=params)
        data = resp.json()
        return data["esearchresult"]["idlist"]
    except Exception as e:
        print(f"PubMed Search Error: {e}")
        return []

def fetch_pubmed_details(pmids):
    """Fetch details for a list of PMIDs."""
    if not pmids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
        "email": "student@university.edu"
    }
    
    try:
        resp = requests.post(f"{PUBMED_API_BASE}/efetch.fcgi", data=params) # POST allows more IDs
        return parse_pubmed_xml(resp.text)
    except Exception as e:
        print(f"PubMed Fetch Error: {e}")
        return []

def parse_pubmed_xml(xml_text):
    """Parse PubMed XML into dictionaries."""
    articles = []
    try:
        root = ET.fromstring(xml_text)
        for article in root.findall(".//PubmedArticle"):
            data = {}
            
            # PMID
            pmid = article.find(".//PMID")
            data["id"] = pmid.text if pmid is not None else None
            if not data["id"]: continue

            # Title
            title = article.find(".//ArticleTitle")
            data["title"] = title.text if title is not None else "No Title"

            # Abstract
            abstract_parts = [elem.text for elem in article.findall(".//AbstractText") if elem.text]
            data["abstract"] = " ".join(abstract_parts) if abstract_parts else "No Abstract"

            # Year
            pub_date = article.find(".//PubDate/Year")
            if pub_date is None:
                 # Try MedlineDate
                 pub_date = article.find(".//PubDate/MedlineDate")
                 
            data["publication_year"] = pub_date.text[:4] if pub_date is not None and pub_date.text else "2024"
            
            # Authors
            authors_list = []
            for author in article.findall(".//Author"):
                last = author.find("LastName")
                initials = author.find("Initials")
                if last is not None:
                    name = last.text
                    if initials is not None:
                        name += f" {initials.text}"
                    authors_list.append(name)
            data["authors"] = ", ".join(authors_list[:5]) # Top 5 authors
            
            data["source"] = "pubmed"
            
            articles.append(data)
    except Exception as e:
        print(f"XML Parse Error: {e}")
    
    return articles

def run_ingestion():
    print("🚀 Starting FULL Native Ingestion Pipeline...")
    
    # 1. Setup Index (Text Only)
    index_name = "pubmed_articles"
    # Ensure index exists (we assume it was created by previous script, if not, create simplistic mapping)
    resp = make_es_request("HEAD", index_name)
    if resp.status_code != 200:
        print(f"Creating index '{index_name}'...")
        mapping = {
            "mappings": {
                "properties": {
                    "id": {"type": "keyword"},
                    "title": {"type": "text"},
                    "abstract": {"type": "text"},
                    "authors": {"type": "text"},
                    "publication_year": {"type": "keyword"},
                    "source": {"type": "keyword"},
                    "metadata": {"type": "object"}
                }
            }
        }
        make_es_request("PUT", index_name, mapping)

    # 2. Define Queires
    queries = [
        "cancer immunotherapy",
        "type 2 diabetes treatment",
        "alzheimers disease",
        "CRISPR gene editing",
        "covid-19 vaccine mRNA",
        "hypertension management", 
        "depression cognitive therapy",
        "climate change health impact",
        "artificial intelligence medicine"
    ]

    total_indexed = 0
    
    for q in queries:
        print(f"\nProcessing: '{q}'")
        
        # A. Search
        pmids = fetch_pubmed_ids(q, max_results=100)
        print(f"  Found {len(pmids)} IDs")
        
        # B. Fetch Details
        articles = fetch_pubmed_details(pmids)
        print(f"  Parsed {len(articles)} articles")
        
        # C. Index
        count = 0
        for doc in articles:
            # Metadata Wrapper
            doc["metadata"] = doc.copy()
            
            # Index
            resp = make_es_request("PUT", f"{index_name}/_doc/{doc['id']}", doc)
            if resp and resp.status_code in [200, 201]:
                count += 1
                print(".", end="", flush=True)
            else:
                print("x", end="", flush=True)
                
        total_indexed += count
        print(f" -> {count} indexed")
        time.sleep(1) # Be nice to PubMed API

    print(f"\n\n🎉 Done! Total indexed: {total_indexed}")

if __name__ == "__main__":
    run_ingestion()
