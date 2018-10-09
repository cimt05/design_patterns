"""
Unittests for the Prototype class

@author: Dr. Christoph Theis
@since: 08.10.2018
@version: 0.1
"""

import unittest

from design_patterns.prototype import Prototype


class PrototypeTest(unittest.TestCase):
    """
    Unittest for the Prototype class
    """

    def test_can_create_a_new_instance_of_prototype(self):
        """
        Tests instantiation of prototype instance
        """
        instance = Prototype('some_value')
        self.assertIsInstance(instance, Prototype)

    def test_can_get_a_clone_as_a_new_instance(self):
        """
        Tests that clone method returns a (deep) copy of the instance
        """
        instance = Prototype('some_value')
        clone = instance.clone()
        self.assertIsInstance(clone, Prototype)
        self.assertNotEqual(instance, clone)


if __name__ == '__main__':
    unittest.main()
