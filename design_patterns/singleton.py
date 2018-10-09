"""
Template for the Singleton design pattern
"""


class Singleton:
    """
    Skeleton of a class that implements the Singleton pattern
    """

    __instance = None

    def __new__(cls):
        """
        checks if an instance exists and creates a new one only if this is not the case
        """
        if cls.__instance is None:
            return super().__new__(cls)
        return cls.__instance

    def __init__(self):
        """
        registers the instance in the class variable (and does further initialization ...)
        """
        cls = self.__class__
        if cls.__instance is None:
            cls.__instance = self
