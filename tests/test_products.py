from src.products import Product, ProductFactory


def test_product():
    Product.clear_numbers()
    product = Product("test", 100)
    assert product.name == "test"
    assert product.price == 100

    product.price = 200
    assert product.price == 200


def test_new_product():
    Product.clear_numbers()
    product1 = Product(name='Product 1', price=101)
    product2 = Product(name='Product 2', price=102)
    product3 = Product(name='Product 3', price=103, product_id=5)
    product4 = Product(name='Product 4', price=104)
    assert product1.product_id == 1
    assert product2.product_id == 2
    assert product3.product_id == 5
    assert product4.product_id == 6
    assert product1.name == 'Product 1'
    assert product2.name == 'Product 2'
    assert product3.name == 'Product 3'
    assert product4.name == 'Product 4'
    assert product1.price == 101
    assert product2.price == 102
    assert product3.price == 103
    assert product4.price == 104


def test_product_factory():
    Product.clear_numbers()
    product1 = Product(name='Product 1', price=101)
    product2 = Product(name='Product 2', price=102)
    product3 = Product(name='Product 3', price=103, product_id=5)
    product4 = Product(name='Product 4', price=104)
    product_factory = ProductFactory()
    assert len(product_factory.products) == 0
    product_factory.add_product(product1)
    product_factory.add_product(product2)
    product_factory.add_product(product3)
    product_factory.add_product(product4)
    assert len(product_factory.products) == 4


def test_upload_product_factory():
    product1 = Product(name='Product 1', price=101)
    product2 = Product(name='Product 2', price=102)
    product3 = Product(name='Product 3', price=103, product_id=5)
    product4 = Product(name='Product 4', price=104)
    product_factory = ProductFactory()
    assert len(product_factory.products) == 0
    products = []
    products.append(product1.to_dict())
    products.append(product2.to_dict())
    products.append(product3.to_dict())
    products.append(product4.to_dict())
    product_factory.upload_products(product_list=products)
    assert len(product_factory.products) == 4
