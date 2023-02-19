# FUNCIONES
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

from random import sample, seed
seed()

def generaPilaA(n):
    return sample(range(1, n+1), n)

# Llevamos de la pila A hacia la pila B los elementos de la LIS
def rotateLIS(lis):
    global a
    global b
    global contador
    for vlis in lis:
        if a.index(vlis) < len(a)/2:
            for i in range(a.index(vlis)):
                ra(a,b); contador += 1
        else:
            for i in range(len(a)- a.index(vlis)):
                rra(a,b); contador += 1
        pb(a,b); contador += 1

# PASOS NECESARIOS PARA COLOCAR CADA ELEMENTO DE A EN SU SITIO EN B      total = pasosA + pasosB

def necesariosA(a, b):   # array pasosA calcula los pasos necesarios para colocar cada elemento de A como el primero de su pila
    for i in a:
        if a.index(i) < len(a)/2:
            pasosA.append(a.index(i))
        else:
            pasosA.append(-(len(a)- a.index(i)))

def necesariosB(a,b):   # array pasosB calcula los pasos de B necesarios para colocar cada elemento de A dentro de su sitio en B
    for v in a:
        try:
            objetivo_primero = max([x for x in b if x<v])
        except:
            objetivo_primero = max(b)   # objetivo_primero calcula el número que se ha de poner en la primera posición de B

        if b.index(objetivo_primero) < len(b)/2:
            pasosB.append(b.index(objetivo_primero))
        else:
            pasosB.append(-(len(b)- b.index(objetivo_primero)))

def totaliza(a,b):   # totalizar pasos
    global total
    for i in range(len(pasosA)):
        if pasosA[i] * pasosB[i] < 0:   # si son de distinto signo
            total.append(abs(pasosA[i]) + abs(pasosB[i]))
        else:
            total.append(max(abs(pasosA[i]), abs(pasosB[i])))

def calculaIndexPasosMinimos():
    global pasosA
    global pasosB
    global total
    pasosA = []   # [0,1,2, ...,41,-41,... , -2,-1]  vector donde cada index está asociado con el valor del mismo index en A
    pasosB = []   # [-3,2,-5, ..., -5,0]   estos dos arrays se han de recalcular cada vez que realmente se mueva algún elemento de A a B
    total = []
    necesariosA(a, b)
    necesariosB(a, b)
    totaliza(a,b)
    return total.index(min(total))   # retorna el índice del elemento de la pila A que menos pasos totales necesita


def giraA(a, b, indice, pasos):
    global contador
    for i in range(abs(pasos)):
        if pasos > 0:
            ra(a,b); contador += 1
        elif pasos < 0:
            rra(a,b); contador += 1

def giraB(a, b, indice, pasos):
    global contador
    for i in range(abs(pasos)):
        if pasos > 0:
            rb(a,b); contador += 1
        elif pasos < 0:
            rrb(a,b); contador += 1

# girando pilas A y B
def giraPilas(a,b,indice):   # indice es el index del valor en la pila A que deseamos poner el primero
    global contador
    if pasosA[indice] * pasosB[indice] > 0:   # Existe sinergia, nos podemos ahorrar pasos
        pasos_comunes = min(abs(pasosA[indice]), abs(pasosB[indice]))
        for i in range(pasos_comunes):
            if pasosA[indice] > 0:   # si el signo de ambos es positivo, ya que ambos tienen el mismo signo
                rr(a,b); contador += 1
            elif pasosA[indice] < 0: # si el signo de ambos es negativo
                rrr(a,b); contador += 1
        exceso_pasosA = abs(pasosA[indice]) - pasos_comunes
        exceso_pasosB = abs(pasosB[indice]) - pasos_comunes
        giraA(a, b, indice, ((pasosA[indice] > 0) - (pasosA[indice] < 0)) * exceso_pasosA)    # (a > 0) - (a < 0) da el signo de a
        giraB(a, b, indice, ((pasosB[indice] > 0) - (pasosB[indice] < 0)) * exceso_pasosB)   # Python no tiene función sign
    else:   # No existe sinergia
        giraA(a ,b, indice, pasosA[indice])   # gira A
        giraB(a, b, indice, pasosB[indice])   # gira B

def situarMax_en_B():
    indice = b.index(max(b))
    if indice < len(a)/2:
        pasos = indice
    else:
        pasos = -(len(b)- indice)
    giraB(a, b, indice, pasos)

def subirTodo_a_A():
    global contador
    for _ in range(len(b)):
        pa(a,b); contador += 1

def establece_lis(arr):   # esta función solo se debería invocar una vez. Proporciona una matriz con listas de posibles lis
    m2 = [[0,1],[0,-1],[0,2],[0,-2],[0,3],[0,-3],[1,-1],[1,2],[1,-2],[1,3],[1,-3],[-1,2],[-1,-2],[-1,3],[-1,-3],[2,-2],[2,3],[2,-3],[-2,3],[-2,-3],[3,-3]]
    posibles_lis = []
    for pareja in m2:   # m2 tiene 21 parejas
        x,y = pareja[0], pareja[1]
        lis = [arr[x], arr[y]]
        posibles_lis.append(lis)

    m3 = [[0,1,-1],[0,1,2],[0,1,-2],[0,1,3],[0,1,-3],[0,-1,2],[0,-1,-2],[0,-1,3],[0,-1,-3],[0,2,-2],[0,2,3],[0,2,-3],[0,-2,3],[0,-2,-3],[0,3,-3],[1,-1,2],[1,-1,-2],[1,-1,3],[1,-1,-3],[1,2,-2],[1,2,3],[1,2,-3],[1,-2,3],[1,-2,-3],[1,3,-3],[-1,2,-2],[-1,2,3],[-1,2,-3],[-1,-2,3],[-1,-2,-3],[-1,3,-3],[2,-2,3],[2,-2,-3],[2,3,-3],[-2,3,-3]]
    for trio in m3:   # m3 tiene 35 trios, total len(m2)+len(m3)=21+35=56 casos posibles de lis 
        x,y,z = trio[0], trio[1], trio[2]
        lis = [arr[x], arr[y], arr[z]]
        posibles_lis.append(lis)
    return posibles_lis

if __name__ == "__main__":    
    n = 500   # número de elementos de la pila
    limite = 5500   # para n=100 limite<700, para n=500 limite<5500
    n_intentos = [0]*56   # array que contará los intentos de tipo cero, uno, dos, tres,....
    for i in range(10000):
        a = generaPilaA(n)
        b = []
        a_original = a[:]
        n = len(a)
        posibles_lis = establece_lis(a)   # llama a la función que proporciona una matriz con las posibles lis de dos o tres números de la pila A
        intento = 0   # contador con los intentos probando diferentes lis
        while True:
            a = a_original[:]
            b = []
            lis = posibles_lis[intento]  # establece lis por ejemplo: lis = [a[0], a[1]]
            contador = 0
            rotateLIS(lis)
            while len(a) > 0:
                index_minimosPasos = calculaIndexPasosMinimos()
                giraPilas(a,b,index_minimosPasos)
                pb(a,b); contador += 1 # lo pasa de A a B haciendo pb
            situarMax_en_B()
            subirTodo_a_A()
            if contador < limite:
                n_intentos[intento] += 1
                if intento > 5:
                    print("intento:", intento, "LIS:", lis, "contador:", contador, "a:", a_original, "\n")
                break
            intento += 1
            #print(f"La pila A {'SI' if sorted(a_original)==a else 'No' } está ordenada.")
            #print(f"contador: {contador}")
        if i%1000==0:
            print(i, n_intentos[:9])
    print(n_intentos)