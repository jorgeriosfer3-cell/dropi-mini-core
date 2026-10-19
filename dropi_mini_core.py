
# ============================================================
# PROYECTO: DROPi MINI CORE
# Simulador de pedidos, logística, liquidación y marketing con IA
# Autor: Aprendiz de Desarrollo de Software
# Lenguaje: Python
# ============================================================

from datetime import datetime


# ------------------------------------------------------------
# 1. PEDIDO SIMULADO
# Representa la información de un pedido entrante.
# ------------------------------------------------------------

pedido = {
    "id_pedido": "DRP-2026-001",
    "producto": "Audifonos Bluetooth Pro",
    "precio_producto": 120000,
    "ciudad_destino": "Medellin",
    "metodo_pago": "Contra Entrega"
}


# ------------------------------------------------------------
# 2. LOGICA LOGISTICA
# Determina el costo del envio segun la ciudad de destino.
# ------------------------------------------------------------

def calcular_envio(ciudad):
    """Retorna el costo de envio en pesos colombianos."""

    ciudad = ciudad.strip().lower()

    if ciudad in ("cali", "bogota", "bogotá"):
        return 10000
    else:
        return 15000


# ------------------------------------------------------------
# 3. LIQUIDACION DE LA BILLETERA
# Calcula el valor neto despues de descontar el envio.
# ------------------------------------------------------------

def liquidar_billetera(pedido, costo_envio):
    """
    Simula el recaudo contra entrega y calcula el neto.
    En este prototipo, el envio es el unico descuento.
    """

    precio_producto = pedido["precio_producto"]
    ganancia_neta = precio_producto - costo_envio

    return ganancia_neta


# ------------------------------------------------------------
# 4. MENSAJE COMERCIAL SIMULADO CON IA
# Genera un mensaje persuasivo de maximo 30 palabras.
#
# NOTA: Esta version usa una plantilla dinamica.
# No se conecta realmente a un modelo de lenguaje.
# ------------------------------------------------------------

def generar_mensaje_ia(pedido):
    """Construye un mensaje comercial usando el producto."""

    producto = pedido["producto"]

    mensaje = (
        f"¡Hola! Descubre {producto} y disfruta una excelente "
        "opcion para ti. Confirma tu pedido hoy y recibe tu "
        "producto en la puerta de tu casa. ¡Te esperamos!"
    )

    # Garantiza un maximo de 30 palabras.
    palabras = mensaje.split()
    mensaje = " ".join(palabras[:30])

    return mensaje


# ------------------------------------------------------------
# 5. FORMATO DE DINERO
# Presenta los valores como pesos colombianos.
# ------------------------------------------------------------

def formato_cop(valor):
    return f"${valor:,.0f}".replace(",", ".")


# ------------------------------------------------------------
# 6. REPORTE FINAL
# Presenta el resultado de forma organizada en la terminal.
# ------------------------------------------------------------

def imprimir_ticket(pedido, costo_envio, ganancia_neta, mensaje):
    separador = "=" * 58

    print("\n" + separador)
    print("          DROPi | MINI CORE DE OPERACIONES")
    print("             SIMULADOR DE LIQUIDACION")
    print(separador)

    print(f"Fecha de ejecucion : {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"ID del pedido      : {pedido['id_pedido']}")
    print(f"Producto           : {pedido['producto']}")
    print(f"Ciudad destino     : {pedido['ciudad_destino']}")
    print(f"Metodo de pago     : {pedido['metodo_pago']}")

    print("-" * 58)
    print("DESGLOSE ECONOMICO")
    print("-" * 58)

    print(f"Precio del producto: {formato_cop(pedido['precio_producto'])}")
    print(f"Costo del envio    : {formato_cop(costo_envio)}")
    print("-" * 58)
    print(f"NETO SIMULADO WALLET: {formato_cop(ganancia_neta)}")

    print("-" * 58)
    print("MENSAJE COMERCIAL SUGERIDO")
    print("-" * 58)
    print(mensaje)
    print(f"\nTotal de palabras: {len(mensaje.split())}")

    print("-" * 58)
    print("ESTADO: SIMULACION COMPLETADA")
    print("Nota: no se realizo ningun recaudo ni abono real.")
    print(separador + "\n")


# ------------------------------------------------------------
# 7. EJECUCION PRINCIPAL
# Coordina las funciones anteriores.
# ------------------------------------------------------------

def main():
    costo_envio = calcular_envio(pedido["ciudad_destino"])

    ganancia_neta = liquidar_billetera(
        pedido,
        costo_envio
    )

    mensaje = generar_mensaje_ia(pedido)

    imprimir_ticket(
        pedido,
        costo_envio,
        ganancia_neta,
        mensaje
    )


# Ejecuta el programa solo cuando se inicia este archivo.
if __name__ == "__main__":
    main()
