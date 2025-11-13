import requests
from bs4 import BeautifulSoup

def fetch_web_scholarships(query):
    search_query = query.replace(" ", "+")
    url = f"https://www.scholarshipportal.eu/scholarships?search={search_query}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    scholarships = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.select("a[data-testid='scholarship-card']")[:5]
        for card in cards:
            title = card.get_text(strip=True)
            link = card.get("href")
            if not link.startswith("http"):
                link = "https://www.scholarshipportal.eu" + link
            scholarships.append({"title": title, "url": link})
    return scholarships