from src.products import Product


def test_create_product():
    Product.clear_numbers()
    product = Product(name='Product 1')
    assert product.name == 'Product 1'


def test_new_product():
    Product.clear_numbers()
    Product.add_product(name='Product 1')
    Product.add_product(name='Product 2')
    Product.add_product(name='Product 3', product_id=5)
    Product.add_product(name='Product 4')
    product = Product(name='Product 5')
    Product.add_product_by_obj(product)
    assert Product.get_by_id(1).product_id == 1
    assert Product.get_by_id(5).product_id == 5
    assert Product.get_by_id(7).name == product.name


def test_upload_product():
    Product.clear_numbers()
    products = [{'name': 'Product 1'}, {'name': 'Product 2'}, {'name': 'Product 3', 'product_id': 5}]
    Product.upload_products(product_list=products)
    assert Product.get_by_id(1).product_id == 1
    assert Product.get_by_id(1).name == 'Product 1'
    assert Product.get_by_id(2).product_id == 2
    assert Product.get_by_id(5).product_id == 5
    assert Product.get_by_id(5).name == 'Product 3'


def test_product_name():
    Product.clear_numbers()
    Product.add_product(name='Product 1')
    Product.add_product(name='Product 2', product_id=5)
    product = Product(name='Product 3')
    Product.add_product_by_obj(product)
    prod_name = 'Prod'
    products = Product.get_by_name(prod_name)
    for product in products:
        assert prod_name in product.name
