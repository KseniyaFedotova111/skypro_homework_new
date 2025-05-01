from abc import ABC, abstractmethod


class CreationLoggerMixin:
    def __init__(self, *args, **kwargs):
        print(f"Создан объект {self.__class__.__name__} с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass


class Product(CreationLoggerMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, data):
        return cls(**data)

    def __repr__(self):
        return (f"Product(name={self.name}, description={self.description}, "
                f"price={self.price}, quantity={self.quantity})")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if not isinstance(product, Product) and not issubclass(type(product), Product):
            raise TypeError("Можно добавлять только объекты Product или его подклассов")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )

    def __repr__(self):
        return f"Category(name={self.name}, description={self.description}, products={self.__products})"

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return (f"Smartphone(name={self.name}, description={self.description}, "
                f"price={self.price}, quantity={self.quantity}, "
                f"efficiency={self.efficiency}, model={self.model}, "
                f"memory={self.memory}, color={self.color})")

    def __str__(self):
        base = super().__str__()
        return f"{base}, Модель: {self.model}, Память: {self.memory}GB, Цвет: {self.color}"


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return (f"LawnGrass(name={self.name}, description={self.description}, "
                f"price={self.price}, quantity={self.quantity}, "
                f"country={self.country}, germination_period={self.germination_period}, "
                f"color={self.color})")

    def __str__(self):
        base = super().__str__()
        return f"{base}, Страна: {self.country}, Срок прорастания: {self.germination_period}"
