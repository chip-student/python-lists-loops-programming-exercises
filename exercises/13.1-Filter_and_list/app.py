
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def my_function(items):
    for i in range(0,len(items)):
        if items[i][0] == "R":
            return items[i]

resulting_names=list(filter(my_function, all_names))
print(resulting_names)




