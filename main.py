from bs4 import BeautifulSoup
import requests

url = "https://www.sandiego.gov/events?page=1"

headers = {
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

search_response = requests.get(url)

if search_response.status_code == 200:
    print("connection successful\n")
    soup = BeautifulSoup(search_response.content, "html.parser")

events = soup.find_all("div", class_="event-info")

event_vector = []
for block in events:
    title = block.find('h2', class_='l-margin-tn').text.strip()
    date_time = block.find('p', class_='post__date l-margin-bs').text.strip()
    description = block.children
    event_vector.append({
        "Title": title,
        "Date and Time": date_time,
        "Description": description
    })

print(description)


