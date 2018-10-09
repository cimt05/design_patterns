"""
Template for the Singleton design pattern
(from, SO question 6760685, creating-a-singleton-in-python)
"""


class SingletonType(type):
    """
    Metaclass to make some class a Singleton
    """
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        else:
            cls.__instances[cls].__init__(*args, **kwargs)
        return cls.__instances[cls]


class Singleton(metaclass=SingletonType):
    """
    Skeleton of a class that implements the Singleton pattern
    """

    def __init__(self, some_value):
        """
        initializes properties of singleton
        """
        self.some_value = some_value

    def some_method(self):
        """
        some other method of the singleton
        """
        return 'some_ret_value'

    def some_more_method(self):
        """
        some more method (to make pylint happy ;-))
        """
        return 'some_more_ret_value'
