# 99-python
99 programming problems in Python
5 problems solved

source: http://www.ic.unicamp.br/~meidanis/courses/mc336/2006s2/funcional/L-99_Ninety-Nine_Lisp_Problems.html

Working with lists
P01 (*) Find the last box of a list.
Example:
* (my-last '(a b c d))
(D)
P02 (*) Find the last but one box of a list.
Example:
* (my-but-last '(a b c d))
(C D)
P03 (*) Find the K'th element of a list.
The first element in the list is number 1.
Example:
* (element-at '(a b c d e) 3)
C
P04 (*) Find the number of elements of a list.
P05 (*) Reverse a list.
P06 (*) Find out whether a list is a palindrome.
A palindrome can be read forward or backward; e.g. (x a m a x).
P07 (**) Flatten a nested list structure.
Transform a list, possibly holding lists as elements into a `flat' list by replacing each list with its elements (recursively).

Example:
* (my-flatten '(a (b (c d) e)))
(A B C D E)

Hint: Use the predefined functions list and append.
