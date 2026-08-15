ingredientes = [
    "farinha de trigo",
    "açucar",
    "ovos",
    "leite",
    "manteiga"
]

print("Lista inicial:", ingredientes)

novo_ingrediente = input("Digite um novo ingrediente: ")
ingredientes.append(novo_ingrediente)

print("Lista final de ingredientes:", ingredientes)

ingrediente_inserido = input("Insira um novo ingrediente: ")
posicao = int(input(f"Digite a posição para inserir (0 a {len(ingredientes)}): "))

if 0 <= posicao <= len(ingredientes):
    ingredientes.insert(posicao, ingrediente_inserido)
else:
    print("O ingrediente não foi inserido.")

print("Lista atual:", ingredientes)

ingrediente_remover = input("Digite o ingrediente que sera removido: ")

if ingrediente_remover in ingredientes:
    ingredientes.remove(ingrediente_remover)
    print("Ingrediente removido com sucesso.")
else:
    print("Ingrediente não encontrado.")

print("Lista final:", ingredientes)
