import numpy as np


def coef():
    m = np.array([[1, 2, 3, 4],
                  [2, 1, 4, 3]])
    return m


def imprimir(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


def mean(matriz):
    m = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
        m.append([suma/len(matriz[i])])
    return m


def transpuesta_nocuadrada(matriz):
    m = []
    for i in range(len(matriz[0])):
        m.append([])
        for j in range(len(matriz)):
            m[i].append(matriz[j][i])
    return m


def main():
    mat = coef()
    media = mean(mat)
    center = mat - media
    resul = np.dot(center, transpuesta_nocuadrada(center))
    imprimir(resul)


if __name__ == '__main__':
    main()


