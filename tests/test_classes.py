import pytest
from src.classes import BaseProduct, Product, Category, Smartphone, LawnGrass, CreationLoggerMixin


def test_product_init():
    product = Product("Телефон", "Хороший телефон", 10000, 5)
    assert product.name == "Телефон"
    assert product.price == 10000
    assert product.quantity == 5


def test_product_price_set():
    product = Product("Телефон", "Описание", 10000, 5)
    product.price = 15000
    assert product.price == 15000

    product.price = -5000
    assert product.price == 15000


def test_category_init():
    product = Product("Телефон", "Описание", 10000, 5)
    category = Category("Электроника", "Техника", [product])
    assert category.name == "Электроника"
    assert len(category.products.split('\n')) == 1


def test_add_product_category():
    category = Category("Электроника", "Техника")
    product = Product("Телефон", "Описание", 10000, 5)
    initial_count = len(category.products.split('\n')) if category.products else 0
    category.add_product(product)
    assert len(category.products.split('\n')) == initial_count + 1


def test_smartphone_init():
    phone = Smartphone("iPhone", "Хороший", 50000, 10, 95.5, "13 Pro",
                       256, "Black")
    assert phone.model == "13 Pro"
    assert phone.memory == 256


def test_lawn_grass_init():
    grass = LawnGrass("Трава", "Зеленая", 500, 100, "Россия",
                      "14 дней", "Зеленый")
    assert grass.country == "Россия"
    assert grass.germination_period == "14 дней"


def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct("Тест", "Тест", 100, 1)


def test_creation_logger_mixin():
    class TestProduct(CreationLoggerMixin, BaseProduct):
        def __init__(self, name, description, price, quantity):
            super().__init__(name, description, price, quantity)
            self._price = price

        def __str__(self):
            return f"{self.name}"

        @property
        def price(self):
            return self._price

        @price.setter
        def price(self, value):
            self._price = value

    product = TestProduct("Тест", "Тест", 100, 1)
    assert product.name == "Тест"


def test_product_add():
    p1 = Product("Товар1", "Описание", 100, 2)
    p2 = Product("Товар2", "Описание", 200, 3)
    assert p1 + p2 == 800


def test_invalid_product_add():
    p1 = Product("Товар1", "Описание", 100, 2)
    with pytest.raises(TypeError):
        p1 + "не товар"
