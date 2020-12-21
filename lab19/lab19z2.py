# Розробити клас що виконує основні функції бази даних (Додавання, вилучення
# та пошуку) а також містить методи для зберігання данних у файлах та зчитування із файлу.
# Склад. База товарів, які зберігаються на складі: назва товару, одиниця виміру, кількість.
# Організувати вибір товару за назвою.

class Product:
    def __init__(self, name_product, unit, number):
        self.name_product = name_product
        self.unit = unit
        self.number = number

    def __str__(self):
        return f"Name_product: {self.name_product}, Unit: {self.unit}, Number: {self.number}"

    def __repr__(self):
        return str(self)

class Storage:
    def __init__(self, file_name):
        self.__list = []
        self.file_name = file_name

    def __repr__(self):
        return str(self.__list)

    def add(self, product):
        self.__list.append(product)

    def exclude(self, product):
        self.__list.remove(product)

    def save_to_file(self):
        with open(self.file_name, "w") as file:
            for product in self.__list:
                file.write(f"{product.name_product},{product.unit},{product.number}\n")

    def load_from_file(self):
        self.__list.clear()
        with open(self.file_name, "r") as file:
            for row in file:
                name_product, unit, number = row.split(",")
                number = number[:-1]
                self.__list.append(Product(name_product, unit, number))

    def find_by_name_product(self, name_product):
        for product in self.__list:
            if product.name_product == name_product:
                return product
        return None



dec = Storage("storage.txt")
dec.add(Product("banana", "kg", 6))
dec.add(Product("door", "kg", 3))
dec.add(Product("water", "liters", 5))
dec.save_to_file()
dec.load_from_file()
print(dec)
print(dec.find_by_name_product("banana"))

