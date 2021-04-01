

# Your code go above, nothing to change after this line:
def lyrics_generator(arr):
    result =""
    cont = 0
    for i in range(0, len(arr)):
        if arr[i] == 0: 
            result += 'Boom '
        else:
            cont += 1
            result += 'Drop the base '
            if cont == 3:
                result += '¡¡¡Break the base!!! '
    return result

print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))

