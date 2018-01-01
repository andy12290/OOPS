# Lets create the class deccorator

class Decorator():
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Call method call before {} '.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@Decorator
def display():
    print('This is just display function')

display()
