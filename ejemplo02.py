from eii_utils import mostrar_menu

lista_nombres:list[str] = ['Diego ',' Jimena','santiago','Giuliana','ALISSA','Arath','Abigail', 'Lizeth', 'Isabella', 'Paula']

def selecionar_estudiante(lista:list[str]) -> str:
    lista_procesada = [  i.strip().capitalize() for i in lista  ]
    lista_procesada.sort()
    print(lista_procesada)
    return ''

if __name__ == '__main__':
    selecionar_estudiante(lista_nombres)