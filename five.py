#   project euler
#   bradley smith
#   problem five
#   start: 1/15/2019
#   completed: 2/11/2019
#   language: python 2.7

#   problem statement:
#       2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#       what is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


#   notes:


import fractions 

def divisor(x,y):

	# while y != 0:

	# 	x, y = y, x % y

	# 	return x 

	ans = x 

	for i in range(1, y + 1): 
		ans = (ans * i ) / fractions.gcd(ans, i)

	return ans 



print(divisor(1, 20))





        