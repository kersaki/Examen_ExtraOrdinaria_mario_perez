# Examen_ExtraOrdinaria_mario_perez

https://github.com/kersaki/Examen_ExtraOrdinaria_mario_perez.git

1.1 Creación (0,5 puntos)
 
Crea una clase llamada armaduras.py que tenga los atributos nombre y rango
Crea el constructor de la clase. Añadir en el constructor un print para informar de que la armadura se ha creado con éxito.
Crear un método llamado calificacion que clasifique a las armaduras de IronMan de la siguiente forma: 
1.2 Experimentación (0,5 Puntos)
Crea una lista con un numero arbitrario de objetos tipo armaduras.
Recorre los elementos de la lista, y prueba a ejecutar el método calificación de cada objeto que has creado

2.1 Creación (0,5 puntos)
 
Copia el ejercicio anterior y realicemos la siguiente modificación:
 
Junto al método init y calificación, sobrescriba el método especial de Python, el método str, que tiene el siguiente formato:
 
 
def __str__(self):
    return "Lo que quiero mostrar"
 
 
Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto stormtropper1 creado y realizamos print(armaduras1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).
 
 
2.2 Experimentación (0,5 puntos)
 
Implementa el método str y haz que muestre el nombre y el rango de las armaduras
Crea una lista con un numero arbitrario de objetos tipo Armaduras.
Recorre los elementos de la lista, y utiliza el método print de esos objetos para visualizar por pantalla la información del str

3.1 Creación (0,5 Puntos)
 
Crea una clase llamada artefactosvaliosos.py que tenga los atributos peso, nombre, precio y fecha de caducidad.
Crea el constructor de la clase. Añade en el constructor un print para informar de que la conserva se ha creado con éxito
Crea el método __str__ para visualizar por pantalla la información de los productos
 
 
3.2 Experimentación (0,5 Puntos)
 
Crea algunos artefactos valiosos
Prueba a mostrar los datos de algunos artefactos valiosos ordenados por su fecha de caducidad y a modificar algún valor, por ejemplo, prueba a modificar el precio de un de la conserva

4.(1 Punto)
Suponga que Namor está atrapado bajo el fuego de las armaduras de IronMan, pero muy cerca está su mochila que contiene muchos artefactos valiosos que debe impedir a toda costa que sean requisados por el ejército de armaduras.
Implementa una función recursiva llamada “hijo sin amor” que le permita a Namor en su último aliento y “con ayuda del dios Kukulcán” realizar las siguientes actividades:
 
sacar los objetos de la mochila de a uno a la vez hasta encontrar un anillo de poder o que no queden más objetos en la mochila;
 
Determinar si la mochila contiene un anillo de poder y cuantos objetos fueron necesarios sacar para encontrarlo;
 
Utilizar una lista para representar la mochila.

5.(1 Punto)
IronHeart maestra ladrona del multiverso, ha robado de las manos de una armadura una mochila con muchos artefactos valiosos (Pensamos que era de un poderoso dios Azteca.). Pero, llegando a la nave Wakandiana se da cuenta que para escapar de las garras del malvado Ultrón debe desprenderse de algunos artefactos valiosos ya que su nave debe ser más ligera que la de ultrón y debe contener una cantidad limitada de peso. Su objetivo es salir con el valor combinado más alto de artefactos que quepan en la mochila, pero ¿cómo elige estos artículos y cuál es el valor óptimo?
 
Ahora vamos a ser un poco más precisos y dados los siguientes valores:
precio = [103, 60, 70, 5, 15] 
pesos = [12, 23, 11, 15, 7]
peso_maximo = 100
 
¿Cuál es el valor máximo de los artículos que se pueden agregar a la mochila de manera que el peso no exceda el límite de peso W?

6. (2,0 Puntos)
Ultrón te ha destinado la misión de desarrollar los algoritmos para organizar las armaduras cumpliendo con las siguientes demandas:
 
Deberá generar 2000 Armaduras siguiendo el formato de la imagen del primer ejercicio contemplando las siguientes legiones FL, TF, TK, CT, FN, FO y los dígitos generados de manera aleatoria;
 
deberá cargar los Armaduras generados en dos tablas hash encadenadas, en la primera se deberá agrupar de acuerdo con los tres últimos dígitos del código y en la segunda a partir de las iniciales de la legión;
 
determinar si el Armaduras FN-2187 está cargado para poder quitarlo porque es un trai dor desertor.
 
ahora obtenga todos los Armaduras terminados en 781 para asignarlos a una misión de asalto y a los terminados en 537 para una misión de exploración;
 
ahora obtenga los Armaduras de la legión CT para que custodien a Ultrón a una misión de exploración al planeta Hoth y los de la legión TF para una misión de extermi nación a IronHeart.

7.(1 Punto)
Black Panther, líder del escuadrón Nuevos Vengadores, tiene dificultades para transmitir los mensajes a la base de los Vengadores Originales, dado que los mismos son muy largos y los satélites espías de Ultrón los intercepta, en un lapso muy corto desde que se transmiten. Por lo cual, nos solicita desarrollar un algoritmo que permita comprimir los mensajes para enviarlos más rápido y no puedan ser interceptados. Contemplando los siguientes requerimientos, implementar un algoritmo que pueda crear un árbol de Huffman a partir de la siguiente tabla y desarrollar las funcionas para comprimir y descomprimir un mensaje.

8. (2 Puntos)
Generar un grafo no dirigido con planetas del MCU y diseñar los algoritmos necesarios para resolver las siguientes actividades:
 
los siguientes planetas deben estar en el grafo: Tierra,Knowhere,Zen-Whoberi,Vomir,Titán,Nidavellir, agregue 7 más;
 
genere al menos 4 aristas para cada uno de los planetas del grafo, no puede haber nodos con arcos a sí mismo;
 
encuentre el árbol de expansión mínima en cuanto a costos para recorrer todos los planetas;
 
hallar el camino más corto desde:
 
Tierra hasta Vormir,
 
Knowhere hasta Titán,
 
Zen-Whoberi hasta Nidavellir;
 
determinar todos los planteas a los que se puede llegar desde Titán.