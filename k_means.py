from scipy.spatial import distance

def distancia(lista1,lista2):
    distancia = distance.euclidean(lista1, lista2)
    return distancia
