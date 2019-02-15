#   project euler
#   bradley smith
#   problem four
#   start: 1/14/2019
#   completed: 1/14/2019
#   language: python 2.7

#   problem statement:
#       a palindromic number reads the same both ways. 
#       the largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#       find the largest palindrome made from the product of two 3-digit numbers.

#   notes:
#       constructing a palindromic number
#       k[::] == k[_:_:_] ---> start, stop, increment --> when numbers are absent in three slots python
#       assumes start and finish 


def isPalindrome(k):

    if k == k[::-1]:
        return True
    else:
        return False

def largestPalindrome(n):

    arr = []

    for i in range(0, n):
        for j in range(0,n):

            k = str(i*j)

            if isPalindrome(k):
                arr.append(int(k))

    print max(arr)


largestPalindrome(9999)
