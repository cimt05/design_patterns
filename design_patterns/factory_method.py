"""
Templates for the Factory Method design pattern

Remark: Due to dynamic typing in Python we don't need an (abstract) Product class since we don't
need to declare the type of products that are created by the Creator class
"""


class Product:
    """
    Sample product to be created by the Factory Method
    """

    def __init__(self, some_value):
        """
        Initializes the sample property of Product
        @param some_value: sample property
        @type some_value: str
        """
        self.some_property = some_value

    def some_method(self):
        """
        Sample method of Product
        """
        return 'some_ret_value'

    def some_other_method(self):
        """
        Some more sample method of Product to make pylint happy
        """
        return 'some_other_ret_value'



class Creator:
    """
    Base class of concrete Creators
    """

    def factory_method(self):
        """
        abstract factory method
        """
        raise NotImplementedError('factory_method has to be implemented in a subclass')

    def some_other_method(self):
        """
        Some other method to make pylint happy
        """
        return 'some_other_ret_value'


class ConcreteCreator(Creator):
    """
    Subclass of Creator that implements the factory_method
    """

    def factory_method(self):
        """
        implementation of factory method
        @return: a product
        @rtype: instance of Product
        """
        return Product('some_value')
