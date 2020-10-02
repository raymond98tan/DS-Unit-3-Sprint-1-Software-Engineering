import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_nondefault_explode_stealability(self):
        prod = Product('Test Product', price=1000, flammability=40)
        self.assertEqual(prod.explode(), "...BABOOOM!!")
        self.assertEqual(prod.stealability(), "Very stealable!")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        products = generate_products()
        for prod in products:
            self.assertIn(prod.name.split()[0], ADJECTIVES)
            self.assertIn(prod.name.split()[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
