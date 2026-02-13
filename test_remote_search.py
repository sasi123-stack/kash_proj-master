import requests
import json

def test_search():
    url = "https://sasidhara123-biomed-scholar-api.hf.space/api/v1/search"
    payload = {
        "query": "cancer immunotherapy",
        "top_k": 5
    }
    
    print(f"Testing search at: {url}")
    try:
        response = requests.post(url, json=payload, timeout=20)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            print(f"Found {len(results)} results")
            
            for i, result in enumerate(results):
                print(f"\nResult {i+1}:")
                print(f"Title: {result.get('title')}")
                print(f"Score: {result.get('score')}")
        else:
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Failed to connect: {e}")

if __name__ == "__main__":
    test_search()
