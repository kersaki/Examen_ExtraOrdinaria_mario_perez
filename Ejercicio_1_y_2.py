import random
class Armaduras():
    def __init__(self,nombre,rango):
        self.nombre=nombre
        self.rango=rango
        self.codigo_legion='MK'
        self.id_coherente=''
        self.id_siglo=''
        self.num_aramdura=''
        self.num_escuadra=''
    
    def calificacion(self):
        self.codigo_legion='MK'
        self.id_coherente=''+str(random.randint(0,9))
        self.id_siglo=''+str(random.randint(0,9))
        self.num_aramdura=''+str(random.randint(0,9))
        self.num_escuadra=''+str(random.randint(0,9))

    def __str__(self):
        return 'La armadura se llama {}, tiene rango {} y su calificación es {}-{}{}{}{}'.format(self.nombre,self.rango,self.codigo_legion,self.id_coherente,self.id_siglo,self.num_aramdura,self.num_escuadra)

if __name__ == '__main__':
    lista = []
    for i in range(0,random.randint(1,10)):#Estoy generando un numero arbitrario de armaduras de 1 a 10
        armadura = Armaduras('MK'+str(i), i)
        armadura.calificacion()
        lista.append(armadura)
        print(lista[i])
