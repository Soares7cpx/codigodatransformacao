a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b if b != 0 else "Divisão por zero não permitida")
print("Resto da divisão:", a % b if b != 0 else "Divisão por zero não permitida")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é {num1}")
elif num2 > num1:
    print(f"O maior número é {num2}")
else:
    print("Os dois números são iguais")

idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Você é uma Criança")
elif idade < 18:
    print("Você é um Adolescente")
elif idade < 60:
    print("Você é um Adulto")
else:
    print("Você é um Idoso")

while True:
    print("\nMenu:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado da Soma:", n1 + n2)
    elif opcao == "2":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado da Subtração:", n1 - n2)
    elif opcao == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
