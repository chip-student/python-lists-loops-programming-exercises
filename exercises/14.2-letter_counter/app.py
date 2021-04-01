par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

def remove(string):
    return string.replace(" ", "")

counts = {}

# Using for loop
cadena = remove(par)
for char in cadena:
    if char.lower() in counts:  
        counts[char.lower()] += 1    
    else:
        counts[char.lower()] = 1
    
print(counts)






