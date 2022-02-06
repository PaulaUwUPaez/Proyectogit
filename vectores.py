import libreria as lc
#import libreria as lc
def sumavec(v,w):
    long = len(v)
    suma = [(0,0) for i in range(long)]
    j = 0
    while j < long:
        suma[j] = lc.sum(v[j],w[j])
        j = j + 1
    return suma
def multiesca(c,v):
    long = len(v)
    mult = [(0,0) for i in range(long)]
    j = 0
    while j < long:
        mult[j] = lc.multi(c,v[j])
        j = j + 1
    return mult
def main():
    v = [(3, 7), (8, 9), (3.4, -7.8)]
    w = [(5, 6), (6, 8), (0, 0)]
main()
