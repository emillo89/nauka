from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20210404021759/https://www.billboard.com/charts/hot-100/"

response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")

hot_100 = soup.find_all(name='span',class_="chart-element__information__song text--truncate color--primary")

hot_100_title = [songs.getText() for songs in hot_100]
print(hot_100_title)
