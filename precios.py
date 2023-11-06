#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
from functools import reduce as rd
import itertools

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(itertools.islice(iterable, n, None), default)

estructura = lambda datos: {'nombre': datos.pop(0), 'precios': np.array(datos, dtype=int)}
# Estructura(lista) nos da la lista como diccionario

carga = lambda linea: estructura(linea.split())
# Carga(linea) nos devuelve la línea como diccionario

def cogelineas(fichero, funestr):
    return map(lambda linea: funestr(linea), open(fichero, 'r'))
# Cogelineas(fichero, funestr) nos devuelve un map de líneas de fichero a estructura, usando la función funestr

datos = list(cogelineas('precios.txt', carga))
# Una lista de las líneas del fichero; cada una como estructura

precios = map(lambda lin: lin['precios'], datos)
# Solo los precios de cada línea

nombres = map(lambda lin: lin['nombre'], datos)
# Solo los nombres de cada línea

todos = rd(lambda previo, otro: np.vstack((previo, otro)), precios)
# Matriz numpy con una fila para cada precio

rangos = list(map(lambda precio, nombre: (nombre, np.min(precio), np.max(precio)), todos, nombres))
print("Rangos de precios:")
list(map(lambda rango: print(f"{rango[0]}: Mínimo = {rango[1]}, Máximo = {rango[2]}"), rangos))
# Variación 1: Rango de precios (mínimo y máximo)

prom_posc = list(map(lambda precio: np.mean(np.argsort(precio)), todos))
ind_mejor_prom = int(np.argmax(np.array(prom_posc)))
# Variación 2: Promedio de la mejor posición de cada histórico

nombres = list(map(lambda lin: lin['nombre'], datos))
# Convierto el objeto map de nombres a una lista, esta solución surgió a causa de un error que presentó de 'índice fuera de rango'

print(f"\nLa acción con el mejor promedio de posición es: {nombres[ind_mejor_prom]}")
# Resultado pedido