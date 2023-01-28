def hijo_sin_amor(mochila,objeto):
    return hijo_sin_amor_rec(mochila, objeto, 0)

def hijo_sin_amor_rec(mochila,objeto,contador):
    if len(mochila) > 0:
        if mochila[0] == objeto:
            return contador
        else:
            return hijo_sin_amor_rec(mochila[1:],objeto,contador+1)
    else:
        return  -1 #pasará si el objeto no está en la mochila

mochila = ['Pistola', 'Guantes', 'Metralleta', 'usar la ayuda del dios Kukulcán']
print(hijo_sin_amor,(mochila,'usar la ayuda del dios  Kukulcán'))