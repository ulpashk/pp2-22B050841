def my_function(*args):

    result = 1
    for number in args:
        result = result * number

       
    return result

print(my_function(1,2,10,5,6))



