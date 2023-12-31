# -*- coding: utf-8 -*-
"""Webscraper

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iZ73dsIw0mNLM8zPsEb42g5vM2BssfON
"""

!pip install bs4

import pandas as pd
from bs4 import BeautifulSoup
import requests

r = requests.get('https://lazybeauty2207.blogspot.com/2022/12/')

b_soup = BeautifulSoup(r.text)

print(b_soup.get_text())

for i in b_soup.findAll("div",{"class":"content"}):
  print((i.find("div",{"class":"content-inner"})).text)

for meta_tag in b_soup.find_all("meta"):
    content_attribute = meta_tag.get("content")
    if content_attribute:
        print(content_attribute)

for div_tag in b_soup.find_all("div"):
    class_attribute = div_tag.get("class")
    if class_attribute:
        print(class_attribute)

text_content = ""

for div_class in ["content-cap-top", "content-fauxborder-left", "cap-bottom"]:
    elements = b_soup.find_all("div", class_=div_class)
    for element in elements:
        text_content += element.get_text(separator=" ", strip=True)

text_content

for script_tag in b_soup.find_all("script"):
    src_attribute = script_tag.get("src")
    if src_attribute:
        print(src_attribute)

for title_tag in b_soup.find_all("title"):
    title_text = title_tag.text
    if title_text:
        print(title_text)