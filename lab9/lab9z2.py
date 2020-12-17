# Довідник автомеханіка. База даних запчастин: назва запчастини, марка автомобіля, рік
# випуску. Організувати вибір за довільним запитом. Дані зберігаються в масиві записів, який
# створюється динамічно.

class Spare_parts:
    def __init__(self, name_spare_parts, car_brand, graduation_year):
        self.name_spare_parts = name_spare_parts
        self.car_brand = car_brand
        self.graduation_year = graduation_year

    def __str__(self):
        return f"Name_spare_parts: {self.name_spare_parts}, Car_brand: {self.car_brand}, Graduation_year: {self.graduation_year}"


detals = Spare_parts("dor", "BMW", 2017)
detals1 = Spare_parts("Headlight", "BMW", 2014)
print(detals)
print(detals1)






