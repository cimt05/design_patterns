class Singleton(object):

    instance = None

    def __new__(cls):
        if cls.instance is None:
            return super().__new__(cls)
        else:
            return cls.instance

    def __init__(self):
        cls = self.__class__
        if cls.instance is None:
            cls.instance = self
