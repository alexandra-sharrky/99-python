# 3 from the last P03 (*) Find the K'th element of a list.
# The first element in the list is number 1.
# Example:
# * (element-at '(a b c d e) 3)
# C
# http://www.ic.unicamp.br/~meidanis/courses/mc336/2006s2/funcional/L-99_Ninety-Nine_Lisp_Problems.html

lis = input("Enter your list")
k = int(input("Enter K - integer"))
x = k-1
print(lis[x])
