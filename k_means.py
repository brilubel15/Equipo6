from scipy.spatial import distance
from sklearn.cluster import KMeans
from os import system
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib
from visualizations import show_clusters_centroids

def distancia(lista1,lista2):
    #import pdb; pdb.set_trace()
    dist = distance.euclidean(lista1, lista2)
    return dist

def centros(lista):
    # Create an empty list for the new centers
    centros_list = []

    # Convert the list into a numpy array
    listasnonpy = np.array(lista, dtype=object)

    for i in listasnonpy:
        centros_list.append(np.mean(i, axis = 0))
    return centros_list

def cercanos(puntos,centros):
    lista=[[]for x in centros]
    #import pdb; pdb.set_trace()
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

    cantidad_de_centros = int(input("Elija la cantidad de centros: "))
    system('clear')
    iterationts = int(input("Elija la cantidad de iteraciones: "))

    idx = np.random.randint(len(points),size=cantidad_de_centros)
    k_lista = points[idx,:]
    clusters = cercanos(points, k_lista)

    # Redifine puntos and centers adjusting with the methods cercanos() and centros()
    for i in range(iterationts):
        if i % 1 == 0:
            if i == 0:
                title = "Initialization"
            else:
                title = "Iteration {}".format(i+1)

        show_clusters_centroids(clusters, k_lista, title)
        clusters = cercanos(points, k_lista)
        k_lista = centros(clusters)

    # Return the new adjustes list
    return clusters, k_lista

def generarPuntos(i, j):
    puntos = []
    for cony in range(i):
        lista=[]
        for conx in range(j):
            lista.append(random.randint(0, 5000))
        puntos.append(lista)
    return puntos

# def generarPuntos(i):
#     lista = []
#     for con in range(i):
#         lista.append(random.randint(0, 100))
#     return np.array(lista)


if __name__ == '__main__':
    system('clear')
    system('clear')
    puntos = generarPuntos(200, 8)
    # print("Antes: ")
    # print(puntos)
    cluster=k_means(puntos)
    print("Despues: ")
    print(cluster)
