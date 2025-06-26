import requests
from bs4 import BeautifulSoup

# URL of a news website (Example: BBC)
URL = "https://www.indiatoday.in"

# Custom headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send GET request
response = requests.get(URL, headers=headers)

# Check for successful response
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Find headline tags (you might need to inspect the site to get the exact tags)
    headlines = soup.find_all("h3")  # You can also try h2 or other tags

    # Extract and clean text
    top_headlines = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

    # Save to file
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for headline in top_headlines:
            f.write(headline + "\n")

    print(f"✅ Successfully scraped and saved {len(top_headlines)} headlines to 'headlines.txt'")

else:
    print("❌ Failed to retrieve the page. Status code:", response.status_code)
