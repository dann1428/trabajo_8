"""
Problema 2: Cambio mínimo de monedas (Programación Dinámica, bottom-up).

Dado un conjunto de denominaciones (cantidad ilimitada de cada una) y un monto
objetivo, hallar el mínimo de monedas necesarias y una combinación válida.

Estado DP:
    dp[x] = mínimo de monedas necesarias para formar exactamente el monto x.
    ultima[x] = última moneda usada en la solución óptima de x
                (sirve para reconstruir la combinación).

Relación de recurrencia:
    dp[x] = min( dp[x - c] + 1 )   para cada moneda c <= x con dp[x - c] alcanzable

Casos base:
    dp[0] = 0        (monto 0 no requiere monedas)
    dp[x] = INF      inicialmente (aún no se sabe si x es alcanzable)
    Si dp[objetivo] sigue siendo INF, no existe combinación (resultado -1).

Complejidad (M = nº de monedas, T = monto objetivo):
    Tiempo  O(M * T)
    Espacio O(T)
"""
import sys

INF = float("inf")


def cambio_minimo(monedas, objetivo):
    """Devuelve (minimo, combinacion, tabla_dp). Si es imposible: (-1, [], tabla)."""
    if objetivo < 0:
        raise ValueError("La cantidad objetivo debe ser >= 0.")
    # Se ignoran duplicados; las monedas deben ser enteros positivos.
    monedas = sorted(set(monedas))
    if any((not isinstance(c, int)) or c <= 0 for c in monedas):
        raise ValueError("Las monedas deben ser enteros positivos.")

    dp = [INF] * (objetivo + 1)
    ultima = [0] * (objetivo + 1)   # moneda usada para llegar a cada monto
    dp[0] = 0                       # caso base

    for x in range(1, objetivo + 1):
        for c in monedas:
            if c > x:
                break               # monedas ordenadas: las siguientes tampoco caben
            if dp[x - c] + 1 < dp[x]:
                dp[x] = dp[x - c] + 1
                ultima[x] = c

    if dp[objetivo] == INF:
        return -1, [], [(-1 if v == INF else v) for v in dp]

    # Reconstrucción: retroceder desde el objetivo restando la moneda usada.
    combinacion, x = [], objetivo
    while x > 0:
        combinacion.append(ultima[x])
        x -= ultima[x]
    combinacion.sort(reverse=True)

    tabla = [(-1 if v == INF else v) for v in dp]   # -1 = monto imposible
    return dp[objetivo], combinacion, tabla


def leer_lista(texto):
    """Convierte '1,3,4' o '[1, 3, 4]' o '1 3 4' en [1, 3, 4]."""
    limpio = texto.replace("[", " ").replace("]", " ").replace(",", " ")
    return [int(t) for t in limpio.split()]


def main():
    try:
        if len(sys.argv) >= 3:
            monedas, objetivo = leer_lista(sys.argv[1]), int(sys.argv[2])
        else:
            monedas = leer_lista(input("Ingrese las monedas (ej. 1,3,4): "))
            objetivo = int(input("Ingrese la cantidad objetivo: "))
        if not monedas:
            raise ValueError("Debe ingresar al menos una moneda.")
        minimo, comb, tabla = cambio_minimo(monedas, objetivo)
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        sys.exit(1)

    print(f"Monedas: {monedas}")
    print(f"Cantidad: {objetivo}")
    if minimo == -1:
        print("Cantidad mínima de monedas: imposible formar el monto exacto")
    else:
        print(f"Cantidad mínima de monedas: {minimo}")
        print(f"Combinación: {' + '.join(map(str, comb)) if comb else '(ninguna)'}")
    print(f"Tabla DP (-1 = imposible):\n{tabla}")


if __name__ == "__main__":
    main()
