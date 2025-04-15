from classes import Category, Product

if __name__ == "__main__":
    # Создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Вывод информации о продуктах
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    # Создание первой категории и добавление продуктов
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(category1.products)  # Используем геттер для вывода списка продуктов
    print(Category.category_count)
    print(Category.product_count)

    # Добавление нового продукта в категорию
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(Category.product_count)

    # Создание второй категории
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4]
    )

    print(category2.name)
    print(category2.description)
    print(category2.products)
    print(Category.category_count)
    print(Category.product_count)

    # Создание нового продукта через класс-метод
    new_product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }
    new_product = Product.new_product(new_product_data)

    # Вывод информации о новом продукте
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    # Изменение цены нового продукта
    new_product.price = 800
    print(new_product.price)

    new_product.price = -100  # Попытка установить некорректную цену
    new_product.price = 0     # Попытка установить нулевую цену
    print(new_product.price)
