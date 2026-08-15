times = ['Real Madrid', 'Barcelona', 'Sporting', 'Manchester city','Zenit', 'Arsenal', 'PSG']
print("Primeiros colocados:")
print(times[:3])
print("\nUltimos colocados:")
print(times[-2:])
print("\nOrdem crescente:")
times.sort()
print(times)
print("Posicao do Barcelona")
if "Barcelona" in times:
    print("Esta na posicao: ", times.index("Barcelona"))
else:
    print("Nao tem esse time na lista!")


