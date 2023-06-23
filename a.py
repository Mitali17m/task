import requests
from bs4 import BeautifulSoup
import csv

def scrape_links(query, max_results, website):
    url = f"https://www.youtube.com/c/OpeninApp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for link in soup.find_all("a"):
        href = link.get("href")
        if href.startswith("/url?q=") and website in href:
            url = href.replace("/url?q=", "").split("&")[0]
            results.append(url)
        if len(results) >= max_results:
            break

    return results

def save_results_to_csv(results):
    with open("search_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Search Results"])
        writer.writerows([[link] for link in results])

query = "openinapp.co"
max_results = 10000
website = "youtube.com"

search_results = scrape_links(query, max_results, website)
save_results_to_csv(search_results)
