# Instituto Tecnológico de Costa Rica      Principios De Sistemas Operativos
# Proyecto II                                             Grupo 50
## Elison Corrales Vargas - Ian Vargas Ledezma - Jean Carlos Urbina - Steven Alvarado Aguilar
## Programación de categorizador de páginas web utilizando el teorema de Bayes
###     El teorema de Bayes es utilizado para calcular la probabilidad de un suceso, teniendo información de antemano sobre ese suceso. Podemos calcular la probabilidad de un suceso A, sabiendo además que ese A cumple cierta característica que condiciona su probabilidad. El teorema de Bayes entiende la probabilidad de forma inversa al teorema de la probabilidad total. (J. F. López, 2021). 
###     Para la creación de este proyecto usaremos el lenguaje de programación Python y utilizaremos una base de datos en Postgresql  en ella desde Python le enviamos los diferentes urls que el programa encuentra según el código programado y busca las palabras según las clasificaciones que creamos y que más adelante vamos a explicar de mejor manera. En el proyecto implementamos las clases Bayes, Conexión, funcionespostgres y webScraping las cuáles tendrán la codificación necesaria para lograr que el proyecto cumpla con todos los requerimientos explicados por el profesor.
### Iniciamos con la clase Conexión : Esta clase se creó con la intención de tener un método de acceso a la base de datos, con esta clase podemos conectarnos a un servidor local de postgres ingresando un string de conexión. 
### Para que la conexión se realice utilizamos una librería de python llamada psycopg2 esta es un adaptador de base de datos PostgreSQL más popular para el lenguaje de programación Python. Sus principales características son la implementación completa de la especificación Python DB API 2.0 y la seguridad de subprocesos (varios subprocesos pueden compartir la misma conexión). Su instalación en el proyecto por medio de la terminal fue la siguiente: pip install psycopg2.
###     Para la clase funcionespostgres se importó la clase Conexión, ya que necesita estar en comunicación para que se conecte a la base de datos y se hagan todos los procedimientos. Primero creamos una lista con palabras. Creamos el método insertarcategoria que recibirá los parámetros nombreTabla y lista la cual abre una conexión a postgres con un cursor que tendrá el tiempo de activación en dónde iremos insertando una por una las palabras que encontraremos en una página web luego la conexión hace un commit si se llega a la última palabra, se cierra el cursor y se hace un close para cerrar la conexión con la base de datos.
### La función principal de insertarcategoria es meter las palabras que tengan que ver con una temática en específico en la base de datos, por ejemplo si se quiere realizar una base de datos que tenga palabras relacionadas a deportes el procedimiento es el siguiente:
###     Buscamos en internet una página web que tenga un listado de palabras relacionadas a la temática en este caso pudimos encontrar un buen referente en el siguiente link https://relatedwords.io/sport esta pagina pide ingresar un tema y devuelve una cantidad bastante considerable de palabras relacionadas. Una vez tenemos ese listado podemos hacer uso de nuestro WebScraping para extraer estas palabras, almacenarlas en una lista y finalmente hacer uso de la función insertar categoría, de esta manera se realizó un repositorio de tablas con palabras relacionadas a una temática para preparar el teorema bayes. 
### WebScraping para sacar palabras relacionadas a una temática 
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture1.png)
###     Además se creó el método consultar categoría, este sirve para consultar las palabras clave de una categoría en específica, con el fin de almacenar todas las palabras clave en una estructura de datos de tal manera automatizar el hecho de no estar haciendo múltiples peticiones a la base de datos, con esta lista podemos prepararnos para el teorema bayesiano. 
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture2.png)
###     Creamos otro método llamado consultar no tiene ningún parámetro, debido a que una consulta donde se abre la conexión y el cursor y se ejecuta los datos de la tabla seleccionada y en la cual se va a recorrer los diferentes datos consultados y los mostraremos, luego de todo esto se cerrará tanto el cursor y la conexión. La función principal es corroborar que los elementos si se están insertando en la tabla, como un punto adicional este método podría ser dinámico de manera que podamos insertar una categoría cualquiera y devuelva el mismo resultado, en este caso únicamente consultamos la categoría deportes.
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture3.png)
###     Creamos el método de eliminar el cuál abrimos la conexión y el cursor ejecutamos la función de eliminar todos los datos de la base de datos, hacemos un commit para confirmar la transacción pendiente en la base de datos, esta función tiene como objetivo vaciar la tabla en la base de datos únicamente si se necesitara la reinserción en algun momento, al igual que la anterior este método podría ser genérico para poder ser utilizado con cualquier tabla.
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture4.png)
###     Creamos un método para insertar los resultados que obtengamos de el WebScraping aplicado a una lista de links en la base de datos, en este caso se pidió un total de 10.000 links para realizar el web scraping, la función que inserta estos resultados es la siguiente:
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture5.png)
###     Además se creó un método para obtener los resultados y almacenarlos en una estructura de datos tipo lista, de esta forma evitamos realizar el WebScraping cada vez que se ejecute el programa, a sí mismo se realizó otro método para eliminar estos resultados de ser necesario la reinserción.
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture6.png)
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture7.png)
###     Finalmente se crean dos funciones de suma importancia para la interfaz gráfica que se va desarrollar, estos métodos se utilizan para almacenar los links según el resultado de su categorización en la base de datos con la tabla resultados, el método categorizar recibe el link y el nombre de la categoría resultante después de su análisis mediante el webScraping. La segunda función llenarPalabrasCategorizadas es para guardar la lista de palabras que fueron categorizadas en las temáticas correspondientes, este resultado se guarda en la tabla resultados, es decir para cada link guardamos lo siguiente:
###     1- El link de referencia 
###     2- El html del WebScraping 
###     3- La categoría 
###     4- La lista de palabras de la categorización 1 con la cantidad de repeticiones por palabra.
###     5- La lista de palabras de la categorización 2 con la cantidad de repeticiones por palabra.
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture8.png)
### Para la clase webScraping se requieren algunas importaciones importantes, primero necesitamos conectarnos a la base de datos donde están almacenados los url a consultar, para esto realizamos una petición a la clase conexion donde realizaremos una nueva conexión a la base de datos para realizar la consulta de petición de urls (import Conexion),  seguidamente una vez obtenemos el resultado del query se nos pidió realizar el primer nivel de multiprocesamiento para consultar cada página y realizar el web scraping, en este nivel se requiere el uso de la librería BeautifulSoup de bs4(from bs4 import BeautifulSoup) y la librería requests(import requests) además para realizar el multiprocesamiento se requiere la librería  ThreadPoolExecutor la cual nos permite crear threads para multiprocesamiento(from concurrent.futures import  ThreadPoolExecutor)
### Creamos un método llamado webscraping el cual realiza la solicitud a la base de datos para obtener los 10.000 links, para efectos de prueba se limita la consulta para que devuelva un total de 50 links, ya que el tiempo de consulta es demasiado elevado con 10.000 lo que dificulta el avance del proyecto en prueba y error. Seguidamente se crea un ejecutor con un total de 3 hilos para ser usados a continuación. El procedimiento es el siguiente:
###     1- Se solicitan los links 
###     2- Se crea el ejecutor con la cantidad de hilos deseados 
###     3- Se recorre el resultado de la consulta y se obtiene el url para enviarlo a la función extraer. 
####    Nota: como los hilos se ejecutan en paralelo se requiere un tiempo para que cada hilo haga el procedimiento antes de que no da tiempo a la funcion extraer de realizarse correctamente, para dar este tiempo se hace uso de la librería time(import time) con el método sleep para que cada 2 segundos se ejecute la función que extrae el html de cada link. Además si desea ver cuál hilo está en uso puede importar la librería logging para imprimir que hilo está ejecutando.
###     El método extraer es la función más importante en este procedimiento ya que es la que realiza todo el proceso de parseo del html y lo obtiene en un string de palabras con todo el contenido de la página, hacemos uso de BeautifulSoup y requests para consultar el link que se solicite con la función webScraping mencionada anteriormente. El procedimiento es el siguiente:
###     1- Se obtiene el link enviado desde WebScraping 
###     2- Se realiza la petición para obtener la página con requests
###     3- Se parsea la con BeautifulSoup para obtener el contenido en formato html 
###     4- Se establecen las etiquetas de parseo para desechar lo innecesario, en este caso solicitados todos los <p>,<span> y <h1>, adicionalmente podemos solicitar los <strong> que también típicamente tienen texto. 
###     5- Se crea un string con esa información y se agregan a una lista global la cual serán los resultados finales del WebScraping, esta lista guarda sublistas con el url y la sublista de palabras obtenidas del parseo. 
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture10.png)
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture9.png) 
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture11.png)
###     En la clase Bayes ocurre todo el procedimiento de preparación para el teorema de bayes, esta clase hace uso de las demás clases para obtener los datos necesarios para el teorema, además acá se realiza el segundo nivel de multiprocesamiento donde al ingresar un nuevo link a la base de datos este tiene que ser parseado y categorizado según la historia, en este caso la historia es el total de información que obtuvimos con el webScraping de los 10.000  links. 
## Dependencias 
### Primero crear un entorno virtual, Si no se tiene virtualenv hay que correr 
##      pip install virtualenv
### luego hay que activar el entorno virtual con 
##      .\env\Scripts\activate
### Si sale el (env) al inicio significa que ya estamos en el entorno virtual
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture12.png)
### luego en el entorno virtual se instalan las demás dependencias
##      pip install flask
##      pip install partial
##      pip install psycopg2 
##      pip install Pool
##      pip install time
##      pip install bs4 
##      pip install requests
##      pip install ThreadPoolExecutor
## Ahora para levantar el servidor y correr la aplicación se ejecuta 
##     python .\app\app.py
###     Importante: siempre ejecutar la línea que levanta el servidor en el entorno virtual ya que sino no tendría las dependencias necesarias.
nota: cuando ocurren errores en el código se cae el servidor entonces tenemos que volver a correr la línea >python .\app\app.py  en el entorno virtual.
###    Después tenemos que verificar las importaciones necesarias, primero se requiere obtener la lista global que creamos en la clase anterior ya que aqui esta toda la información de los sitios web junto con sus html, por lo tanto necesitamos importar la clase webScraping(import webScraping) además debemos hacer uso de las funciones que nos conectan a la base de datos para obtener la lista de las palabras clave a utilizar en el teorema, por lo tanto necesitaremos importar funciones postgres(import funcionespostgres) finalmente como acá se realiza el segundo nivel de multiprocesamiento requerimos importar otra librería para multiproceso, esta vez Pool (from multiprocessing import Pool).
###     Creamos un método llamado cargar, este método se encarga de obtener la lista global de la clase WebScraping y también corrige algunos errores que explicaremos a continuación, esto es el procedimiento del método:
###     * Solicita ejecutar el WebScraping de los links 
###     * Solicita la lista obtenida que se guarda globalmente en la clase 
recorre esa lista para corregir errores: Los errores que podemos presentar es que al obtener el html completo de una página, tenemos demasiada información que no se utilizará, como algunos símbolos “<” y “>”, “//”, “\\”, “.”, “,”, “:”, “;”, “‘”, “\n” y muchos otros que en este procedimientos son eliminados para mejorar la precisión de las palabras y evitar las solicitudes extras a la base de datos de palabras clave. 
###     * Se solicita la función de postgres insertar Resultado para meter los links junto con las palabras arregladas en la tabla resultados.
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture13.png)
###     Una vez ejecutamos el método cagar, no necesitaremos ejecutarlo otra vez ya que la información optimizada ya está en la base de datos por lo cual no necesitamos solicitar un segundo WebScraping. Seguidamente realizamos procedimientos de forma global para guardar la información de la base de datos, los pasos son los siguientes:
###     * Creamos una variable global para almacenar la lista de resultados, para obtener esta lista hacemos uso del método llenarResultado véase explicado en las funciones  de la clase funcionespostgres este método devuelve una lista con los elementos de la tabla resultados almacenados en la base de datos, después se crea una lista Palabras para segmentar el string de html, que este aunque ya esté optimizado es un string con todas las palabras que necesitan ser separadas para verificarlas una por una, aquí hacemos uso de la funcion split de python para separar el string con cada espacio que encuentre, los pasos son los siguientes:
###     - Crear una nueva lista global
###     - Recorrer la lista de resultados
###     - Realizar el split a la sublista donde esta el string del html de cada url
###     - Guardar esta segmentación en la lista nueva
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture14.png)
###     * Seguidamente conocemos ya las url y sus respectivas palabras segmentadas, pero no conocemos la cantidad de repeticiones de cada palabra, por lo cual necesitaremos contar estas palabras de la siguiente manera 
###     - Se crea una lista definitiva global 
###     - Se recorre la lista de palabras segmentada, la que creamos anteriormente(listaPalabras)
###     - Se crea una lista con las frecuencias de cada palabra haciendo uso de la función count de python.
###     -  Creamos una tupla que contiene la palabra y el número de repeticiones obtenidos de la lista frecuencia, como lista de frecuencia y lista palabras por link tienen el mismo len, podemos hacer uso de la función zip para realizar la tupla correspondiente a cada palabra con su respectiva frecuencia 
###     - Realizamos un segundo recorrido porque necesitamos quitar las repeticiones de las palabras, ya que sería ilógico que guardaramos la misma tupla varias veces. 
###          + Ejemplo: En el html se recolectó la palabra “fútbol” y se obtuvo una frecuencia de 2, la tupla generada es la siguiente (‘fútbol’, 2) pero como hay 2 repeticiones solo necesitamos guardar una tupla. 
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture15.png)
### Creamos un método para imprimir la lista definitiva para verificar que los arreglos se realizan correctamente.
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture16.png)
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture17.png)
###     Seguidamente explicaremos el método sacarProbabilidadPrevia, este método es el que obtiene la historia de los links totales en la lista definitiva, de esta manera podemos obtener un universo, una cantidad de links para categoría 1 y otra para categoría 2, el procedimiento del método es el siguiente:
###     - Se guardan las palabras claves en dos listas, una para categoría 1 y otra para la categoría 2, estas variables hacen uso de la funcion consultar categoría de la clase funncionesposgrest 
###     - Se crea una variable que será el len de la lista definitiva, esta variable nos servirá como universo para aplicar el teorema de bayes. 
###     - Se crean 3 variables, cant1, cant2, otro 
###          * cant1: Almacena el total de links en categoría 1 
###          * cant 2 : Almacena el total de links en categoría 2
###          * otro: Almacena los links que no se categorizaron en ninguna de las anteriores
###     - Se recorre la lista definitiva para obtener por cada link la lista de palabras segmentadas, arregladas y contabilizadas. 
###     - Se crean 4 listas dentro del recorrido:
###          * LD: es la lista que guardara las palabras clasificadas en la categoría 1 para almacenar en la base de datos resultados
###          * LS: es la lista que guardara las palabras clasificadas en la categoría 2 para almacenar en la base de datos resultados
###          * L1: es la lista que guardara las palabras clasificadas en la categoría 1 para ser comparada al final 
###          * L2: es la lista que guardara las palabras clasificadas en la categoría 2 para ser comparada al final 
###     - Se pregunta por cada palabra de la lista de palabras de cada link si esta existe en la base de datos de palabra clave para categoría 1 o 2, dependiendo de este resultado la palabra se agrega a las listas, en este caso se agrega de la siguiente manera:
###          * Si la palabra es encontrada en la categoría 1: Se agrega a LD Y L1, el primer append es para guardar toda la tupla con la frecuencia para usarla en el gráfico final y la segunda para verificar la clasificación comparando la cantidad de palabras en L1 y L2 
###          * Si la palabra es encontrada en la categoría 2 : Se agrega a LS Y L2, el primer append es para guardar toda la tupla con la frecuencia para usarla en el gráfico final y la segunda para verificar la clasificación comparando la cantidad de palabras en L1 y L2 
###     - Una vez terminada la clasificación anterior se verifica los largos de L1 y L2 aquí ocurren 3 casos posibles:
###          * Si L1 y L2 tienen el mismo largo el link no se puede clasificar debido a que tiene la misma cantidad de palabras en las dos categorías y se inserta en la base de datos con categoría otro, 
###          * Si L1 es mayor a L2 el link se clasifica en la primera categoría debido a que tiene mayor cantidad de palabras de esa categoría  y se inserta en la base de datos con categoría 1.  Además se aumenta el cant1 
###          * Si L2 es mayor a L1 el link se clasifica en la segunda categoría debido a que tiene mayor cantidad de palabras de esa categoría  y se inserta en la base de datos con categoría 2. Además se aumenta el cant2
###     - Una vez terminado el proceso, solicitamos la función llenarPalabrasCategorizadas para insertar por cada link las palabras categorizadas que están con todo y frecuencia en las listas LD y LS, se solicita la función de postgres y se insertan según sea el url el cual nos sirve como id, la tabla resultados tiene 5 atributos 
###          * url : Tiene la dirección web 
###          * palabras : Tiene el string completo del html de cada sitio
###          * categoría: Tiene la categoría asignada en la categorización 
###          * palabras c1: Tiene las palabras que se obtuvieron de LD con su respectiva frecuencia.
###          * palabras c2:  Tiene las palabras que se obtuvieron de LS con su respectiva frecuencia.
###          * palabras c2:  Tiene las palabras que se obtuvieron de LS con su respectiva frecuencia.
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture18.png)
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture19.png)

###     - Una vez hecho todo el proceso anterior ya podemos llamar al método bayes enviando como parámetros:
###          * Cant1 : Cantidad de links categorizados como categoría 1
###          * Cant2 : Cantidad de links categorizados como categoría 2
###          * Universo: cantidad de links totales
###          * URL: nuevo objeto para ser categorizado 
###          * ###          * ListaC1: Lista de palabras clave para la categoría 1 que están en la base de datos    
###          * ListaC2: Lista de palabras clave para la categoría 1 que están en la base de datos 
###     El método bayes es el que realiza la función principal de este proyecto aquí vamos a aplicar el segundo nivel de paralelismo, donde al ingresar un nuevo link este debe ser parseado y categorizado con  la fórmula de Bayes según la historia. El procedimiento para realizar el Bayes es el siguiente:
###          - Se calcula una probabilidad previa(pVd) de la categoría 1 esta es cant1 / universo
###          - Se calcula una probabilidad previa (pVs) de la categoría 2 esta es cant2 / universo
###          - Se realiza el webScraping solicitando la función extraer, al ejecutar esta función el resultado se guarda en la lista global en la posición 0 por lo tanto para obtener la lista del URL y las palabras de ese mismo nada más solicitamos el índice cero de la lista global de esta manera ya tenemos el html del nuevo URL, sin embargo si recordamos aún tenemos que corregir y segmentar este resultado para optimizar la búsqueda en las palabras clave, por lo tanto se implementan dos métodos 
###          * corregir Lista
###          * Segmentar Lista
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture20.png)
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture21.png)
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture22.png)
###     - Una vez segmentada y corregida la lista de palabras de nuestro nuevo URL la guardamos y generamos dos variables para contar cada palabra encontrada en la base de datos de las palabras clave:
###          * cantD: Almacena la cantidad de palabras encontradas en la categoría 1
###          * cantS: Almacena la cantidad de palabras encontradas en la categoría 2
###     - Aquí vamos a hacer el otro nivel de paralelismo donde vamos a consultar 10 palabras a la vez en las listas de categorías, los pasos para hacer esto son los siguientes:
###          * Recorremos la lista que guardamos anteriormente pero esta vez utilizamos un recorrido en rango, para esto utilizamos la función range de python, designamos que avancemos en la lista de 10 en 10 para enviar las 10 palabras al método paralelo.
###          * Guardamos las palabras en variables creadas dentro del for donde:
###               ** Palabra1 = ListaWords [ i ] 
###               ** Palabra2 = ListaWords [ i + 1 ] 
###               ** Palabra3 = ListaWords [ i + 2 ] 
###               ** Palabra4 = ListaWords [ i + 4 ] 
###               ** ……..
###               ** Palabra10 = ListaWords [ i + 9] 
### Nota: Debemos meter estas asignaciones dentro de un try debido a que si la función intenta asignar una palabra pero ya se terminaron las palabras de la lista está el método no devuelva un error de indexación.
###          * Creamos una variable para guardar el resultado de la busqueda, aquí realizamos el paralelismo enviando las 10 palabras a consultar de una vez al método verificarLis , mediante el uso de la librería Pool, el método map nos permite enviar subprocesos a una función específica de tal modo que las acciones se hagan a esos objetos al mismo tiempo, este método es más eficiente que los hilos ya que utiliza subprocesos. Lo que se va a hacer acá es lo siguiente:
###          * llamar al método map donde sus parámetros son, la función a ejecutar y la lista de objetos, en este caso lo que vamos a hacer es preguntar cuáles palabras de las 10 que enviamos están en la lista de palabras clave de categoría 1 y 2, si alguna de estas es hallada en categoría 1 devuelve un 1 y si se encuentra en la 2 devuelve un 2, las que devuelven None no se encuentran en el diccionario de palabras clave.
###          * Sin embargo necesitamos que la función sepa donde buscar estas palabras clave por lo tanto necesitamos enviar las listas con las palabras clave de categoría 1 y 2, acá debemos tener en consideración la librería partial(from functools import partial) la cual nos permite realizar el llamado de una función de multiproceso de tipo map con múltiples argumentos, los cuales no  son afectados por el proceso sino que se envían solo para comprobar las palabras, en este caso enviamos las dos listas de palabras clave de categoría 1 y 2.
###     - Solicitamos la función verificarLis dónde se reciben las dos listas con las palabras clave y las 10 palabras para ser buscadas en paralelo en un y otra lista, aquí pasan dos acciones:
###          * Si la palabra se encontró en ListaC1 se retorna un 1 
###          * Si la palabra se encontró en ListaC1 se retorna un 2
![Image text](https://github.com/IanVargas1/clasificador-bayesiano/blob/master/app/img/Picture23.png)





































