"""
Unittests for the Singleton class

@author: Dr. Christoph Theis
@since: 08.10.2018
@version: 0.1
"""

import unittest

from design_patterns.singleton import Singleton


class SingletonTest(unittest.TestCase):
    """
    Unittest for the Singleton class
    """

    def test_get_instance_of_singleton(self):
        """
        test normal creation of an instance
        """
        instance = Singleton()
        self.assertIsNotNone(instance)

    def test_two_instances_of_singleton_are_the_same(self):
        """
        tests that no new instance is created if there is an existing one
        """
        instance = Singleton()
        other_instance = Singleton()
        self.assertIs(instance, other_instance)


if __name__ == '__main__':
    unittest.main()
