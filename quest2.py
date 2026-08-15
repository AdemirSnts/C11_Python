loja_1 = {'Samsung A15', 'Xiaomi', 'Motorola M16'}
loja_2 = {'Iphone 7', 'Redmi Note 17', 'Samsung S50','Xiaomi'}

print("Primeira loja: ",loja_1)
print("Segunda loja: ", loja_2)

Lojas = loja_1|loja_2
modelos_nas_duas = loja_1 & loja_2

print("Aparelhos disponiveis no total: ")
print(Lojas)
print("Aparelhos disponiveis em ambas as lojas: ")
print(modelos_nas_duas)

