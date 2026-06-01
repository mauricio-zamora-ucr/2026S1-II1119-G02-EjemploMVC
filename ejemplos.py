# # ejemplos de colecciones

lista_nombres:list[str] = ['Diego','Jimena','Santiago','Giuliana','Alissa','Arath']

lista_largos:list[int] = []

lista_comprimida_largo:list[int] = [ len(i)  for i in lista_nombres  ]
print('lista_comprimida_largo', lista_comprimida_largo)

for nombre in lista_nombres:
    lista_largos.append(len(nombre))

print(lista_largos)

lista_largo_nombre = list( zip(lista_largos, lista_nombres) )
print(lista_largo_nombre)

def extrae_largo(x):
    return x[0]

for x in lista_largo_nombre:
    print(extrae_largo(x))