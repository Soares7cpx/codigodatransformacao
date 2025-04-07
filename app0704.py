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
nome= input('Qual é o seu nome? ')
agora = datetime.now()
hora_atual = agora.strftime('%H:%M')
print(f'{nome}! Agora são {hora_atual}')
print(f'Qual seria o seu desejo {nome}?')
print('Segue alguns links para sua duvida')

a = 10
b = 5
resultado = a > b
print(resultado) #True

x = 10
y = 5
print(x > 5 and y < 10) # True
print(x > 5 or y > 10) # True
print(not(x > 5)) # False


