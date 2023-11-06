import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Fazer uma solicitação HTTP para a página da web
url = 'https://averdade.org.br/'
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Analisar o conteúdo HTML da página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar os elementos HTML que contêm as notícias
    news_items = soup.find_all('div', class_='td-module-container')

    # Criar uma lista para armazenar os dados das notícias
    news_data = []

    # Iterar pelos elementos das notícias
    for news_item in news_items:
        # Extrair o título da notícia
        title = news_item.find('h3', class_='entry-title').text

        # Extrair a data da notícia
        date_str = news_item.find('time', class_='entry-date').get('datetime')
        # Converter a data para um objeto datetime
        news_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')

        # Adicionar os dados da notícia à lista
        news_data.append({'title': title, 'date': news_date})

    # Ordenar as notícias pelo mais recente
    sorted_news = sorted(news_data, key=lambda x: x['date'], reverse=True)

    # Criar um arquivo txt para escrever os dados da notícia
    with open('news_data.txt', 'w', encoding='utf-8') as file:
        # Iterar pelas notícias ordenadas e escrever os dados no arquivo
        for news in sorted_news:
            file.write(f"Data da notícia: {news['date']}\n")
            file.write(f"Título da notícia: {news['title']}\n")
            file.write("\n")

    # Mensagem de confirmação
    print("Dados das notícias foram gravados com sucesso em news_data.txt")

else:
    print(f"A solicitação falhou com o código de status: {response.status_code}")
