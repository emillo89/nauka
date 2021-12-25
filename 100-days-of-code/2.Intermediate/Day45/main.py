from bs4 import BeautifulSoup
import lxml

with open("index.html", "r") as file:
    contents = file.read()
    print(contents)

soup = BeautifulSoup(contents, "html.parser" )

# print(soup.title)
# print(soup.prettify())
print(soup.a)