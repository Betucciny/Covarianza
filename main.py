import numpy as np


def coef():
    m = np.array([[1, 2, 3, 4],
                  [2, 1, 4, 3]], dtype=float)
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


def matrixmult(m1, m2):
    m = []
    for i in range(len(m1)):
        m.append([])
        for j in range(len(m2[i])):
            m[i].append(0)
            for k in range(len(m2)):
                m[i][j] += m1[i][k] * m2[k][j]
    return m


def main():
    mat = coef()
    media = mean(mat)
    center = mat - media
    resul = matrixmult(center, transpuesta_nocuadrada(center))
    imprimir(resul)


if __name__ == '__main__':
    main()


