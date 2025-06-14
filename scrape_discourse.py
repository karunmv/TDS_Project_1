# scrape_discourse.py
import requests

def scrape_discourse(start_date, end_date, base_url):
    # Use Discourse API (add your API key if needed)
    topics = []
    for i in range(0, 100):  # adjust range as needed
        res = requests.get(f"{base_url}/latest.json?page={i}")
        if res.status_code != 200: break
        for topic in res.json().get("topic_list", {}).get("topics", []):
            # Filter based on creation date if available
            topics.append(topic)
    return topics
