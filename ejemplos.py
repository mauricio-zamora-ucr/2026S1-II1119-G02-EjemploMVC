# # ejemplos de colecciones

lista_nombres:list[str] = ['Diego','Jimena','Santiago','Giuliana','Alissa','Arath']

lista_largos:list[int] = []

lista_comprimida_largo:list[int] = [ len(i)  for i in lista_nombres  ]
print('lista_comprimida_largo', lista_comprimida_largo)

for nombre in lista_nombres:
    lista_largos.append(len(nombre))

print(lista_largos)

lista_largo_nombre = list( zip(lista_nombres,lista_largos) )
print(lista_largo_nombre)

def extrae_largo(x):
    return x[1]

#lista_largo_nombre.sort(key=extrae_largo)

lista_largo_nombre.sort(key=lambda x: x[1])

largo = max(lista_largos)
print(largo)

print(lista_largo_nombre)

def filtrar_largo(tupla):
    return extrae_largo(tupla) == 8

los_mas_largos = list(filter(filtrar_largo, lista_largo_nombre))
print(los_mas_largos)