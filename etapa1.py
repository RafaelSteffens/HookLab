import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do Reddit e headers para simular um navegador
url = "https://www.reddit.com/r/programming/"
headers = {'User-Agent': 'Mozilla/5.0'}

# Fazer a solicitação GET para a página
response = requests.get(url, headers=headers)

# Verificar se a página foi carregada com sucesso
if response.status_code == 200:
    print("Página carregada com sucesso!")
else:
    print("Falha ao carregar a página:", response.status_code)

# Criar o objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Listas para armazenar os dados
titles = []
links = []
likes = []

# Iterar pelos posts e coletar os dados
for post in soup.find_all('div', class_='col-start-1 col-end-2 row-start-2 row-end-3 overflow-hidden'):
    
    # Encontrar o título
    title_tag = post.find('a', id=lambda x: x and x.startswith('post-title-')) 
    title = title_tag.text.strip() if title_tag else "Título não encontrado"

    # Encontrar o link
    link_tag = post.find('a', class_=["post-link", "max-w-full", "truncate", "cursor-pointer"])
    link = link_tag['href'] if link_tag else "Link não encontrado"

    # Encontrar o número de curtidas
    likes_tag = post.find('faceplate-number')
    likes = likes_tag['number'] if likes_tag else "Curtidas não encontradas"

    # Adicionar os dados às listas
    titles.append(title)
    links.append(link)
    # likes.append(likes)

# Criar um DataFrame com os dados
data = {
    'Título': titles,
    'Link': links,
    'Curtidas': likes
}
df = pd.DataFrame(data)

# Salvar o DataFrame em um arquivo Excel
df.to_excel('postsReddit.xlsx', index=False, sheet_name='Posts')

print("Dados escritos no arquivo demofile.xlsx com sucesso!")
