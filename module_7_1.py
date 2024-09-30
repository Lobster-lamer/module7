import os


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


def get_product_name(product) -> str:
    if isinstance(product, str):
        return product.split(", ")[0]
    if isinstance(product, Product):
        return product.name


class Shop:
    def __init__(self):
        self.__file_name = "products.txt"
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, "w"):
                pass

    def get_products(self):
        with open(self.__file_name, "r") as file:
            return file.read()

    def get_products_names(self) -> list:
        products_names = []
        with open(self.__file_name, "r") as file:
            for line in file.readlines():
                products_names.append(get_product_name(line))
        return products_names

    def add_products(self, *products: Product):
        existing_products_names = self.get_products_names()
        with open(self.__file_name, "a") as file:
            for product in products:
                product_name = get_product_name(product)
                if product_name in existing_products_names:
                    print(f"Продукт {product_name} уже есть в магазине")
                else:
                    file.write(f"{product}\n")


if __name__ == "__main__":
    farm_shop = Shop()
    potato = Product("potato", 50.0, "vegetable")
    tomato = Product("tomato", 10.0, "vegetable")
    farm_shop.add_products(potato, tomato)
    print(farm_shop.get_products())
    print(farm_shop.get_products_names())
