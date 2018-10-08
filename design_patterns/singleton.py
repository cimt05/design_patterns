"""
Template for the Singleton design pattern
"""


class Singleton:
    """
    Skeleton of a class that implements the Singleton pattern
    """

    instance = None

    def __new__(cls):
        """
        checks if an instance exists and creates a new one only if this is not the case
        """
        if cls.instance is None:
            return super().__new__(cls)
        return cls.instance

    def __init__(self):
        """
        registers the instance in the class variable (and does further initialization ...)
        """
        cls = self.__class__
        if cls.instance is None:
            cls.instance = self
