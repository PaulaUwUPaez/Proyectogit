#Escuela Colombiana de ingeniera Julio Garabito
#Ing sistemas
#Manuel Felipe Barrera Barrera

import vectoresprueba as uso


def slitmatrix(matrizadyacente, clic):
    repeticiones = 1
    resultado = matrizadyacente
    while repeticiones < clic:
        resultado = uso.multiplicacionMatrices(resultado, matrizadyacente)
        repeticiones += 1
    return resultado

def slitvector(resultado, posicion):
    vector_repeticion = uso.accion(resultado, posicion)
    return vector_repeticion
def main():
    matrizadyacencia = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
    [(1/sqrt(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
    [(1/sqrt(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
    [(0,0),(-1/sqrt(6),1/sqrt(6)),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
    [(0,0),(-1/sqrt(6),-1/sqrt(6)),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
    [(0,0),(1/sqrt(6),-1/sqrt(6)),(-1/sqrt(6),1/sqrt(6)),(0,0),(0,0),(1,0),(0,0),(0,0)],
    [(0,0),(0,0),(-1/sqrt(6),-1/sqrt(6)),(0,0),(0,0),(0,0),(1,0),(0,0)],
    [(0,0),(0,0),(1/sqrt(6),-1/sqrt(6)),(0,0),(0,0),(0,0),(0,0),(1,0)]]
    estatus = [[(1,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)]]

    print(slitmatrix(matrizadyacencia,2))
    print("------")
    print(slitvector(slitmatrix(matrizadyacencia,2),estatus))
main()
