from code import compile_command
from bs4 import BeautifulSoup
# Maybe needed for some sites:
# import lxml

from black import re_compile_maybe_verbose


with open('45\\website.html', 'r', encoding='utf8') as file:
    content = str(file.readlines())

soup = BeautifulSoup(content, "html.parser")
# Title:
# print(soup.title)
# Title name:
# print(soup.title.name)
# Title contents:
# print(soup.title.string)
# formatted html
# print(soup.prettify())

# first a tag or whatever element respresented:
# print(soup.a)

#find all of whatever element:
# print(soup.find_all(name='a'))
all_anchor_tags = soup.find_all(name='a')

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get('href'))

# Find for h1 by id
heading = soup.find(name="h1", id="name" )
print(heading)

# Find for h3 by class name
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# Find base selector tag:
company_url = soup.select_one(selector='p a')
print(company_url)

headings = soup.select(".heading")
print(headings)