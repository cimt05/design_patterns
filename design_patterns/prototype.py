"""
Template for the Prototype design pattern
"""

from copy import deepcopy


class Prototype:

    def clone(self):
        return deepcopy(self)
