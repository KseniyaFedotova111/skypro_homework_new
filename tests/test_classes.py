def test_init(samsung_product):
    assert samsung_product.name == 'Samsung Galaxy S23 Ultra'
    assert samsung_product.description == '256GB, Серый цвет, 200MP камера'
    assert samsung_product.price == 180000.0
    assert samsung_product.quantity == 5


def test_init_category(category):
    assert category.name == 'Смартфоны'
    assert category.description == 'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни'


def test_category_count(category):
    assert category.category_count == 1


def test_product_count(category):
    assert len(category.products) == 3
