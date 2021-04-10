import requests
from bs4 import BeautifulSoup


response = requests.get('https://thehost.ua/ua/domains/whois')


if response.status_code ==200:
  html_doc = BeautifulSoup(response.text, features='html.parser')
  list_of = html_doc.find_all('span')
  print(list_of)
