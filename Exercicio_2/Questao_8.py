numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

adicao = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

print("\nAdicao:", adicao)
print("Subtracao:", subtracao)
print("Multiplicacao:", multiplicacao)

if numero2 != 0:
    print("Divisao:", numero1 / numero2)
    print("Resto da divisao:", numero1 % numero2)
else:
    print("Divisao: nao e possível dividir por zero.")
    print("Resto da divisao: não e possível dividir por zero.")

print("Potencia:", numero1 ** numero2)

if adicao % 2 == 0:
    print("O resultado da adicao é par.")
else:
    print("O resultado da adicao é ímpar.")