import requests
from bs4 import BeautifulSoup

# 1. Fazer uma solicitação HTTP para a página da web
url = 'https://averdade.org.br/'
response = requests.get(url)

# 2. Verificar se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # 3. Analisar o conteúdo HTML da página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # 4. Encontrar os elementos da página que você deseja extrair
    # Por exemplo, para encontrar todos os links na página:
    links = soup.find_all('a')

    # 5. Iterar pelos elementos encontrados e extrair os dados desejados
    for link in links:
        # Extrair o texto do link
        link_text = link.get_text()
        
        # Extrair o URL do link
        link_url = link.get('href')

        # 6. Processar os dados ou salvá-los em um arquivo
        # Por exemplo, imprimir os dados ou salvar em um arquivo CSV
        print(f"Texto do link: {link_text}")
        print(f"URL do link: {link_url}")
        
else:
    print(f"A solicitação falhou com o código de status: {response.status_code}")
