from src.stock import Stock
from src.products import Product


def test_product_stock():
    Product.clear_numbers()
    product1 = Product(name='Product 1')
    Product.add_product_by_obj(product1)
    product2 = Product(name='Product 2')
    Product.add_product_by_obj(product2)
    product3 = Product(name='Product 3', product_id=5)
    Product.add_product_by_obj(product3)
    product4 = Product(name='Product 4')
    Product.add_product_by_obj(product4)
    stock = Stock()
    stock.add_product(product=product1, quantity=10)
    stock.add_product(product=product3, quantity=3)
    stock.add_product(product=product4, quantity=22)
    assert stock.get_quantity_by_id(1) == 10
    assert stock.get_quantity_by_id(2) == 0
    assert stock.get_quantity_by_id(5) == 3
    assert stock.get_quantity_by_id(6) == 22
    assert stock.get_quantity_by_product(product3) == 3

def test_add_quantity():
    Product.clear_numbers()
    product1 = Product(name='Product 1')
    Product.add_product_by_obj(product1)
    Product.add_product_by_obj(Product(name='Product 2'))
    Product.add_product_by_obj(Product(name='Product 3', product_id=5))
    Product.add_product_by_obj(Product(name='Product 4'))
    stock = Stock()
    stock.add_product(product=Product.get_by_id(1), quantity=10)
    stock.add_product(product=Product.get_by_id(2), quantity=3)
    stock.add_product(product=Product.get_by_id(5), quantity=22)
    stock.add_quantity_by_product(Product.get_by_id(1), quantity=5)
    assert stock.get_quantity_by_id(1) == 15
    stock.add_quantity_by_product(Product.get_by_name('Product 3')[0], quantity=6)
    assert stock.get_quantity_by_id(5) == 28



    # assert not stock.is_product_in_stock(product2)
    # assert stock.is_product_in_stock(product3)
    # assert stock.get_quantity(product3) == 3
    # assert stock.get_quantity(product4) == 0

#
# def test_stock():
#     correct_stock = [{'id': 'e7ac57cb-abb2-44f0-8c5b-9af96d0f1b5d', 'name': 'Морковь', 'price': 100, 'quantity': 1},
#                      {'id': 'd93b5d1a-dd0e-4a6f-86a8-8c0e2a6e0725', 'name': 'Мясо', 'price': 200, 'quantity': 1},
#                      {'id': '9cf14c28-53a0-4a19-b524-967f6e12b748', 'name': 'Рыба', 'price': 300, 'quantity': 1}]
#
#     carrot = Vegetables("Морковь", 100)
#     cow_meat = Meat("Мясо", 200)
#     fish = Fish("Рыба", 300)
#
#     assert Stock.products == correct_stock  # будет ошибка из-за генерации id
#
#     for product in Stock.products:
#         if product['name'] == 'Яблоко':
#             product['quantity'] += 1
#             assert product['quantity'] == 1
#         elif product['name'] == 'Мясо':
#             product['quantity'] += 2
#             assert product['quantity'] == 2
#         elif product['name'] == 'Рыба':
#             product['quantity'] += 3
#             assert product['quantity'] == 3
#
#
# def test_is_in_stock():
#     carrot = Vegetables("Морковь", 100)
#
#     assert Stock.is_product_in_stock(carrot)
#
#
# def test_add_quantity():
#     carrot = Vegetables("Морковь", 100)
#
#     Stock.add_quantity(carrot, 2)
#
#     assert Stock.products[0]['quantity'] == 2
