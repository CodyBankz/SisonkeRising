""" Program By:
    Koketso Maphothoma.. """


myList1 = [1,5,8,11,12,15]
myList2 = [1,100,25]



def Sisonke_length(list): 
    length = 0
    for index in list:
        length = length + 1
    return length


#Returning the length
listLength = Sisonke_length(myList1)
print("List 1 length :")
print(listLength)

length2 = Sisonke_length(myList2)
print("Second list :  ")
print(length2)

print(" ")
#getting the value at
def get_value_at(index,list):
    value = list[index]
    return value

myValue = 3
print("Your value is : ",get_value_at(myValue,myList1))
    


#getting the index of value
def get_index_of_value(value,list):
    list_length = Sisonke_length(list)
    counter = 0
    while(counter < list_length):
        for index in range(0,list_length):
            if(list[index] == value):
                return index
        counter =+ 1
    return "Did not match"


print("Your Index Is : ",get_index_of_value(15,myList1))
