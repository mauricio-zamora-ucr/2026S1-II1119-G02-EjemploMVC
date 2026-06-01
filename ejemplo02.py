from eii_utils import mostrar_menu

lista_nombres:list[str] = ['Diego ',' Jimena','santiago','Giuliana','ALISSA','Arath','Abigail', 'Lizeth', 'Isabella', 'Paula']

def selecionar_estudiante(lista:list[str]) -> str:
    lista_procesada = [  i.strip().capitalize() for i in lista  ]
    lista_procesada.sort()
    opcion:int = mostrar_menu('Seleccione estudiante',lista_procesada,'Ninguno')
    if opcion == 0:
        return None
    return lista_procesada[opcion-1]

if __name__ == '__main__':
    print(selecionar_estudiante(lista_nombres))