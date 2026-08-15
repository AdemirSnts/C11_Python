x = int(input("Quantas pessoas serao cadastradas? "))

soma_idades = 0
mulheres = 0

for i in range(x):
    print(f"\nPessoa {i + 1}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    soma_idades += idade

    if sexo == "F" and idade < 20:
        mulheres += 1

if x > 0:
    media_idades = soma_idades / x
    print("\nMedia de idade do grupo:", f"{media_idades:.2f}")
    print("Quantidade de mulheres com menos de 20 anos:", mulheres)
else:
    print("Nenhuma pessoa foi cadastrada.")
