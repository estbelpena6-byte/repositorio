import requests
from bs4 import BeautifulSoup


website = 'https://pelisflix1.wiki/serie/jujutsu-kaisen/'
result = requests.get(website)
texto = result.text

soup = BeautifulSoup(texto, 'lxml')
#print(soup.prettify())

box = soup.find('div', class_= 'TPMvCn')

title = box.find('h1').get_text()

Description = box.find('div', class_='Description').get_text()


with open(f"{title}.txt", "w") as file:
    file.write(Description)

