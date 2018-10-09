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
        instance = Singleton('some_value')
        self.assertIsInstance(instance, Singleton)
        self.assertEqual(instance.some_value, 'some_value')
        self.assertEqual(instance.some_method(), 'some_ret_value')
        self.assertEqual(instance.some_more_method(), 'some_more_ret_value')

    def test_two_instances_of_singleton_are_the_same(self):
        """
        tests that no new instance is created if there is an existing one
        but the one instance is reinitialized
        """
        instance = Singleton('some_value')
        other_instance = Singleton('other_value')
        self.assertIs(instance, other_instance)
        self.assertEqual(instance.some_value, 'other_value')


if __name__ == '__main__':
    unittest.main()
