import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.reddit.com/r/programming/"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Página carregada com sucesso!")
else:
    print("Falha ao carregar a página:", response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

teste = soup.find_all("a", class_="absolute inset-0")

# for post in soup.find_all('main', class_='main w-full flex-grid--main-container-card right-sidebar-s'):
for post in soup.find_all('div', class_='col-start-1 col-end-2 row-start-2 row-end-3 overflow-hidden'):
    title_tag = post.find('a', id=lambda x: x and x.startswith('post-title-')) 
    if title_tag:
        title = title_tag.text.strip() 
    else:
        title = "Título não encontrado"

    link_tag = post.find('a', class_=["post-link", "max-w-full", "truncate", "cursor-pointer"])
    if link_tag:
        link = link_tag['href']
    else:
        link = "Link não encontrado"

    likes_tag = post.find('faceplate-number')
    if likes_tag:
        likes = likes_tag['number']
    else:
        likes = "Curtidas não encontradas" 


    print(f'Título: {title}')
    print(f'Link: {link}')
    print(f'Curtidas: {likes_tag}')
    print('---')
