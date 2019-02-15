#   project euler
#   bradley smith
#   problem one 
#   start: 1/9/2019
#   completed: 1/9/2019
#   language: python 2.7

#   problem statement:
#       if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#       the sum of these multiples is 23.
#       find the sum of all the multiples of 3 or 5 below 1000.

#   notes:
#       input target number
#       divide by 5, find numbers where remainder is zero
#       place those numbers in an array 
#       divide by 3, find number where remainder is zero
#       add those numbers to the array
#       sum all of the numbers in the array

# x = 1000
# y = 1000 / 5                                        # regular divisor floors the number
# z = 1000 / 3   

#   '%' --- the 'modulo' operator yields the remainder from the division of the first object into the second

# print x, y, z 

def problemOne(targetInt):

    arr = []
    for i in range(0,targetInt):
        a = i % 5                                       # if using 5.0 answer will auto-floating point                                               
        b = i % 3    
        if a == 0 or b == 0:
            arr.append(i)      
        # print a 
    print arr
    ans = sum(arr)
    # print ans
    return ans 

print problemOne(1000)


