from scipy.spatial import distance
#from sklearn.cluster import KMeans
import numpy as np
import random

def distancia(lista1,lista2):
    distancia = distance.euclidean(lista1, lista2)
    return distancia

def centros(lista):
    # Create an empty list for the new centers
    centros_list = []

    # Convert the list into a numpy array
    listasnonpy = np.array(lista)

    for i in listasnonpy:
        centros_list.append(np.mean(i, axis = 0))
    return centros_list

def cercanos(puntos,centros):
    lista=[[]for x in centros]
    for i, punto in enumerate(puntos):
        dist=[]
        for j, centro in enumerate(centros):
            dist.append(distancia(punto,centro))
        small=np.argmin(dist)
        lista[small].append(punto)
    return lista

def k_means(puntos):
    cantidad_de_centros = 0
    points = np.array(puntos)
    # cantidad_de_centros = int(input("Elija la cantidad de centros: "))
    cantidad_de_centros = 3
    idx = np.random.randint(len(points),size=cantidad_de_centros)

    k_lista = points[idx,:]

    # print("Puntos: ")
    # print(puntos)
    # print("Centros: ")
    # print(k_lista)

    # Redifine puntos and centers adjusting with the methods cercanos() and centros()
    for i in range(100):
        k_lista = centros(cercanos(puntos, k_lista))

    # Return the new adjustes list
    return k_lista

def generarPuntos(i, j):
    lista = []
    puntos = []
    j= (int)(j/i)
    for cony in range(i):
        for conx in range(j):
            lista.append(random.randint(0, 100))
        puntos.append(lista)
    return puntos

if __name__ == '__main__':
    puntos = generarPuntos(8, 8)
    print("Antes: ")
    print(puntos)

    k_means(puntos)
    print("Despues: ")
    print(puntos)
