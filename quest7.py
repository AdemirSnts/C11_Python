ingredientes_receita = {
    "farinha de trigo",
    "açucar",
    "ovos",
    "leite",
    "manteiga",
    "fermento",
    "chocolate em pó",
    "granulado"
}

pessoa1 = {
    "farinha de trigo",
    "açucar",
    "ovos",
    "leite"
}

pessoa2 = {
    "manteiga",
    "fermento"
}

disponiveis = pessoa1 | pessoa2
faltam_comprar = ingredientes_receita - disponiveis

print("Ingredientes da receita:", ingredientes_receita)
print("Ingredientes da primeira pessoa: ", pessoa1)
print("Ingredientes da segunda pessoa:", pessoa2)
print("Ingredientes disponiveis:", disponiveis)
print("Ingredientes que faltam comprar:", faltam_comprar)

