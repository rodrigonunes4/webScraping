import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

productList = []

search = input("Digite o produto que deseja buscar: ")
search = search.replace(" ", "-")

response = requests.get(f"https://lista.mercadolivre.com.br/{search}")

site = bs(response.content, 'html.parser')

products = site.find_all('div', attrs={'class': 'ui-search-result__content-wrapper'})

for product in products:
    
    productTitle = product.find('a', attrs= {'class': 'ui-search-item__group__element ui-search-link'})
    productPrice = product.find('span', attrs={'class': 'andes-money-amount'})
    productLink = productTitle['href']

    print(f"Título: {productTitle.text}")
    print(f"Preço: {productPrice.text}")
    print(f"Link: {productLink}")
    print("\n\n")

    productList.append([productTitle.text, productPrice.text, productLink])

productDataFrame = pd.DataFrame(productList,columns=['Título','Preço','Link'])
productDataFrame.to_excel('webScraping/05 - Mercado Livre/products.xlsx', index=False)