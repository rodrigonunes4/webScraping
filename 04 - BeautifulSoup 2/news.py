import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

newsList = []

response = requests.get("https://g1.globo.com/")

content = response.content    #Conteúdo

site = bs(content, 'html.parser')

news = site.find_all('div', attrs={'class': 'feed-post-body'})

for i in news:

    newsTitle = i.find('a', attrs={'class': 'feed-post-link'})
    newsLink = newsTitle['href']

    print(f"Título: {newsTitle.text}")
    print(f"Link: {newsLink}")

    try:
        newsBulletPoints = i.find_all('a', attrs={'class': 'bstn-relatedtext'})
        print(f"Bullet-points: {' <---> '.join(j.text for j in newsBulletPoints)}")
    except:
        pass

    try:
        newsResumo = i.find('div', attrs={'class': 'feed-post-body-resumo'})
        print(f"Resumo: {newsResumo.text}")
    except:
        pass
    
    if newsResumo:
        newsList.append([newsTitle.text, newsResumo.text, newsLink])
    else:
        newsList.append([newsTitle.text, '', newsLink])

    print("\n")

newsDataFrame = pd.DataFrame(newsList, columns=['Título','Resumo','Link'])
newsDataFrame.to_excel('news.xlsx', index=False)

#print(newsDataFrame)