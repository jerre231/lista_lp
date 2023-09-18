h = float(input("digite a altura: "))
opc = input("homem ou mulher: h/m? ")

if opc == "h":
    peso = round(((72.7*h) - 58), 2)

elif opc == "m":
    peso = round(((62.1*h) - 44.7), 2)

else:
    print("opção invalida")
    exit()

print(f"O peso ideal é de {peso}")