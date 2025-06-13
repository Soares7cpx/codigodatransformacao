import requests

chave_api = "4e0ce3bbb51c0e8937aac336d27e0d89"
cidade = "São Paulo"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados["main"]["temp"]
    clima = dados["weather"][0]["description"]
    print(f"Temperatura em {cidade}: {temperatura}°C")
    print(f"Condição: {clima}")
else:
    print(f"Erro: {resposta.status_code}")