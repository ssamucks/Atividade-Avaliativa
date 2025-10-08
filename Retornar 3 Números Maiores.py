lista = [42, 12, 9, 73, 51, 22]

def ordenar_lista(numeros: list[int]):
    listaOrdenada = sorted(numeros, reverse=True)
    listaOrdenada = listaOrdenada[:3]
    return listaOrdenada

print(ordenar_lista(lista))