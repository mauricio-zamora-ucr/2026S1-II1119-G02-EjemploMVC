from principal.vista import mostrar_menu_principal
from eii_utils import limpiar_consola, pausar

def iniciar_aplicacion() -> None:
    opcion:int = -1

    while opcion != 0:
        limpiar_consola()
        opcion = mostrar_menu_principal()
        match opcion:
            case 1:
                print('Ver producto')
                pausar()
            case 2:
                print('ver clientes')
                pausar()
            case 0:
                print('Hasta la vista, Baby!')
                pausar()

