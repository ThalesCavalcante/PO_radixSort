import timeit
from random import randint
import matplotlib.pyplot as plt
import sys
from random import shuffle

sys.setrecursionlimit(10 ** 6)


def desenhaGrafico(x, y, xl="Entradas", yl="Saidas", name="out"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)


def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def radixSort(lista):
    exponencial = 1
    maior = max(lista) if len(lista) > 2 else 0


    bckts = [ [] for i in range(10)]


    while maior // exponencial > 0:
        for i in lista:
            bckts[(i//exponencial)%10].append(i)


        del lista[:]


        for i in range(len(bckts)):


            lista.extend(bckts[i])
            bckts[i] = []

        exponencial *= 10
    return lista


size = [100000, 200000, 400000, 500000, 1000000, 2000000]
time = []

for s in size:
    lista = geraLista(s)
    time.append(timeit.timeit("radixSort({})".format(lista),
                              setup="from __main__ import radixSort", number=1))
    print(s)

desenhaGrafico(size, time, "Tamanho", "Tempo",
               "radixSort.png")
