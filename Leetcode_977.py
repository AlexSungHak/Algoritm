#Leetcode 977
#input: sorted array / output: squares of a sorted array

def squareArr (a):
    square = []
    for i in a:
        square.append(i*i)
    
    square.sort()
    return square


print(squareArr([1, 2, 3]))