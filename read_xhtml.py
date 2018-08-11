#will import Russian text, and then output in editor
import os
from bs4 import BeautifulSoup
print("cwd: ", os.getcwd())

print ("hello world")

soup = BeautifulSoup(open(".\dnevnik_1890_51_tom(1)/OEBPS/Text/0001_1009_2001.xhtml", encoding = 'utf-8'), 'html.parser')

#print(soup.prettify())

print(soup.title)

print(soup.text)
