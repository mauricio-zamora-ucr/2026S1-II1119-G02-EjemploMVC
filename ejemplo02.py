from eii_utils import mostrar_menu
from typing import TypedDict

class Estudiante(TypedDict):
    carne:str
    nombre:str
    edad:int
    lugar:str

lista_nueva:list[Estudiante] = []
s1:Estudiante = {}
s1['nombre'] = 'Ligia'


lista_nombres:list[str] = ['Diego ',' Jimena','santiago','Giuliana','ALISSA','Arath','Abigail', 'Lizeth', 'Isabella', 'Paula']

lista_estudiante:list[dict[str, str]] = []
e1 = {'nombre':'Jimena', 'carne':'a', 'lugar':'Cartago'}
lista_estudiante.append(e1)
e2 = {'nombre':'Ariadna', 'carne':'b', 'lugar':'Heredia'}
lista_estudiante.append(e2)
e3 = {'nombre':'Arath', 'carne':'c', 'lugar':'San Jose'}
lista_estudiante.append(e3)

def selecionar_estudiante(lista:list[str]) -> str:
    lista_procesada = [  i.strip().capitalize() for i in lista  ]
    lista_procesada.sort()
    opcion:int = mostrar_menu('Seleccione estudiante',lista_procesada,'Ninguno')
    if opcion == 0:
        return None
    return lista_procesada[opcion-1]

if __name__ == '__main__':
    #print(selecionar_estudiante(lista_nombres))
    print(lista_estudiante)
    for i in lista_estudiante:
        print(i['lugar'], i['nombre'])