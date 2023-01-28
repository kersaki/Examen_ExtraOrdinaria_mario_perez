import random
lista_parejas = ['FL','TF','TK','CT','FN','FO']
class Lista():
    def __init__(self):
        self.l=[]

class Armaduras():
    def __init__(self, nombre, rango):
        self.nombre=nombre
        self.rango=rango
        self.codigo_legion=''
        self.id_cohorente=''
        self.id_siglo=''
        self.numero_armadura=''
        self.numero_escuadra=''
        print('armadura creada')

    def calificador(self):
        self.codigo_legion=lista_parejas[random.randint(0,len(lista_parejas)-1)]
        self.id_cohorente=''+ str(random.randint(1,9))
        self.id_siglo=''+ str(random.randint(1,9))
        self.numero_armadura=''+str(random.randint(1,9))
        self.numero_escuadra=''+str(random.randint(1,9))
    
    
    
    def __str__(self):
        return 'La Armadura se llama {}, tiene rango {} y su calificacion es {}-{}{}{}{}'.format(self.nombre, self.rango, self.codigo_legion,self.id_cohorente,self.id_siglo,self.numero_armadura,self.numero_escuadra)

def crear_tabla(tamaño):
    tabla=[None]*tamaño
    return tabla

def tamaño(lista):
    return len(lista.l)

def cantidad_elementos(tabla):
    return sum(tamaño(lista) for lista in tabla if lista is not None)

def funcion_hash(dato,tamaño_tabla):
    #return len(str(dato).strip()) % tamaño_tabla
    if dato.codigo_legion == 'FL':
        return 0
    elif dato.codigo_legion == 'TF':
        return 1
    elif dato.codigo_legion == 'TK':
        return 2
    elif dato.codigo_legion == 'CT':
        return 3
    elif dato.codigo_legion == 'FN':
        return 4
    else:
        return 5

def funcion_hash_2(dato,tamaño_tabla):
    numero=int(dato.id_siglo) * 100 + int(dato.numero_armadura)*10 + int(dato.numero_escuadra)
    return numero % tamaño_tabla

def insertar(lista,dato):
    lista.l.append(dato)

def agregar(tabla,dato):
    posicion=funcion_hash(dato,len(tabla))
    if tabla[posicion] is None:
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato)

def agregar2(tabla,dato):
    posicion=funcion_hash_2(dato,len(tabla))
    if tabla[posicion] is None:
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato)

def busqueda(lista,dato):
    return dato in lista.l

def buscar(tabla,buscado):
    pos = None
    posicion=funcion_hash(buscado, len(tabla))
    if tabla[posicion] is not None:
        pos = busqueda(tabla[posicion], buscado)
    return pos

def buscar2(tabla,buscado):
    pos = None
    posicion=funcion_hash_2(buscado, len(tabla))
    if tabla[posicion] is not None:
        pos = busqueda(tabla[posicion], buscado)
    return pos

def lista_vacia(lista):
    return len(lista.l)==0

def eliminar(lista,dato):
    return lista.l.pop(dato)

def quitar(tabla,dato):
    dato=None
    posicion= funcion_hash(dato, len(tabla))
    if tabla[posicion] is not None:
        dato = eliminar(tabla[posicion], dato)
        if lista_vacia(tabla[posicion]):
            tabla[posicion] = None
    return dato

if __name__ == '__main__':
    lista=[]
    tabla2=crear_tabla(1000)
    tabla=crear_tabla(6)
    ST_auxiliar=None
    for i in range(0,2000):
        armadura=Armaduras('MK'+str(i), i)
        armadura.calificador()
        if armadura.codigo_legion=='FN' and armadura.id_cohorente=='2' and armadura.id_siglo=='1' and armadura.numero_armadura=='8' and armadura.numero_escuadra=='7':
            ST_auxiliar = armadura
        lista.append(armadura)
        print(lista[i])
        agregar(tabla,armadura)
        agregar2(tabla2,armadura)
    print(tabla2)
    for elemento in tabla:
        for dato in elemento.l:
            print(dato)
    if ST_auxiliar is not None:
        print(buscar2(tabla2,ST_auxiliar))
    