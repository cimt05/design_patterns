import unittest

from design_patterns.singleton import Singleton


class SingletonTest(unittest.TestCase):

    def test_get_instance_of_singleton(self):
        instance = Singleton()
        self.assertIsNotNone(instance)

    def test_two_instances_of_singeton_are_the_same(self):
        instance = Singleton()
        other_instance = Singleton()
        self.assertIs(instance, other_instance)


if __name__ == '__main__':
    unittest.main()
