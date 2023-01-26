from random import sample, seed
seed()

def lista_ordenada(l):
    estaordenada = False
    aux = l[:]
    aux.sort()
    if (aux == l):
        estaordenada = True
    return estaordenada

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
    # Generación de la pila a
    n = 5   # número de elementos de la pila
    a = sample(range(1, n+1), n)
    #a = [17, 5, 13, 20, 6, 12, 4, 3, 7, 18, 1, 14, 8, 10, 16, 2, 11, 15, 19, 9]   # valores de ejemplo
    a_original = a[:]
    b = []
    #print('a:', a)
    #print('b:', b)
    contador = 0
    while len(a)>1:   # se repite hasta que solo quede un elemento en la pila a
        # buscamos el mínimo y vamos haciendo ra hasta que el mínimo esté el primero
        while min(a) != a[0]:
            ra(a,b); contador += 1
        pb(a,b); contador += 1 # luego hacemos pb
    # luego se hace pa pa pa pa hasta que no quede nadie en la pila b
    while len(b)>0:
        pa(a,b); contador += 1
    
    #print('a:', a)
    #print('b:', b)
    print("contador:", contador)

    ### PROCEDIMIENTO MEJORADO
    contador = 0
    a = a_original[:]
    print(a)
    while len(a) > 1 and not lista_ordenada(a):   # se repite hasta que solo quede un elemento en la pila a
        # buscamos el mínimo y vamos haciendo ra o rra hasta que el mínimo esté el primero
        while min(a) != a[0]:
            #print("min(a)=", min(a))
            if a.index(min(a)) <= int(len(a)/2):
                #print(min(a))
                #print("index del min y mitad:", a.index(min(a)), int(len(a)/2))
                ra(a,b)
            else:
                rra(a,b)
            contador += 1
            print(a,b)
        if not lista_ordenada(a):
            pb(a,b); contador += 1; print(a,b) # luego hacemos pb
    # luego se hace pa pa pa pa hasta que no quede nadie en la pila b
    while len(b) > 0:
        pa(a,b); contador += 1; print(a,b)
    print("contador:", contador)
