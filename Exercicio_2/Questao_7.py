palavra = input("Digite uma palavra: ")

print("\nLetras:")
for letra in palavra:
    print(letra.upper())

vogais = "aeiouáéíóúâêîôûãõà"
quantidade_vogais = sum(1 for letra in palavra.lower() if letra in vogais)

print("Quantidade de vogais:", quantidade_vogais)

if "a" in palavra.lower():
    print('A letra "a" esta presente.')
else:
    print('A letra "a" não esta presente.')