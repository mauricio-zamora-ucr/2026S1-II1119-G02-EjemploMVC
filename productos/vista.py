from eii_utils import mostrar_menu

def mostrar_menu_principal() -> int:
    return mostrar_menu('Administración de productos',
    ['Agregar','Modificar','Eliminar','Ver','Listar','Reporte'])