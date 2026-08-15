produtos = []

for i in range(3):
    print(f"\nProduto {i + 1}")

    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

print("\nValor total em estoque de cada produto:")

for produto in produtos:
    valor_total = produto["preco"] * produto["quantidade"]

    print(
        f"{produto['nome']}: "
        f"R$ {valor_total:.2f}"
    )
