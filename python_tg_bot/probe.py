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

# formula = (value - 32)/1.8
#  {'class':'wu-value wu-value-to'}
if response.status_code ==200:
  html_doc = BeautifulSoup(response.text, features='html.parser')
  list_of = html_doc.find_all('span', {'class':'wu-value wu-value-to'})
  i=0
  for tag in list_of:
    i+=1
    if i ==2:
      print(tag)
      tag = str(tag)
      value = int(tag[-9:-7])
      gradus = (value - 32)/1.8
      real_gradus = round(gradus, 1)
      print(real_gradus)
      
    