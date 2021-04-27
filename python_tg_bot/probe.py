import requests
from bs4 import BeautifulSoup
import json
from os.path import join
import pyvips
import pymysql.cursors


afasf = {}


if afasf['0'] is None:
    print('asdaf')
else:
    print('asdwcx')


# gsdjg = {'asasd': {'user_1': {'asd':5}}}

# # print(gsdjg['asasd'])
# # print(gsdjg['asasd']['user_1'])
# print(*gsdjg['asasd']['user_1'])
# # def rakov(**kwargs):
#     print(kwargs)
#     print(*kwargs)
#     print(**kwargs)
    
# rakov(**kwargs=gsdjg)



# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='19951977',
#                              database='mypythondata',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
# with connection:
#     with connection.cursor() as cursor:
        
#         sql = "INSERT INTO `probe` (`user_email`, `user_password`, `user_state`) VALUES (%s, %s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret', '1'))
#     connection.commit()

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #     cursor.execute(sql, ('webmaster@python.org',))
    #     result = cursor.fetchone()
    #     print(result)
# connecting = pymysql.connect(user = 'root', password = '19951977', database = 'mypythondata')

# with connecting:
#     with connecting.cursor() as cursor:
#         sql = "Show tables"
#         kin = cursor.execute(sql)
#         print(kin)


# connect('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Data\\mypythondata\\registration_info.ibd')

# # target_site = 'www.youtube.com'
# # target_site_str = f'{target_site}'
# # response = requests.get('https://thehost.ua/ua/domains/whois')

# # if response.status_code ==200:
# #   html_doc = BeautifulSoup(response.text, features='html.parser')
# #   list_of = html_doc.find_all('input')
# #   for tag in list_of:
# #     if tag.get(key = 'value') is not None:
# #       tag.attrs['value'] = target_site_str
# # Розпарсив, змінив тег, щоб в ньому був необхідний сайт


# # TODO залити назад, натиснути кнопку пошуку, розпарсити необхідну інфу з отриманої сторінки

#   # for elem in list_of:
#   #   if '<input id="check-inp" name="domain"' in elem:
#   #     elem = f'<input id="check-inp" name="domain" placeholder="введіть ім'я для перевірки" type="text" value="{target_site}"/>'

# target_site = 'www.youtube.com'
# target_site_str = f'{target_site}'
# response = requests.get('https://www.wunderground.com/weather/IKYIV366')

# # formula = (value - 32)/1.8 'd:\\image.svg'
# #  {'class':'wu-value wu-value-to'}
# if response.status_code ==200:
#   html_doc = BeautifulSoup(response.text, features='html.parser')
#   list_of_weather = html_doc.find_all('img', {'alt':'icon'})
#   i = 0
#   for tag in list_of_weather:
#     i+=1
#     if i == 2:
#       link =tag.attrs['src']
#       img = requests.get("http://www.wunderground.com/static/i/c/v4/33.svg")
#       img_file = open('python_tg_bot\\img.svg','wb')
#       img_file.write(img.content)
#       img_file.close()
      
# open(file=join('python_tg_bot','img_2.jpg'))
# import cairosvg
# image_weather_prev = join('python_tg_bot','img.svg')
# image_weather_out = join('python_tg_bot','weather.png')
# cairosvg.svg2png(url=image_weather_prev, write_to=image_weather_out)