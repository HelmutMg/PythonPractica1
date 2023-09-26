
listaColor = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

resultados = [listaColor[i] for i in range(len(listaColor)) if i not in [0, 4, 5]]

print(resultados)
