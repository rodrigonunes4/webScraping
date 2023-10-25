import requests
from bs4 import BeautifulSoup as bs

response = requests.get("https://g1.globo.com/")

content = response.content    #Conteúdo

site = bs(content, 'html.parser')

news = site.find_all('div', attrs={'class': 'feed-post-body'})

for i in news:

    newsTitle = i.find('a', attrs={'class': 'feed-post-link'})
    print(f"Título: {newsTitle.text}")

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
    
    print("\n")