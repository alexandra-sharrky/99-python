# 3 from the last P03 (*) Find the K'th element of a list.
# The first element in the list is number 1.
# Example:
# * (element-at '(a b c d e) 3)
# C
# http://www.ic.unicamp.br/~meidanis/courses/mc336/2006s2/funcional/L-99_Ninety-Nine_Lisp_Problems.html

import random
 
def list3():
    while True:
        try:
            length_list=input("Enter the length of the random list you would like to create: ")
            range_list=input("Enter the range to which you would like the numbers to be picked from: 0-")
            List = random.sample(range(range_list),length_list) #creating random list
            k = input("What element would you like to pick?")
            x = k-1
            print("The element corresponding to element("+str(k)+") is: "+str(List[x]))
            print ("The list created was: "+str(List))
            break
        except ValueError:
            print("Your range must be larger than your length. Your chosen element must be greater than zero.")
        except NameError:
            ("Please ensure you type an integer number.")
        except TypeError:
            print("Please ensure you are typing integer numbers.")
        except SyntaxError:
            print("Please type an integer number.")
        except IndexError:
            print("The element you wish to see must be within the size of the list.")
list3()
            
            
