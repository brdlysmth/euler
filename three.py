#   project euler
#   bradley smith
#   problem three
#   start: 1/11/2019
#   completed: 1/11/2019
#   language: python 2.7

#   problem statement:
#       the prime factors of 13195 are 5, 7, 13 and 29. 
#       what is the largest prime factor of the number 600851475143 ?

import math

def largestPrimeFactor(n):

    while n % 2 == 0:
        print 2
        n = n / 2 
    
    for i in range(3, int(math.sqrt(n)), 2):
        while n % i == 0:
            print i 
            n = n / i 


largestPrimeFactor(13195)
largestPrimeFactor(600851475143)
