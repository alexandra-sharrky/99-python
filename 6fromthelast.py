# It is 6-th programming problem
# Find out whether a list is a palindrome.
# A palindrome can be read forward or backward; e.g. (x a m a x).
# http://www.ic.unicamp.br/~meidanis/courses/mc336/2006s2/funcional/L-99_Ninety-Nine_Lisp_Problems.html
s = input("Enter your list")

l = len(s)

for i in range(l//2):
    if s[i] != s[-1-i]:
        print("It's not palindrome")
        quit()

print("It's palindrome")

