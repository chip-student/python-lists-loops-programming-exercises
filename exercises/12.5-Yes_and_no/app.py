theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
cadena = []
def Bools(item):
    if item ==1:
        cadena='wiki'
    else:
        cadena ='woko'
    return cadena

print(list(map(Bools,theBools)))

