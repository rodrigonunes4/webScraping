import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import time

startRequest = time.perf_counter()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
payload = {'ticker': 'PETR4', 'type': 1, 'currences[]': 1}
response = requests.post('https://statusinvest.com.br/acao/tickerprice', headers=headers, data=payload)

endRequest = time.perf_counter()
timeRequest = endRequest - startRequest



codeTimeStart = time.perf_counter()

dados = eval(response.content)
priceList = []

for dado in dados:
    dados = dado['prices']

for dado in dados:
    priceList.append(dado['price'])

print(priceList)

codeTimeEnd = time.perf_counter()
timeCode = codeTimeEnd - codeTimeStart

print(f'Tempo de requisição: {timeRequest:.5f}')
print(f'Tempo de execução do código: {timeCode:.5f}')

plt.plot(priceList)
plt.show()