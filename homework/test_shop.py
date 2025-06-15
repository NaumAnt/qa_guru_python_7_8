"""
Протестируйте! классы из модуля homework/models.py
"""
from turtledemo.penrose import star

import pytest
from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(10) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        start_quantity = product.quantity
        product.buy(5)

        assert product.quantity == start_quantity - 5


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    # Добавление продукта в корзину

    def test_add_product(self, cart, product):
        cart.add_product(product, 3)
        cart.add_product(product, 5)
        assert cart.products[product] == 8

    # Удаление продукта из корзины
    def test_remove_product(self, cart, product):
        cart.add_product(product, 5)
        cart.remove_product(product, 2)
        assert cart.products[product] == 3

        cart.remove_product(product)  # удалить всё
        assert product not in cart.products

    # Очистка корзины
    def test_clear(self, cart):
        cart = Cart()
        product1 = Product("Яблоко", 100, 'Красное', 30)
        product2 = Product("Банан", 30, 'Молодой', 20)

        cart.add_product(product1, 2)
        cart.add_product(product2, 3)
        cart.clear()

        assert len(cart.products) == 0

    # Подсчёт общей стоимости
    def test_get_total_price(self, cart):
        cart = Cart()
        product1 = Product("Яблоко", 100, 'Красное', 30)
        product2 = Product("Банан", 30, 'Молодой', 20)

        cart.add_product(product1, 2)
        cart.add_product(product2, 3)

        assert cart.get_total_price() == 2 * 100 + 3 * 30  # 200 + 90 = 290

    # Покупка товара
    def test_buy_success(self, product):
        cart = Cart()
        product = Product("Банан", 30, 'Молодой', 20)

        cart.add_product(product, 5)
        cart.buy()

        assert product.quantity == 15  # должно остаться 20 - 5 = 15
        assert len(cart.products) == 0

    # Покупка товара с ошибкой
    def test_buy_insufficient_stock(self, product):
        cart = Cart()
        product = Product("Банан", 30, 'Молодой', 20)

        cart.add_product(product, 21)  # но на складе только 20 шт.

        with pytest.raises(ValueError):
            cart.buy()

