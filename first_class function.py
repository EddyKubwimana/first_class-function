#first_class function

#1

def square(value):
    return value*value

def map_function( func, args_list):
    '''This function maps any given array to the square of its individual elements'''
    result = []
    for i in args_list:
        result.append(func(i))
    return result

# testing for the map__function

array = [2,4,6]

result = map_function(square, array)
print(result)



#2

def say_hello():
     msg = " Hello"

     def name(user_name):

         print( msg+ " "+ str(user_name))

     return name

#Testing

greeting = say_hello()

#Here greeting is being treated as variable

individual = greeting
individual("Steve")





