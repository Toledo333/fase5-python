# Matriz de inventario
inventario = [
    ["A001", "Teclado", 5, 10],
    ["A002", "Mouse", 12, 10],
    ["A003", "Monitor", 3, 8],
    ["A004", "USB", 15, 10],
    ["A005", "Audifonos", 2, 6]
]

# Función para calcular pedido
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Mostrar resultados
print("LISTA DE REABASTECIMIENTO")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print(nombre, "-> Pedir:", cantidad_pedir)

