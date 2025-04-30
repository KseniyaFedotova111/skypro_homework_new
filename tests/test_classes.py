import pytest

from src.classes import Category, Product


def test_init(samsung_product):
    assert samsung_product.name == 'Samsung Galaxy S23 Ultra'
    assert samsung_product.description == '256GB, Серый цвет, 200MP камера'
    assert samsung_product.price == 180000.0
    assert samsung_product.quantity == 5


def test_init_category(category):
    assert category.name == 'Смартфоны'
    assert category.description == ('Смартфоны, как средство не только коммуникации, '
                                    'но и получения дополнительных функций для удобства жизни')


def test_category_count(category):
    assert category.category_count == 1


def test_product_count(category):
    assert len(category.products) == 145


def test_product_price_setter(samsung_product):
    samsung_product.price = 175000.0
    assert samsung_product.price == 175000.0

    samsung_product.price = -50
    assert samsung_product.price != -50


def test_add_product_to_category(category):
    new_product = Product("New Product", "Description", 150.0, 5)
    category.add_product(new_product)
    assert len(category.products.split("\n")) == 4
    assert Category.product_count == 4


def test_product_representation(samsung_product):
    expected_repr = ("Product(name=Samsung Galaxy S23 Ultra, description=256GB, Серый цвет, 200MP камера, "
                     "price=180000.0, quantity=5)")
    assert repr(samsung_product) == expected_repr


def test_category_representation(category):
    expected_repr = (f"Category(name=Смартфоны, description=Смартфоны, как средство не только коммуникации, "
                     f"но и получения дополнительных функций для удобства жизни, "
                     f"products={category._Category__products})")
    assert repr(category) == expected_repr


def test_product_str_representation(samsung_product):
    expected_str = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(samsung_product) == expected_str


def test_category_str_representation(category):
    expected_str = "Смартфоны, количество продуктов: 27 шт."
    assert str(category) == expected_str


def test_product_addition(samsung_product, iphone_product):
    assert samsung_product + iphone_product == 2580000


def test_product_addition_with_invalid_type(samsung_product):
    with pytest.raises(TypeError, match="Можно складывать только объекты Product"):
        samsung_product + "not_a_product"


def test_category_str_with_empty_products():
    empty_category = Category("Пустая категория", "Нет товаров", [])
    assert str(empty_category) == "Пустая категория, количество продуктов: 0 шт."


def test_smartphone_properties(smartphone):
    assert smartphone.model == "Note 10"
    assert smartphone.memory == 128
    assert isinstance(smartphone, Product)


def test_lawn_grass_properties(lawn_grass):
    assert lawn_grass.country == "Германия"
    assert lawn_grass.germination_period == "10 дней"
    assert isinstance(lawn_grass, Product)


def test_smartphone_str(smartphone):
    assert "Модель: Note 10" in str(smartphone)


def test_lawn_grass_str(lawn_grass):
    assert "Страна: Германия" in str(lawn_grass)


def test_add_smartphone_to_category(category_with_products, smartphone):
    initial_count = len(category_with_products.products.split("\n"))
    category_with_products.add_product(smartphone)
    assert len(category_with_products.products.split("\n")) == initial_count + 1


def test_add_invalid_to_category(category_with_products):
    with pytest.raises(TypeError):
        category_with_products.add_product("invalid")
