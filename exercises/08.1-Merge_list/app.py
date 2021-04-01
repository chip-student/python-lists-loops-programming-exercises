chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    newArray = []
    for i in range(0, len(list1)):
        newArray.append(list1[i])
    for i in range(0, len(list2)):
        newArray.append(list2[i])
    return newArray
    
print(merge_list(chunk_one, chunk_two))
