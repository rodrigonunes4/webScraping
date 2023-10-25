import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

list = []

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
response = requests.get("https://statusinvest.com.br/indices/indice-dividendos", headers=headers)

site = bs(response.content, 'html.parser')

ativos = site.find('input', attrs={'id': 'ativos'})

ativos = eval(ativos['value'])

for ativo in ativos:
    codigo = ativo['Ticker']

    response = requests.get(f'https://statusinvest.com.br/acoes/{codigo}', headers=headers)
    site = bs(response.content, 'html.parser')

    info = site.find_all('strong', attrs='value')
    
    preco = info[0].text
    dividendYield = info[3].text
    
    percentual = ativo['Percentual']
    setorAtuacao = ativo['Setor_Atuacao']
    subsetorAtuacao = ativo['Subsetor_Atuacao']
    segmentoAtuacao = ativo['Segmento_Atuacao']

    list.append([percentual, codigo, preco, dividendYield, setorAtuacao, subsetorAtuacao, segmentoAtuacao])

    print(f"{ativos.index(ativo)/len(ativos)*100:.2f}%") # Porcentagem de conclusão

ativosDataFrame = pd.DataFrame(list, columns = ['Percentual', 'Código', 'Preço', 'DividendYield', 'Setor de Atuação', 'Subsetor de Atuação', 'Segmento de Atuação'])
ativosDataFrame.to_excel('webScraping/mapaDeAtivos/ativos.xlsx', index = False)