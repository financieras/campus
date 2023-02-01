from random import seed, choice
seed()
def sa(a,b):
    if len(a) > 1: a[0],a[1] = a[1],a[0]
    return a,b
def sb(a,b):
    if len(b) > 1: b[0],b[1] = b[1],b[0]
    return a,b
def ss(a,b):
    sa(a,b)
    sb(a,b)
    return a,b
def pa(a,b):
    if len(b) > 0:
        a.insert(0, b[0])
        b.pop(0)
    return a,b
def pb(a,b):
    if len(a) > 0:
        b.insert(0, a[0])
        a.pop(0)
    return a,b
def ra(a,b):
    if len(a) > 1: a.append(a.pop(0))
    return a,b
def rb(a,b):
    if len(b) > 1: b.append(b.pop(0))
    return a,b
def rr(a,b):
    ra(a,b)
    rb(a,b)
    return a,b
def rra(a,b):
    if len(a) > 1: a.insert(0, a.pop())
    return a,b
def rrb(a,b):
    if len(b) > 1: b.insert(0, b.pop())
    return a,b
def rrr(a,b):
    rra(a,b)
    rrb(a,b)
    return a,b

if __name__ == "__main__":
    a_original = [2, 6, 1, 8, 7, 10, 9, 3, 4, 5]
    b_original = []
    a_ordenada = sorted(a_original)
    catalogo = ["sa","sb","pa","pb","ra","rb","rra","rrb", "ss","rr","rrr"]
    print('\ta: ', a_original)
    print('\tb: ', b_original)
    #mejor_respuesta = [None]*(100+len(a_original)**3)
    mejor_respuesta = ['pb', 'ra', 'pb', 'ss', 'ra', 'ra', 'sa', 'rr', 'rr', 'pa', 'pa']
    len_mejor = len(mejor_respuesta)
    las_mejores = []
    while True:
        instrucciones = []
        a = a_original[:]
        b = b_original[:]
        buscando = True
        while a != a_ordenada and buscando:
            instruccion = choice(catalogo)
            instrucciones.append(instruccion)
            if len(instrucciones) > len_mejor: buscando = False
            if instruccion=="sa": sa(a,b)
            elif instruccion=="sb": sb(a,b)
            elif instruccion=="ss": ss(a,b)
            elif instruccion=="pa": pa(a,b)
            elif instruccion=="pb": pb(a,b)
            elif instruccion=="ra": ra(a,b)
            elif instruccion=="rb": rb(a,b)
            elif instruccion=="rr": rr(a,b)
            elif instruccion=="rra": rra(a,b)
            elif instruccion=="rrb": rrb(a,b)
            elif instruccion=="rrr": rrr(a,b)
        #print("Las instrucciones:", instrucciones)
        len_mejor = len(mejor_respuesta)
        if len(instrucciones) <= len_mejor:
            if instrucciones not in las_mejores:
                mejor_respuesta = instrucciones
                las_mejores.append(mejor_respuesta)
                print("*", mejor_respuesta)
