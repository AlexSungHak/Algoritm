#Leetcode 258 Add Digits
#input: 38 / output: 2

def addDigits(self, num):
    if num == 0:
        return 0
    
    else:
        return (num -1) % 9 + 1