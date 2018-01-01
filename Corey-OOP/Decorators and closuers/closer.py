# closure

def outer_func():
    message = 'Hi Aniket how are you?'

    def inner_func():
        print(message)

    return inner_func()

(outer_func())


#Another Example of closure


import logging
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):

    def log_func(*args):

        logging.info(
            'Running {} with the arguments {}'.format(func.__name__, args)
        )
        print(func(*args))

    return log_func


def add(x,y):
    return x+y


def sub(x,y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,4)



