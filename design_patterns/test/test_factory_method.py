"""
Unittests for the Factory Method Pattern

@author: Dr. Christoph Theis
@since: 11.10.2018
@version: 0.1
"""

import unittest

from design_patterns.factory_method import Product
from design_patterns.factory_method import Creator
from design_patterns.factory_method import ConcreteCreator


class ProductTest(unittest.TestCase):
    """
    Unittest for the Product class
    """

    def test_product_defines_properties_and_methods(self):
        """
        tests that instance of Product with some dummy property and method can be created
        """
        product = Product('some_value')
        self.assertEqual(product.some_property, 'some_value')
        self.assertTrue(hasattr(product, 'some_method'))
        self.assertEqual(product.some_method(), 'some_value')
        self.assertEqual(product.some_other_method(), 'some_value')


class CreatorTest(unittest.TestCase):
    """
    Unittest for the Creator class (containing) factory_method as abstract method
    """

    def test_creator_has_factory_method_but_doesnt_implement_it(self):
        """
        tests that Creator defines a factory_method but has no implementation
        """
        creator = Creator()
        self.assertTrue(hasattr(creator, 'factory_method'))
        self.assertRaises(NotImplementedError, creator.factory_method)
        self.assertEqual(creator.some_other_method(), type(creator))


class ConcreteCreatorTest(unittest.TestCase):
    """
    Unittest for ConcreteCreator class, i.e. a subclass of Creator that
    implements the factory_method
    """

    def test_is_subclass_of_creator(self):
        """
        tests that ConcreteCreator is a subclass of Creator
        """
        concrete_creator = ConcreteCreator()
        self.assertIsInstance(concrete_creator, Creator)
        self.assertEqual(concrete_creator.some_other_method(), type(concrete_creator))

    def test_implements_factory_method(self):
        """
        tests that ConcreteCreator implements the factory_method that return a Product
        """
        concrete_creator = ConcreteCreator()
        self.assertTrue(hasattr(concrete_creator, 'factory_method'))
        self.assertIsInstance(concrete_creator.factory_method(), Product)


if __name__ == '__main__':
    unittest.main()
