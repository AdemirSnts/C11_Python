distancia = float(input("Entre com a distancia da viagem em Km: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"Preco da passagem: R$ {preco:.2f}")