pessoas = []

for i in range(3):
    print(f"\nPessoa {i + 1}")
    nome = input("Nome: ")
    peso = float(input("Peso (kg): "))

    pessoa = {
        "nome": nome,
        "peso": peso
    }

    pessoas.append(pessoa)

mais_pesada = max(pessoas, key=lambda pessoa: pessoa["peso"])
mais_leve = min(pessoas, key=lambda pessoa: pessoa["peso"])

print("\nPessoa mais pesada:", mais_pesada["nome"],
      f"({mais_pesada['peso']:.1f} kg)")
print("Pessoa mais leve:", mais_leve["nome"],
      f"({mais_leve['peso']:.1f} kg)")