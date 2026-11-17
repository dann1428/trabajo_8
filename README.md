# Actividad: Programación Dinámica

Dos problemas de optimización resueltos con programación dinámica (bottom-up) en Python 3:

| Problema | Archivo | Complejidad (tiempo / espacio) |
|---|---|---|
| Escaleras (formas de subir N escalones con pasos de 1 o 2) | `src/escaleras.py` | O(N) / O(N) |
| Cambio mínimo de monedas | `src/monedas.py` | O(M·T) / O(T) |

## Requisitos
Python 3.8 o superior. No hay dependencias externas.

## Ejecución

```bash
# Escaleras: argumento o entrada por teclado
python3 src/escaleras.py 5
python3 src/escaleras.py            # pregunta N

# Monedas: lista de monedas y cantidad objetivo
python3 src/monedas.py "1,3,4" 6
python3 src/monedas.py              # pregunta monedas y cantidad
```

Salida de ejemplo (`monedas.py "1,3,4" 6`):

```
Cantidad mínima de monedas: 2
Combinación: 3 + 3
Tabla DP (-1 = imposible):
[0, 1, 2, 1, 1, 2, 2]
```

En la tabla de monedas, `-1` indica un monto que no se puede formar con las denominaciones dadas.

## Pruebas
```bash
python3 -m unittest discover tests -v
```
Las pruebas comparan la solución DP con los ejemplos del enunciado y con verificaciones por fuerza bruta.

## Documentación
El informe (algoritmo, estado, recurrencia, casos base, complejidad y capturas) está en `docs/Informe_Programacion_Dinamica.pdf`.
