arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumOdds():
    total = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 != 0:
            total += arr[i]
    print(str(total))
    
sumOdds() 


