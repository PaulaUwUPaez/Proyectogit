import Libreria as lc
import math
"""Producto tensor"""
def producten(v,w):
    filasa = len(v)
    filasb = len(w)
    filasres = filasa * filasb
    res = [(0,0)] * filasres
    cuenta = 0
    for i in range(filasa):
        for j in range(filasb):
            res[cuenta] = lc.multi(v[i],w[j])
            cuenta += 1
    return res
"Hermitiana de una matriz"
def hermitiana(v):
    adj = adjuntada(v)
    if adj == v:
        return True
    return False
"Unitaria de una matriz"
def unitaria(v):
    w = multiplicarmatri(adjuntada(v),v)
    for i in range(len(w)):
        for j in range(len(w[0])):
            if i == j:
                if w[i][j] != (1,0):
                    if (round(w[i][j][0],10),round(w[i][j][1],10)) != (1,0):
                        return False
            else:
                if w[i][j] != (0,0):
                    return False
                else:
                    return True
"distancia vectores"
def distancia(v1, v2):
    resta = restamatriz(v1, v2)
    pro = productointe(resta, resta)

    if pro[1] == 0:
        return math.sqrt(pro[0])
    else:
        v3 = lc.cartetopolar(pro)
        return (math.sqrt(v3[0]), v3[1]/2)
"norma de un vector"
def norma(v):
    pro = productointe(v, v)
    if pro[1] == 0:
        return math.sqrt(pro[0])
    else:
        v2 = lc.cartetopolar(pro)
        return (math.sqrt(v2[0], v2[1]/2))
"producto interno entre vectores"
def productointe(v,w):
    return multiplicarmatri(adjuntada(v),w)[0][0]
"accion de una matriz sobre un vector"
def accion(w,v):
    return multiplicarmatri(w,v)
"multiplicar matrices"
def multiplicarmatri(v,w):
    filasv = len(v)
    columnasv = len(v[0])
    filasw = len(w)
    columnasw = len(w[0])

    if columnasv != filasw:
        raise Exception("Diferentes tamaños")
    res = [[(0,0) for i in range(columnasw)] for i in range(filasv)]

    for j in range(filasv):
        for k in range(columnasw):
            for h in range(columnasv):
                res[j][k] = lc.sum(res[j][k], lc.multi(v[j][h],w[h][k]))
    return res
"adjunta de un vector o matriz"
def adjuntada(v):
    return transpuesta(conjugadaMV(v))
"conjugado vector o matriz"
def conjugadaMV(v):
    filas = [(0,0)] * len(v[0])
    res = [filas] * len(v)

    for i in range(len(v)):
        filas = [(0,0)] * len(v[0])
        res[i] = filas
        for j in range(len(v[0])):
            res[i][j] = lc.conjugado(v[i][j])
    return res
"transpuesta de una matriz/vector"
def transpuesta(v):
    p = []
    for i in range(len(v[0])):
        p.append([])
        for j in range(len(v)):
            p[i].append(v[j][i])
    return p
"multiplicacion de una matriz por un escalar"
def matrizesca(v,w):
    p = []
    for i in range(len(v)):
        p.append([])
        for j in range(len(v[0])):
            p[i].append(0)
    for i in range(len(p)):
        for j in range(len(p[0])):
            p[i][j] = v[i][j] * w
    return p
"inverso aditivo de una matriz"
def inversamatriz(v):
    filas = len(v)
    j = 0
    res = [[] for i in range(filas)]

    while j < filas:
        res[j] = inversavector(v[j])
        j += 1
    return res
"resta entre matrices"
def restamatriz(v,w):
    if comprobación(v,w) == True and comprobación(v[0],w[0]) == True:
        filas = len(v)
        j = 0
        res =[[] for i in range(filas)]
        while j < filas:
            res[j] = restavec(v[j],w[j])
            j += 1
        return res
"suma entre matrices"
def sumamatriz(v,w):
    if comprobación(v, w) == True and comprobación(v[0], w[0]) == True:
        filas = len(v)
        j = 0
        res = [[] for i in range(filas)]

        while j < filas:
            res[j] = sumavec(v[j], w[j])
            j += 1

        return res
"multiplicacion vector y numero complejo"
def multiesca(c,v):
    long = len(v)
    mult = [(0,0) for i in range(long)]
    j = 0
    while j < long:
        mult[j] = lc.multi(c,v[j])
        j = j + 1
    return mult
"resta vectores"
def restavec(v,w):
    long = len(v)
    suma = [(0,0) for i in range(long)]
    j = 0
    while j < long:
        suma[j] = lc.resta(v[j],w[j])
        j = j + 1
    return suma
"inverso aditivo de un vector"
def inversavector(v):
    vec = [(0,0) for i in range(len(v))]
    for i in range(len(v)):
        vec[i] = ((v[i][0])*-1),((v[i][1])*-1)
    return vec
"suma vectores"
def sumavec(v,w):
    long = len(v)
    suma = [(0,0) for i in range(long)]
    j = 0
    while j < long:
        suma[j] = lc.sum(v[j],w[j])
        j = j + 1
    return suma
"verificacion de tamaños iguales"
def comprobación(v,w):
    fila1 = len(v)
    fila2 = len(w)
    return fila1 == fila2
#
def main():
    v = [(3, 7), (8, 9), (3.4, -7.8)]
    w = [(5, 6), (6, 8), (0, 0)]
    k = [[(4, 0), (1, 0), (3, 0)],
         [(2, 0), (1, 0), (2, 0)],
         [(4, 0), (1, 0), (5, 0)]]
    t = [[(1, 0), (1, 0), (2, 0)],
         [(1, 0), (2, 0), (3, 0)],
         [(2, 0), (3, 0), (1, 0)]]
    s = [[(0,2), (0,1)],
         [(1,2), (2,4)]]
    x = ([[(2, 0)], [(3, 1)], [(1, 4)]])
    d = ([[(4, 1)], [(1, 2)], [(3, 3)]])
    j = [[(6,-4),(7,9), (10,6)],
         [(7,3),(8,-5),(3,10)],
         [(4.2,8),(7,6),(7,8)]]
    u = [[(0,2), (0,1)], [(1,2), (2,4)]]
    h = [[(1,0), (1,1)], [(8,0), (0,0)]]
    p = [[(0,2), (0,1)],
         [(1,2), (2,4)]]
    l = [[6+3j],
         [0+0j],
         [5+1j],
         [4]]
    r = ([[(2, 0)], [(3, 1)], [(1, 4)]])
    e = ([[(4, 1)], [(1, 2)], [(3, 3)]])
    b = [[(2, 0)], [(3, 1)], [(1, 4)]]
    f = (([[(4, 0), (1, 0), (3, 0)], [(2, 0), (1, 0), (2, 0)], [(4, 0), (1, 0), (5, 0)]]))
    y = (([[(2, 0)], [(3, 0)], [(1, 0)]]))
    i = (([[(-5, 2), (1, -1), (7, -2)], [(2, 0), (3, 3), (-3, 5)], [(8, 10), (1, 0), (9, 5)]]))
    si = (([[(-1, 0), (0, -1)], [(0, 1), (1, 0)]]))
    ti = ([(3, 0), (1, 0)])
    fe = ([(2,1), (0,1), (2,0)])
    print(("La suma de vectores es", sumavec(v,w)))
    print(("la resta de vectores es", restavec(v, w)))
    print(("La multiplicacion de un vector y un escalar es", multiesca((2, 3),w)))
    print(("Inverso aditivo", inversavector(v)))

    c = sumamatriz(u,h)
    if c == None:
        print("No es posible la sumatoria")
    else:
        print("La suma de matrices complejas es")
        for fila in c:
            print("[", end=" ")
            for element in fila:
                print(element, end=" ")
            print("]")
    u = restamatriz(u, h)
    if u == None:
        print("No es posible la sumatoria")
    else:
        print("La resta de matrices complejas es")
        for fila in u:
            print("[", end=" ")
            for element in fila:
                print(element, end=" ")
            print("]")
    h = 3+2j
    q = matrizesca(l,h)
    if q == None:
        print("No es posible la multiplicación")
    else:
        print("La multiplicacion de un escalar con matriz es")
        for fila in q:

            print("[", end=" ")
            for element in fila:
                print(element, end=" ")
            print("]")
    trans = transpuesta(j)
    print("La transpuesta de la matriz es")
    for linea in trans:
        for element in linea:
            print(element, end=" ")
        print()
    print(("el inverso aditivo de la matriz es", inversamatriz(p)))
    print(("El conjugado es", conjugadaMV(s)))
    print(("La adjunta daga es ", adjuntada(s)))
    print(("multiplicar matrices ", multiplicarmatri(k,t)))
    print(("la accion de la matriz ", accion(f,y)))
    print(("el producto interno ", productointe(x,d)))
    print(("la norma es ", norma(b)))
    print(("la distancia es ", distancia(r,e)))
    print(("la unitaria es ", unitaria(i)))
    print(("la hermitiana es ", hermitiana(si)))
    print(("El producto tensor es ", producten(ti,fe)))


main()
