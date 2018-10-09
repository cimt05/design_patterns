"""
Template for the Prototype design pattern
"""

from copy import deepcopy


class Prototype:
    """
    Class that can be used as a prototype, i.e. instances have a clone method that returns a
    copy of the instance
    """

    def __init__(self, some_value):
        """
        Initialization of properties
        """
        self.some_value = some_value

    def some_method(self):
        """
        Other method not related to prototype pattern
        """
        return 'some_ret_value'

    def clone(self):
        """
        Makes a copy of the instance and returns it
        """
        return deepcopy(self)
