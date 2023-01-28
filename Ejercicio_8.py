import heapq
def hacer_arbol(probs):
    q=[]
    for caracter,prob in probs.items():
        heapq.heappush(q,(prob,0,caracter))
    while len(q) > 1:
        elemento1 = heapq.heappop(q)
        elemento2 = heapq.heappop(q)
        nuevo_nodo = (elemento1[0] + elemento2[0],max(elemento1[1],elemento2[1]) + 1, [elemento1, elemento2])
        heapq.heappush(q,nuevo_nodo)
    return q[0]

        

if __name__ == '__main__':
    probs = {}
    probs['3'] = 0.21
    probs['A'] = 0.2
    probs['F'] = 0.17
    probs['T'] = 0.15
    probs['1'] = 0.13
    probs['M'] = 0.09
    probs['0'] = 0.05
    for elemento in hacer_arbol(probs):
        print(elemento)