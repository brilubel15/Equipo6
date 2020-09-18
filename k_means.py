from scipy.spatial import distance
from sklearn.cluster import KMeans
import nompy as np
import random

def distancia(lista1,lista2):
    distancia = distance.euclidean(lista1, lista2)
    return distancia

def centros(puntos):
    # Create an empty list for the new centers
    centros = []

    # Convert the list of lists into a numpy array
    listasnonpy = np.array(puntos)

    # Start a loop that goes from 0 to the last list in listas
    for lista in puntos:
        sumaParcial = 0
    # Strart a loop that will get the summatory for the values in each list
        for i in lista:
            sumaParcial+=i
    # Get the avarage for each list and store ir as a center in a list of centers
        centros.append(sumaParcial/float(len(lista[i])))

    # After going through all the lists, sends the new list of centers
    return centros

   def cercanos(puntos,centros):
       lista=[[]for x in centros]
       for i, punto in enumarate(puntos):
           dist=[]
           for j, centro in enumarate(centros):
               dist.append(dist((punto, centro)))
           min=np.argmin(dist)
           lista[min].append(punto)
   return lista

def k_means(puntos):
    # Set an empty list for centers
    k_lista = []

    # Search for the minimum and maximum value in the lists of puntos
    min = puntos[0][0]
    max = min
    for lista in puntos:
        for i in lista:
            temp = i
            if(temp<min):
                min = temp
            elif(temp>max):
                max = temp

    # Define the quantity of ceners according to the quantity of data
    length = 0
    for lista in puntos:
        length+=len(lista)
    if length>3:
        n = random.randint(2, (len(puntos)+1)/3)
    else:
        n = random.randint(2, 3)

    # Create n of centers between the minimum and maximum value in puntos
    for i in range(2, n):
        k_lista.append(random.randint(min, max))

    # Redifine puntos and centers adjusting with the methods cercanos() and centros()
    for i in range(100):
        puntos = cercanos(puntos, k_lista)
        k_lista = centros(k_lista)

    # Return the new adjustes list
    return puntos

def generarPuntos(i, j):
    lista = []
    puntos = []
    j= (int)(j/i)
    for cony in range(i):
        for conx in range(j):
            lista.append(random.randint(0, 100))
        puntos.append(lista)
    return puntos

if _name_ == '_main_':
    puntos = generarPuntos(8, 8)
    print("Antes: ")
    print(puntos)

    k_means(puntos)
    print("Despues: ")
    print(puntos)
