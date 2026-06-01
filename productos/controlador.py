from eii_utils import limpiar_consola, imprimir_mensaje, imprimir_advertencia, imprimir_error, pausar
import productos.vista as vista
import productos.modelo as modelo

from eii_utils import limpiar_consola, pausar

def iniciar_procesamiento_producto() -> None:
    opcion:int = -1

    while opcion != 0:
        limpiar_consola()
        opcion = vista.mostrar_menu_principal()
        match opcion:
            case 1:
                agregar_producto()
                
            case 2:
                print('ver clientes')
                pausar()
            case 0:
                print('Hasta la vista, Baby!')
                pausar()

def agregar_producto() -> None:
    limpiar_consola()
    codigo, nombre, precio, cantidad, activo = vista.agregar_info_producto()
    #limpio el codigo, lo convierto en mayusculas y ademas le quito los espacio
    codigo = codigo.strip().upper()
    nombre = nombre.strip()
    estado, mensaje = modelo.agregar_producto(codigo, nombre, precio, cantidad, activo)
    if estado:
        imprimir_mensaje('Producto registrado')
    else:
        imprimir_error(mensaje)
    pausar()
