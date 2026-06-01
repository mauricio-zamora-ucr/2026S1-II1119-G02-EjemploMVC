# # ejemplos de colecciones

lista_nombres:list[str] = ['Diego','Jimena','Santiago','Giuliana','Alissa','Arath']

lista_largos:list[int] = []

lista_comprimida_largo:list[int] = [ len(i)  for i in lista_nombres  ]
print('lista_comprimida_largo', lista_comprimida_largo)

for nombre in lista_nombres:
    lista_largos.append(len(nombre))

print(lista_largos)