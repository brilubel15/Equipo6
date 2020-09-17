from scipy.spatial import distance
from sklearn.cluster import KMeans
import nompy as np

def distancia(lista1,lista2):
    distancia = distance.euclidean(lista1, lista2)
    return distancia


def centros(listas):
    listasnonpy = np.array(listas)
    sumaParcial = 0
    for lista in listas:
        sumaParcial+=lista
    cantValores = len(listas)
    return sumaParcial/float(cantValores)
print promedio
