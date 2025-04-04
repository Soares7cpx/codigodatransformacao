print("Olá Mundo")
print("Corinthians sem tradição na liberta")
print("Messi melhor que CR7")

caixa= 'celular'
print("caixa")

nome= 'Henzo'
idade= 16
altura= 1,73
estudante= True
print(nome, idade, altura, estudante)

mensagem= 'TeLeViSaO'
print(mensagem.strip())
print(mensagem.upper())
print(mensagem.lower())

nome=input('Qual é o seu nome? ')
print(f'Olá {nome}, Seja muito bem vindo ao codigo da transformação')
from datetime import datetime
nome= input('Qual é o seu nome?')
agora = datetime.now()
hora_atual = agora.strftime('%H:%M')
print(f'{nome}! Agora são {hora_atual}')
