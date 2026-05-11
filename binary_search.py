import random
import time

def busqueda_ingenua(lista, target):
    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1


#si la lista es muy grande es mas eficiente la busqueda binaria, pro la lista debe estar ordenada en orden ascendente
def binary_search(lista, target, inf_limit=None, sup_limit=None):
    if inf_limit is None:
        inf_limit = 0 # inicio de lista
    if sup_limit is None:
        sup_limit = len(lista) - 1 # final de lista

    if sup_limit < inf_limit:
        return -1

    punto_medio = (inf_limit + sup_limit) // 2

    # [1, 3, 5, 10, 12]
    #  0  1  2   3   4
    # punto_medio = (0 + 4) // 2 = 4 // 2 = 2

    if lista[punto_medio] == target:
        return punto_medio
    elif target < lista[punto_medio]:
        return binary_search(lista, target, inf_limit, punto_medio - 1)
    else:
        return binary_search(lista, target, punto_medio + 1, sup_limit)


if __name__=='__main__':
    # crear lista ordenada con 10000 numeros aleatorios
    size = 10000
    initial_list = set()

    while len(initial_list) < size:
        initial_list.add(random.randint(-3*size, 3*size))

    sorted_list = sorted(list(initial_list))

    #medir tiempo de busqueda ingenua
    inicio = time.time()
    for target in sorted_list:
        busqueda_ingenua(sorted_list, target)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos.")

    # medir tiempo de binary search
    inicio = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    fin = time.time()
    print(f"Tiempo de busqueda binaria: {fin - inicio} segundos.")