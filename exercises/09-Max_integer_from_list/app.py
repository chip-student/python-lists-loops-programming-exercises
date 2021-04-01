my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]


#Your code go from here:
aux = 0

for x in range(0, len(my_list)): 
    if my_list[x] > aux: 
        aux = my_list[x]
    

print(aux)
