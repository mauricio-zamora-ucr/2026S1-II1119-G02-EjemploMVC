from eii_utils import limpiar_consola, imprimir_mensaje, imprimir_advertencia, imprimir_error, pausar
import productos.vista as vista
import productos.modelo as modelo

def agregar_producto() -> None:
    limpiar_consola()
    codigo, nombre, precio, cantidad, activo = vista.agregar_info_producto()
    #limpio el codigo, lo convierto en mayusculas y ademas le quito los espacio
    codigo = codigo.strip().upper()
    estado, mensaje = modelo.agregar_producto(codigo, nombre, precio, cantidad, activo)
    if estado:
        imprimir_mensaje('Producto registrado')
    else:
        imprimir_error(mensaje)
    pausar()
