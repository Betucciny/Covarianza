import numpy as np
from sklearn import datasets


def covarianza(mat):
    media = mean(mat)
    center = mat - media
    resul = mult2(center)
    cov = resul / (len(mat[0]))
    return cov


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
    return np.array(m)


def transpuesta_nocuadrada(matriz):
    m = []
    for i in range(len(matriz[0])):
        m.append([])
        for j in range(len(matriz)):
            m[i].append(matriz[j][i])
    return np.array(m)


def matrixmult(m1, m2):
    m = []
    for i in range(len(m1)):
        m.append([])
        for j in range(len(m2[i])):
            m[i].append(0)
            for k in range(len(m2)):
                m[i][j] += m1[i][k] * m2[k][j]
    return np.array(m)


def vectormult(vector):
    m = []
    for i in range(len(vector)):
        m.append([])
        for j in range(len(vector)):
            m[i].append(vector[i] * vector[j])
    return np.array(m)


def mult2(mat: np.ndarray):
    m = np.zeros((len(mat), len(mat)))
    for i in range(len(mat[0])):
        m = m + vectormult(mat[:, i].T)
    return m


def main():
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target
    mat = np.concatenate((x, y[:, None]), axis=1).T
    resul = covarianza(mat)
    imprimir(resul)


if __name__ == '__main__':
    main()


