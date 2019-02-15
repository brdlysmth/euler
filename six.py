#   project euler
#   bradley smith
#   problem six
#   start: 2/15/2019
#   completed: 2/15/2019
#   language: python 2.7

#   problem statement:
#      The sum of the squares of the first ten natural numbers is,
#                   1^2 + 2^2 + ... + 10^2 = 385
#      The square of the sum of the first ten natural numbers is,
#                   (1 + 2 + ... + 10)^2 = 552 = 3025
# 
#      Hence the difference between the sum of the squares of the first ten natural numbers 
#      and the square of the sum is 3025 - 385 = 2640 
#      
#      Find the difference between the sum of the squares of the first one hundred natural 
#      numbers and the square of the sum.


#   notes:


def sumVsquares(n):

    sum1 = 0 
    sum2 = 0 
    diff = 0 
    i = 0

    while i <= n:
        # print i
        sum1 = sum1 + i 
        sum2 = sum2 + i**2

        i += 1

        
    sum1 = sum1**2

    diff = sum1 - sum2 
    
    return diff


print(sumVsquares(100))
