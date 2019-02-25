#   project euler
#   bradley smith
#   problem seven
#   start: 2/25/2019
#   completed: 2/25/2019
#   language: python 2.7

#   problem statement:
#
#		By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#		What is the 10 001st prime number?
#    

#   notes:
#		    The only even prime number is 2. All other even numbers can be divided by 2.
#
#			If the sum of a number's digits is a multiple of 3, that number can be divided by 3.
#
#			No prime number greater than 5 ends in a 5. Any number greater than 5 that ends in a 5 can be divided by 5.
#
#			Zero and 1 are not considered prime numbers.
#
#			Except for 0 and 1, a number is either a prime number or a composite number. 
#			A composite number is defined as any number, greater than 1, that is not prime.

import time 

#	option one -- try factoring increasing numbers until we come across the 10,001st prime 
#			   -- this option is slow 

def factors(n):
	factors = []

	#	look for factors of two 
	while n % 2 == 0:
		factors.append(2)
		n = n / 2 

	#	look for odd factors 
	p = 3 
	while n != 1:
		while n % p == 0: 
			factors.append(p)
			n = n / p 
		p += 2

	return factors 

def nthPrime(n): 
	prime = 2		# last prime
	count = 1 		# number of primes 
	num = 3			# next number to check 

	while count < n:
		if len(factors(num)) == 1: 
			prime = num 
			count += 1 
		num += 2 	# only check odd numbers 

	return prime

start = time.time()
prime = nthPrime(10001)
elapsed = (time.time() - start)


print "found %s in %s seconds" % (prime, elapsed)

