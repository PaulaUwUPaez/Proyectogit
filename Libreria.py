#Manuel Felipe Barrera
#Escuela colombiana de ingeniera
#Ing sistemas
import math
"multiplicacion coordenadas polares"
def multiplicacionpolar(c1,c2):
    magnitud = c1[0] * c2[0]
    phase = c1[1] + c2[1]
    return (magnitud, phase)
"conversion cartesiana a polar"
def cartetopolar(c1):
    return (modulo(c1), fase(c1))
"conversion polar a cartesiana"
def polartocarte(c1):
    x = c1[0] * math.cos(c1[1])
    y = c1[0] * math.sin(c1[1])
    return (x, y)
"fase de vector"
def fase(c1):
    return math.atan(c1[1]/c1[0])
"conjugado vector"
def conjugado(c1):
    real = c1[0]
    imagina = -c1[1]
    return (real,imagina)
"modulo vectores"
def modulo(a):
     return (a[0] ** 2 + a[1] ** 2) **(1/2)
"division vectores"
def div(c1,c2):
    Re = (c1[0] * c2[0] + c1[1] * c2[1]) / (c2[0]**2 + c2[1] **2)
    Im = (c2[0] * c1[1] - c1[0] * c2[1]) / (c2[0]**2 + c2[1] **2)
    return(Re, Im)
"multiplicacion vectores"
def multi(c1,c2):
    real = c1[0]*c2[0] - c1[1]*c2[1]
    imagina = c1[0]*c2[1] + c1[1]*c2[0]
    return (real, imagina)
"resta de vectores"
def resta(c1,c2):
    return (c1[0]-c2[0],c1[1]-c2[1])
"sumatoria de vectores"
def sum(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])
def main():
    print("suma", sum((3.5,7),(4.2,8))) #(3.5 + 7i) + (4.2 + 8i) = (7.7 + 15i)
    print("resta", resta((4, 4), (4, 2))) #(4 - 4),(4i - 2i) = (0,2i)
    print("multiplicación", multi((3, -1) ,(1,4))) #(3 - 1) * (1 + 4i) = (7 + 11i)
    print("division", div((-2,-1),(1,2))) #(-2 - 1i) / (1 + 2i) = ( 0 + 1i)
    print("modulo", modulo((1,-1))) #(1 - 1i) = 1.41
    print("conjugado", conjugado((1,-1))) #(1 - 1j) = (1 + 1j)
    fase ((1,1)) #(1 + 1i) = 45°
    polartocarte((1,1)) #(1 + 1i) = (1,41,45)
    print("Cartesianas hacia polares", cartetopolar((1.41,45))) #(1.41,45) = (1 + 1i)
    print("multiplicacion coordenadas polares", multiplicacionpolar((4,-3),(4,3)))
