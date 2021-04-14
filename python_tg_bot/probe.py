import requests
from bs4 import BeautifulSoup
import json



# target_site = 'www.youtube.com'
# target_site_str = f'{target_site}'
# response = requests.get('https://thehost.ua/ua/domains/whois')

# if response.status_code ==200:
#   html_doc = BeautifulSoup(response.text, features='html.parser')
#   list_of = html_doc.find_all('input')
#   for tag in list_of:
#     if tag.get(key = 'value') is not None:
#       tag.attrs['value'] = target_site_str
# Розпарсив, змінив тег, щоб в ньому був необхідний сайт


# TODO залити назад, натиснути кнопку пошуку, розпарсити необхідну інфу з отриманої сторінки

  # for elem in list_of:
  #   if '<input id="check-inp" name="domain"' in elem:
  #     elem = f'<input id="check-inp" name="domain" placeholder="введіть ім'я для перевірки" type="text" value="{target_site}"/>'

target_site = 'www.youtube.com'
target_site_str = f'{target_site}'
response = requests.get('https://www.wunderground.com/weather/IKYIV366')

# formula = (value - 32)/1.8 'd:\\image.svg'
#  {'class':'wu-value wu-value-to'}
if response.status_code ==200:
  html_doc = BeautifulSoup(response.text, features='html.parser')
  list_of_weather = html_doc.find_all('img', {'alt':'icon'})
  i = 0
  for tag in list_of_weather:
    i+=1
    if i == 2:
      link =tag.attrs['src']
      img = requests.get("http://www.wunderground.com/static/i/c/v4/33.svg")
      img_file = open('python_tg_bot\\img.svg','wb')
      img_file.write(img.content)
      img_file.close()
      
    