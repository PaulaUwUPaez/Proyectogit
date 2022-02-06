#Manuel Felipe Barrera
#Escuela colombiana de ingeniera
#Ing sistemas
import math
"conversion cartesiana a polar"
def cartetopolar(c1,c2):
    u = (round((c1)*math.cos(c2)))
    m = (round((c1)*math.sin(c2)))
    return (u , m)
"conversion polar a cartesiana"
def polartocarte(c1,c2):
    c = (math.atan(c2 / c1))
    print("Polares a cartesianas (",round(((((c1) ** 2) + ((c2) ** 2)) ** (1 / 2)), 2),",", round(((c * (180 / (3.14))))),")")
"fase de vector"
def fase(c1,c2):
    c = (math.atan(c2/c1))
    print("Fase en grados", round(((c * (180 / (3.14))))))
"conjugado vector"
def conjugado(c2):
    return (c2.conjugate())
"modulo vectores"
def modulo(a,c):
     return round(((((a)**2)+((c)**2))**(1/2)),2)
"division vectores"
def div(c1,c2):
    Re = (c1[0] * c2[0] + c1[1] * c2[1]) / (c2[0]**2 + c2[1] **2)
    Im = (c1[1] * c1[1] - c1[0] * c2[1]) / (c2[0]**2 + c2[1] **2)
    return(Re, Im)
"multiplicacion vectores"
def multi(c1,c2):
    return ((c1[0]*c2[0]) - (c1[1]*c2[1]), (c1[0]*c2[1]) + (c1[1]*c2[0]))
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
    print("modulo", modulo(1,-1)) #(1 - 1i) = 1.41
    print("conjugado", conjugado(1 - 1j)) #(1 - 1j) = (1 + 1j)
    fase (1,1) #(1 + 1i) = 45°
    polartocarte(1,1) #(1 + 1i) = (1,41,45)
    print("Cartesianas hacia polares", cartetopolar(1.41,45)) #(1.41,45) = (1 + 1i)
main()