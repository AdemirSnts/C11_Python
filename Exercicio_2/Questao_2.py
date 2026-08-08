num = int(input("Digite um numero da tabuada: "))
inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim do intervalo: "))

print(f"\nTabuada do {num}:")
for i in range(inicio, fim + 1):
    print(f"{num} x {i} = {num * i}")
