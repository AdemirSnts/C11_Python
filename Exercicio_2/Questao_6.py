import math

numero = float(input("Digite um número decimal: "))

if numero >= 0:
    print("Raiz quadrada:", math.sqrt(numero))
else:
    print("Não é possível calcular a raiz quadrada real de um numero negativo.")

print("Função teto:", math.ceil(numero))
print("Função chão:", math.floor(numero))
print("Parte inteira:", int(numero))
