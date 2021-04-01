people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    myArray = []
    for i in range(0, len(people)):
        if people[i] != person_name:
            myArray.append(people[i])
    return myArray
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))