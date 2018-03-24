from pip._vendor import requests

main_page = requests.get('https://114.by/')
assert main_page.status_code == 200
print (main_page.status_code)

kak = requests.get('https://114.by/item/kak-polzovatsia-servisom/')
assert kak.status_code == 200
print (kak.status_code)

kontakt = requests.get('https://114.by/item/kontakty/')
assert kontakt.status_code == 200
print (kontakt.status_code)

route = requests.get('https://114.by/bus/route/gorodok-as/vyshedki/')
assert route.status_code == 200
print (route.status_code)

route = requests.get('https://114.by/bus/route/minsk-as-druzhnaja/molodechno-av/')
assert route.status_code == 404
print (route.status_code)

route = requests.get('https://114.by/bus/route/grodno-av/belostok-av-pks/')
assert route.status_code == 404
print (route.status_code)

route = requests.get('https://114.by/bus/route/14-j-km/bajdino-2-oe/')
assert route.status_code == 404
print (route.status_code)