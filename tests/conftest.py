import pytest
from src.classes import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def samsung_product():
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )


@pytest.fixture
def category():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                       5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )


@pytest.fixture(autouse=True)
def reset_counters():
    """сбрасывает счетчики перед тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def iphone_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def xiaomi_product():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category_with_products(samsung_product, iphone_product, xiaomi_product):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации...",
        [samsung_product, iphone_product, xiaomi_product]
    )


@pytest.fixture
def smartphone():
    return Smartphone("Xiaomi", "128GB", 50000, 10, 85.0, "Note 10",
                      128, "Blue")


@pytest.fixture
def lawn_grass():
    return LawnGrass("Трава", "Мягкая", 300, 50, "Германия",
                     "10 дней", "Зеленая")
