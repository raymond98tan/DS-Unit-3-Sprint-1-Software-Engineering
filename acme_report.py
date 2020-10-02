import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=30):
    products = []

    for i in range(0, n):
        product_name = random.choice(ADJECTIVES) + " " + random.choice(NOUNS)
        weight = random.randint(5, 100)
        price = random.randint(5, 100)
        flammability = random.uniform(0, 2.5)
        product = Product(product_name, weight=weight, price=price,
                          flammability=flammability)
        products.append(product)

    return products


def inventory_report(products):
    price, weight, flam = 0, 0, 0
    for prod in products:
        price += prod.price
        weight += prod.weight
        flamm += prod.flammability

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: ", len(products))
    print("Average price: ", price/len(products))
    print("Average weight: ", weight/len(products))
    print("Average flammability: ", flamm/len(products))

if __name__ == '__main__':
    inventory_report(generate_products())
