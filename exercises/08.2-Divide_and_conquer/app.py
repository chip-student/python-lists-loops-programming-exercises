list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]

even = []
odd = []
#Your code here:
def merge_two_list(list):
    for i in range(0 , len(list)):
        if list[i] % 2 != 0:
            odd.append(list[i])
        else:
            even.append(list[i])
        
    odd.extend(even)
    return odd

print(merge_two_list(list_of_numbers))

