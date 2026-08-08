nome = input("Nome: ")
print("Meu nome em letras maiusculas: ", nome.upper())
print("Meu nome em letras minusculas: ", nome.lower())

Quant_letras = len(nome.replace(" ", " "))
print("Quantidade total de letras: ", Quant_letras)
print("\nSubstituindo")
print(nome.replace('Nogueira','do Inatel'))
