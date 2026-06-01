from typing import TypedDict

class Producto(TypedDict):
    codigo:str
    nombre:str
    precio:float
    cantidad:int
    activo:bool

