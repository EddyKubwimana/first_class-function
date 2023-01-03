import logging
logging.basicConfig(filename = "used function", level = logging.INFO)

def logger(func):
    def my_funct(*args):
        logging.info("running {} with argument{}".format(func.__name__, args))
        print(func(*args))
    return my_funct

def add(*args):

    summation = 0
    for i in args:
        summation += i
    return summation

add_logger = logger(add)
add_logger(1,3,5,7)
add_logger(100,300)
    

                     
