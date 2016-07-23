''' Author Koketso Maphothoma
    A Dictionary(Map) that groups
    my Favourite cars.'''

# A Function to display my favourite Cars ( The Dictionary/Map group )
def display_Cars():
        My_Favourite_Cars = { 1 : " Mercedes Benz AMG G63 " , 2 : " Ford Mustang G550 " , 3 : " BMW M6 " ,
                              4 : " VW Sirocco R " , 5 : " Mercedes Benz AMG C63 " , 6 : " Mercedes Benz AMG SLS " }
                        

        print(" This are Koketso's favourite cars : ")
        for favouriteCar in My_Favourite_Cars :
                print(favouriteCar , My_Favourite_Cars.get(favouriteCar))


''' Calling a function to display '''
display_Cars()
