# Proyecto 1 - Sistemas de Redes
Proyecto en el que se hace uso de algoritmos de búsqueda en grafos para recrear una situación de una agencia de viajes que busca diseñar rutas de vuelo entre distintas ciudades.

---
## Visualización
Para un mejor entendimiento, se realizó esta matriz que indica los costos de viajar entre las distintas ciudades. <br>

<p align="center">
  <img width="750" height="250" src="https://github.com/samuelmarina/sistemas-de-redes/blob/main/imagenes/matriz-costo.png">
</p>

*- Amarillo: existe una conexión entre las ciudades de dicha celda* <br>
*- Blanco: no existe una conexión entre las ciudades de dicha celda* <br>
*- Rojo: diagonal principal - no existen vuelos de una ciudad a ella misma*

---
## Instrucciones
1. Clone el proyecto y ábralo en su editor de texto de preferencia
2. Ejecute el archivo **main.py** desde el terminal o la línea de comandos
3. Siga las instrucciones impresas

---
## Observaciones
* El *input* a ingresar en la terminal por parte del usuario a la hora de escoger las ciudades de origen y destino, tiene que coincidir con alguna de las ciudades en la lista.
Puede estar escrito en minúsculas o mayúsculas.

<p align="center">
  <img width="500" src="https://github.com/samuelmarina/sistemas-de-redes/blob/main/imagenes/nota-1.png">
</p>

*Ejemplo: para seleccionar **CCS**, el usuario debe introducir **CCS** ó **ccs**.*

* El *input* a ingresar en la  terminal por parte del usuario a la hora de escoger el tipo de ruta, tiene que coincidir con el número que enlista a la misma.

<p align="center">
  <img width="500" src="https://github.com/samuelmarina/sistemas-de-redes/blob/main/imagenes/nota.png">
</p>

*Ejemplo: **1** para la ruta más corta, y **2** para la ruta más barata*

---
## Algoritmos
En este proyecto se busca conocer las ruta más corta y la ruta más barata de viajar entre dos ciudades (origen y destino). <br>
* Para conseguir la ruta más corta entre dos ciudades (menor cantidad de vuelos a tomar), se utilizó el algoritmo **Breadth-First Search**. <br>
* Para conseguir la ruta más barate entre dos ciudades, se utilizó el algoritmo **Dijkstra's Shortest Path**.

---
## Autores
* Samuel Mariña
* María Cafarelli
* Gabriel Silva
* Andrés Linarez
