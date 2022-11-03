
import Conexion

lista = [
    'athletics', 'aerobics', 'handball', 'baseball', 'badminton', 'basketball', 'jogging', 'soccer', 'gymnastics', 'volleyball',
    'chess','cycling', 'darts', 'diving', 'fencing', 'fishing', 'golf', 'hiking', 'motor racing','long jumping','pool','parkour','mountain biking',
    'mountain bike', 'motorcycling','rugby', 'skiing','tennis', 'swimming','running','run','swim','water skiing', 'archery', 'boxing','goal','touchdown']

# Ejecutamos una consulta
def insertarcategoria(nombreTabla,lista):
    conexion = Conexion.conexion()
    cur = conexion.cursor()
    for i in lista:
        query = "INSERT INTO "+nombreTabla+"(palabraclave)values('"+i+"')"
        cur.execute(query)
    conexion.commit()
    cur.close()
    conexion.close()

def consultar():
    conexion = Conexion.conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM deportes")
    # Recorremos los resultados y los mostramos
    for objeto in cur.fetchall():
        print(objeto[1])
    cur.close()
    conexion.close()

def eliminar():
    conexion = Conexion.conexion()
    cur = conexion.cursor()
    cur.execute("truncate deportes restart identity")
    conexion.commit()
    cur.close()
    conexion.close()


def insertarResultados(url, palabras):
    palabras = str(palabras)
    conexion = Conexion.conexion()
    cur = conexion.cursor()
    cur.execute("INSERT INTO resultados(url,palabras) values('"+url+"','"+palabras+"')")
    #cur.execute("INSERT INTO resultados(url,palabras) values('addad','adaddada')")
    conexion.commit()
    cur.close()
    conexion.close()


def llenarResultador():
    lista = []
    conexion = Conexion.conexion()
    cur = conexion.cursor()
    cur.execute("select * from resultados")
    for objeto in cur.fetchall():
        lista.append(objeto)
    cur.close()
    conexion.close()
    return lista


def eliminarR():
    conexion = Conexion.conexion()
    cur = conexion.cursor()
    cur.execute("truncate resultados")
    conexion.commit()
    cur.close()
    conexion.close()




def web_site(nombreTabla):
    lista=[]
    conexion = Conexion.conexion()
    cur = conexion.cursor()
    querys= "select url from enfermo limit 3000"
    cur.execute(querys)
    for objeto in cur.fetchall():
        lista.append(objeto[0])
    for i in lista:
        query = "INSERT INTO direcciones(url)values('"+i+"')"
        cur.execute(query)
        pass
    print(lista)
    conexion.commit()
    cur.close()
    conexion.close()

#web_site("direcciones")


def consultarCategoria(nombreCategoria):
    lista = []
    conexion = Conexion.conexion()
    cur = conexion.cursor()
    cur.execute("select palabraclave from "+ nombreCategoria)

    for objeto in cur.fetchall():
        lista.append(objeto[0])
    cur.close()
    conexion.close()
    return lista

def categorizar(url, categoria):
    conexion = Conexion.conexion()
    cur = conexion.cursor()
    cur.execute("UPDATE resultados SET categoria = '"+categoria+"' WHERE url= '"+url+"';")
    conexion.commit()
    cur.close()
    conexion.close()

def llenarPalabrasCategorizadas(url,lista1, lista2):
    conexion = Conexion.conexion()
    cur = conexion.cursor()
    palabras1 = ''
    palabras2 = ''
    for i in lista1:
        palabras1 = palabras1 + str(i[0]) + " " + str(i[1]) + ";"
    for i in lista2:
        palabras2 = palabras2 + str(i[0]) + " " + str(i[1]) + ";"
    cur.execute("UPDATE resultados SET palabrasc1 = '" + palabras1 + "' WHERE url= '" + url + "';")
    cur.execute("UPDATE resultados SET palabrasc2 = '" + palabras2 + "' WHERE url= '" + url + "';")
    conexion.commit()
    cur.close()
    conexion.close()
    # print("Se insertaron con exito!!!")
    
def obtenerURLS():
    URL1 = []
    URL2 = []
    conexion = Conexion.conexion()
    cur = conexion.cursor()
    cur.execute("select * from resultados")
    for objeto in cur.fetchall():
        if objeto[2] == 'deportes':
            URL1.append(objeto[0])
        if objeto[2] == 'sexual':
            URL2.append(objeto[0])
    cur.close()
    conexion.close()
    return [URL1, URL2]



def obtenerPalabras(url):
    lista = []
    conexion = Conexion.conexion()
    cur = conexion.cursor()
    cur.execute("select * from resultados")
    for objeto in cur.fetchall():
        if objeto[0]== url:
            palabra = objeto[3].split(";")
            palabra.pop(len(palabra)-1)
            for i in palabra:
                words = []
                p = i.split()
                words.append(p[0])
                words.append(int(p[1]))
                words.append('deportes')
                lista.append(words)
            palabra = objeto[4].split(";")
            palabra.pop(len(palabra) - 1)
            for i in palabra:
                words = []
                p = i.split()
                words.append(p[0])
                words.append(int(p[1]))
                words.append('sexual')
                lista.append(words)
    cur.close()
    conexion.close()
    return lista