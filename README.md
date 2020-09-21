# Equipo 6
Este repositorio fue creado durante la Semana Tec: Herramientas computacionales, el arte de la analítica. (TC10025.2)

### Integrantes del Equipo:
- Brianda Lubel García
- Arturo Sosa
- Javier Perdomo
- Alan Cassab
- Salomon Shabot

Los centros encontrados con nuestra implementación en Python del método de k Means sí pueden ser representativos, pero debemos de tener mucho cuidado en algunos aspectos:
- No realizar demasiadas iteraciones del problema
- No hacer muy pocas iteraciones
- Utilizar un valor adecuado de K
- Asegurarse de que los valores de los centros no sean demasiado similares

Estas son cuestiones que siempre deben de considerarse al utilizar algún método estadístico de machine learning, en especial si es un método insupervisado.

Ela valor de K utilizado fue de 3, ya que en nuestra base de datos original solamente teníamos tres clases de datos (en este caso, tres tipos de flores). Si usáramos otro número para el valor de K, los datos no serían representativos para las clases que estamos buscando, pero podrían serlo para agrupar los datos en otros valores.

En las primeras iteraciones del programa, algunos centros estaban muy cerca entre sí, pero más adelante se fueron separando, y fueron identificando de manera más exacta los grupos de los valores.

Al graficar las clases, antes de utilizar el algoritmo de k Means, podríamos analizar si hay muchos outliers que puedan afectar de forma negativa las agrupaciones de los clusters, y podríamos utilizar medianas en vez de promedios, para asegurarnos de que no afecten a nuestros centros.
