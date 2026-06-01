from typing import TypedDict


class Producto(TypedDict):
    codigo: str
    nombre: str
    precio: float
    cantidad: int
    activo: bool


# este diccionario no debería de ser accedido directamente
# solo a través de funciones, para la seguridad de los datos
_productos: dict[str:Producto] = {}


def existe_producto(codigo: str) -> bool:
    producto = _productos.get(codigo)
    return producto is not None


def agregar_producto(
    codigo: str, nombre: str, precio: float, cantidad: int = 0, activo: bool = True
) -> tuple[bool, str]:
    if not existe_producto(codigo):
        producto:Producto = {}
        producto['codigo'] = codigo
        producto['nombre'] = nombre
        producto['cantidad'] = cantidad
        producto['precio'] = precio
        producto['activo'] = activo
        _productos[codigo] = producto
        return True, 'Producto registrado'
    else:
        return False, 'No se pudo agregar producto'


def listar_todos_productos() -> list[Producto]:
    return list( _productos.values() )


if __name__ == '__main__':
    print(agregar_producto('7441234','Galleta Chocko',1000,85))
    print(agregar_producto('7441235','Galleta Chocko Grande',2000,66))
    print(agregar_producto('7441234','Jugo Chocko',1000,85))
    print(listar_todos_productos())