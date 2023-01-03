#first_class function
def square(value):
    return value*value

def map_function( func, args_list):
    '''This function maps any given array to the square of its individual elements'''
    result = []
    for i in args_list:
        result.append(func(i))
    return result
array = [2,4,6]

result = map_function(square, array)
print(result)
