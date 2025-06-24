import requests
from bs4 import BeautifulSoup
import csv

URL = "https://github.com/trending"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

repos = soup.find_all("h2", class_="h3 lh-condensed")[:5]

with open("trending_repos.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Repository Name", "Link"])
    
    for repo in repos:
        anchor = repo.find("a")
        repo_name = anchor.text.strip().replace("\n", "").replace(" ", "")
        link = "https://github.com" + anchor["href"]
        writer.writerow([repo_name, link])

print("Top 5 trending repositories saved to trending_repos.csv")
