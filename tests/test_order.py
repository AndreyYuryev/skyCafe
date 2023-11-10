""" Тестовые случаи для заказа """
from src.order import Order


def test_order():
    order1 = Order()
    order2 = Order()
    order3 = Order()
    assert order1.number == 1
    assert order2.number == 2
    assert order3.number == 3
    order1.add_item('1', 1)
    order1.add_item('2', 2)
    order2.add_item('4', 10)
    order3.add_item('20', 11)
    assert order1.items == {'1': 1, '2': 2}
    assert order2.items == {'4': 10,}
    assert order3.items == {'20': 11,}
