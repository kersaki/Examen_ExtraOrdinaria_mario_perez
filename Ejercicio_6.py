def menor(e1):
    return e1[2] 
def mochila(precio, peso, peso_maximo):
    array_ordenado = []
    for i in range(len(precio)):
        array_ordenado.append([precio[i],peso[i],precio[i]/peso[i]])# ej: [103,12,0]
    array_ordenado.sort(key=menor, reverse= True)
    valor_total = 0
    for elemento in array_ordenado:
        if peso_maximo - elemento[1] >= 0:
            peso_maximo -= elemento[1]
            valor_total += elemento[0]
    return valor_total

if __name__ == '__main__':
    precio = [103, 60, 70, 5, 15]
    peso = [12, 23, 11, 15, 7]
    peso_maximo = 100
    print(mochila(precio,peso,peso_maximo))
