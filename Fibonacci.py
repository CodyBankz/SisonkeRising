""" A Program to
    demostrate the fionacci
    number sequence.
    By: Koketso..... """

fibonacci = []

for index in range(0,141):
    """ If Index is zero """
    if(index == 0):
        number = 0
    """ If index is 1 """
    if(index == 1):
        number = 1
    """ Index Greater than 1 """
    if(index > 1):
        number = fibonacci[index - 1] + fibonacci[index - 2]

    """ Adding element to the list. """
    fibonacci.append(number)
    


#Printing the Sequence
print(fibonacci)

