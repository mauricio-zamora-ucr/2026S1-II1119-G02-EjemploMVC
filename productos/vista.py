from eii_utils import mostrar_menu, leer_entero, leer_texto, leer_flotante, leer_booleano

def mostrar_menu_principal() -> int:
    return mostrar_menu('Administración de productos',
    ['Agregar','Modificar','Eliminar','Ver','Listar','Reporte'])

def agregar_producto() -> tuple[str, str, float, int, bool]:
    codigo:str = leer_texto('Código')
    nombre:str = leer_texto('Nombre')
    precio:float = leer_flotante('Precio')
    cantidad:int = leer_entero('Cantidad')
    activo:bool = leer_booleano('¿Esta activo?')
    return codigo, nombre, precio, cantidad, activo