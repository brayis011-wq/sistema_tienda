"""Sistema de inventario y promociones"""

# --- Inventario ---
inventario = {
    "Huevos": [12000, 0],
    "Leche": [4000, 0],
    "Pan": [5000, 0],
    "Arroz": [2500, 0],
    "Papa": [3000, 0],
    "Pasta": [3200, 0],
    "Lentejas": [3000, 0],
    "Frijol": [2700, 0],
}

# --- Promociones ---
promociones = [
    (["Huevos", "Leche", "Pan"], 19999),
    (["Arroz", "Frijol", "Lentejas"], 6500),
    (["Pan", "Pasta", "Arroz"], 9900),
]


def actualizar_stock(producto, cantidad, modo="sumar"):
    if producto not in inventario:
        print(f" {producto} no existe.")
        return
    if modo == "sumar":
        inventario[producto][1] += cantidad
    elif modo == "restar":
        inventario[producto][1] = max(0, inventario[producto][1] - cantidad)
    elif modo == "fijar":
        inventario[producto][1] = cantidad
    print(f"✅ Stock de {producto}: {inventario[producto][1]}")


def actualizar_precio(producto, precio):
    if producto in inventario:
        inventario[producto][0] = precio
        print(f"✅ Precio de {producto}: ${precio:,.0f}")
    else:
        print(f" {producto} no existe.")


def calcular_compra(carrito):
    """carrito = {producto: cantidad}"""
    restante = dict(carrito)
    total = 0

    for productos, precio_combo in promociones:
        veces = min(restante.get(p, 0) for p in productos)
        if veces > 0:
            for p in productos:
                restante[p] -= veces
            total += veces * precio_combo
            print(f"{veces}x Promo [{' + '.join(productos)}] = ${veces*precio_combo:,.0f}")

    for producto, cantidad in restante.items():
        if cantidad > 0 and producto in inventario:
            subtotal = inventario[producto][0] * cantidad
            total += subtotal
            print(f"{cantidad}x {producto} = ${subtotal:,.0f}")

    print(f"TOTAL: ${total:,.0f}")
    return total


