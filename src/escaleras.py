"""
Problema 1: Escaleras (Programación Dinámica, enfoque bottom-up).

Cuántas formas hay de llegar al escalón N avanzando 1 o 2 escalones por paso.

Estado DP:
    dp[i] = número de formas distintas de llegar exactamente al escalón i.

Relación de recurrencia:
    dp[i] = dp[i-1] + dp[i-2]      (llegar desde i-1 con 1 paso, o desde i-2 con 2 pasos)

Casos base:
    dp[0] = 1   (una forma de "estar en el suelo": no hacer nada)
    dp[1] = 1   (solo 1 escalón)

Complejidad:
    Tiempo  O(N)
    Espacio O(N) por la tabla (se necesita completa para mostrarla;
            podría reducirse a O(1) guardando solo los dos últimos valores).
"""
import sys


def contar_formas(n):
    """Devuelve (formas, tabla_dp) para una escalera de n escalones."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("N debe ser un entero mayor o igual a 0.")

    # Tabla de tamaño n+1 (índices 0..n); se llena con ceros.
    dp = [0] * (n + 1)

    # Caso base: dp[0] = 1 (siempre existe) y dp[1] = 1 (si n >= 1).
    dp[0] = 1
    if n >= 1:
        dp[1] = 1

    # Llenado bottom-up: cada celda depende de las dos anteriores.
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n], dp


def main():
    # N puede venir como argumento (python escaleras.py 5) o por teclado.
    try:
        texto = sys.argv[1] if len(sys.argv) > 1 else input("Ingrese el número de escalones N: ")
        n = int(texto)
        formas, tabla = contar_formas(n)
    except ValueError as e:
        print(f"Entrada inválida: {e if 'N debe' in str(e) else 'ingrese un entero.'}")
        sys.exit(1)

    print(f"N = {n}")
    print(f"Formas posibles: {formas}")
    print(f"Tabla DP:\n{tabla}")


if __name__ == "__main__":
    main()
