''' A Program to
    illustrate bubble sorting
    by : Koketso..... '''


#Creating a list
ages=[8,4,5,18,0]
print (ages)

print(" ")
#Displaying list with an incrementing index
print("Unordered list")
for index in range(0,5):
    print (index, ages[index])

    
#Backwards display
print(" ")
print("Backwards")
for index in range(0,5):
    print(4 - index,ages[4 - index])


print(" ")
#Bubble sorting
for numbers in range(len(ages)-1,0,-1):
    for index in range(numbers):
        if (ages[index]>ages[index+1]):
            number = ages[index]
            ages[index] = ages[index+1]
            ages[index + 1] = number
print("Sorted List : ")
print(ages)



























































    
    
