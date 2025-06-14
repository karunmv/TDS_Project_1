import requests, json

def scrape_discourse(base_url, pages=10):
    posts = []
    for i in range(pages):
        resp = requests.get(f"{base_url}/latest.json?page={i}")
        if resp.status_code != 200: break
        topics = resp.json().get("topic_list", {}).get("topics", [])
        posts.extend(topics)
    with open("data/discourse.json", "w") as f:
        json.dump(posts, f, indent=2)
    print(f"Scraped {len(posts)} posts")
