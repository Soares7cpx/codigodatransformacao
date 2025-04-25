for i in range(10):
    print(f"Interação{i}")
print("_____________________________________________________________")
contador=0
while contador<10:
    contador+=1
    print(f"Contador:{contador}")
print("______________________________________________________________________________")

for i in range(10):
    if i == 5:
        break
    print(i)