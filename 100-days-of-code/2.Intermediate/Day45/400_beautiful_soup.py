from bs4 import BeautifulSoup
import lxml

with open("website.html", "r") as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser" )

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

all_anchar_tags = soup.find_all(name="a")
# print(all_anchar_tags)

# for tag in all_anchar_tags:
#     print(tag.getText())

heading = soup.find(name="h1", id="name")
print(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
heading = soup.select(selector=".heading")
print(name)
print(heading)