


futebol = ["bolas","cones","coletes"]

futebol.append("cartao")
print(futebol) # ["bolas","cones","coletes","bomba de ar","garrafa de agua"]

futebol.insert(2,"fones")
print(futebol)

futebol.remove("cones")
print(futebol)

futebol.pop(1)
print(futebol)

futebol.sort()
print(futebol)

futebol.reverse()
print(futebol)

dias_da_semana = ("Segunda","Terça","Quarta","Quinta","Sexta")
print(dias_da_semana[3]) # Quinta

pessoa={"nome":"henzo","idade":"16","cidade":"São Paulo"}
print(pessoa["nome"]) # Henzo

print(pessoa["nome"])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get("idade", 10))

pessoa.update({"idade": 17}) 
print(pessoa)  