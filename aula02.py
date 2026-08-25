def bubble_sort(lista):
    n=len(lista)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1

    return lista, comparacoes, trocas

def selection_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1
    return lista, comparacoes, trocas

def insertion_sort(lista):
    comparacoes, deslocamentos = 0
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if lista[j] > atual:
                lista[j + 1] = lista[j]
                j -= 1
                deslocamentos += 1
            else:
                break
        lista[j + 1] = atual
    return lista, comparacoes, deslocamentos

bubbe, comp_b, trocas_b = bubble_sort(numeros[:])
insertion, comp_i, desloc_i = insertion_sort(numeros[:])
selection, comp_s, trocas_s = selection_sort(numeros[:])

print("Comparações Movimentações")
print("Bubble sort: ", comp_b, "       ", trocas_b)
print("Insertion sort: ", comp_i, "       ", desloc_i)
print("Selection sort: ", comp_s, "       ", trocas_s)