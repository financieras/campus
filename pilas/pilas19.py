from funciones import *

def separa_valor(v):
    posicion = v.find('|')
    a_str = v[:posicion]
    b_str = v[posicion+1:]
    a = [int(num) for num in a_str.split()]   # [4, 3, 2, 1]
    b = [int(num) for num in b_str.split()]
    return a, b

def agrega(k, instruccion, aCopy, bCopy):
    pareja = ' '.join([str(x) for x in aCopy]) + "|" + ' '.join([str(x) for x in bCopy])   # '3 4 2 1|'
    tupla = tuple([str(instruccion)])
    if pareja not in d.values():
        d[k+tupla] = pareja

def busca(a,b):    # Estas son a y b: [4, 3, 2, 1] []
    global d
    while valor_ordenado not in d.values():
        nivel = max([len(k) for k in d.keys()])   # el nivel del árbol es igual a la máxima longitud de las tuplas que van como clave en el diccionario. Inicialmente el nivel=0
        d_nivel = {}   # inicializamos un diccionario que copia d pero solo los items que sean del nivel máximo en ese momento
        for k,v in d.items():
            if len(k) == nivel:
                d_nivel[k] = v

        for k,v in d_nivel.items():
            a, b = separa_valor(v)
        
            for i in moves:
                if (i == "sa"): aCopy, bCopy = sa(a[:], b[:])
                elif (i == "sb"): aCopy, bCopy = sb(a[:], b[:])
                elif (i == "ss"): aCopy, bCopy = ss(a[:], b[:])
                elif (i == "pa"): aCopy, bCopy = pa(a[:], b[:])
                elif (i == "pb"): aCopy, bCopy = pb(a[:], b[:])
                elif (i == "ra"): aCopy, bCopy = ra(a[:], b[:])
                elif (i == "rb"): aCopy, bCopy = rb(a[:], b[:])
                elif (i == "rr"): aCopy, bCopy = rr(a[:], b[:])
                elif (i == "rra"): aCopy, bCopy = rra(a[:], b[:])
                elif (i == "rrb"): aCopy, bCopy = rrb(a[:], b[:])
                elif (i == "rrr"): aCopy, bCopy = rrr(a[:], b[:])
                agrega(k, i, aCopy, bCopy)

if __name__ == "__main__":   # Este código funciona con números no correlativos, grandes, negativos y cero. Para n=6 tarda 4 segundos aprox.
    a_str = "6 5 4 3 2 1"  # este ejemplo equivale a "2147483647 32767 4 0 -32768 -2147483648"
    moves = ["sa","sb","pa","pb","ra","rb","rra","rrb","ss","rr","rrr"]
    d = {(): a_str + "|"}   # diccionario. Ejemplo: {():'4 3 2 1|', ('sa',):'3 4 2 1|', ('pb',):'3 2 1|4', ('ra',):'3 2 1 4|', ('rra',):'1 4 3 2|', ('pb', 'sa'):'2 3 1|4', ('pb', 'pb'):'2 1|3 4'}
    a = [int(num) for num in a_str.split()]   # [4, 3, 2, 1]
    b = []
    valor_ordenado = ' '.join(map(str, sorted(a))) + '|'   #  "1 2 3 4|"
    busca(a,b)
    print(list(d.keys())[list(d.values()).index(valor_ordenado)])   # da la clave que corresponde al valor ordenado "1 2 3 4|"
    #print(d)   # imprime el diccionario completo