# Об’єкт “Телефонний тариф”
# поля
#   ▪ назва тарифу;
#   ▪ дата створення;
#   ▪ дата закінчення дії;
#   ▪ абонплата;
#   ▪ вартість хвилини;
# методи
#   ▪ визначення часу до закінчення дії тарифу;
#   ▪ визначення вартості звінка за вказаною тривалістю;
#   ▪ визначення суми сплаченої абонплати між вказаними датами.
from datetime import date

class Tariff_plan:
    def __init__(self, tariff_name, date_of_creation, expiration_date, subscription_fee, cost_per_minute):
        self.tariff_name = tariff_name
        self.date_of_creation = date_of_creation
        self.expiration_date = expiration_date
        self.subscription_fee = subscription_fee
        self.cost_per_minute = cost_per_minute

    def __str__(self):
        return f"Tarif plan: \n Tariff_name: {self.tariff_name} \n Date_of_creation: {self.date_of_creation}" \
               f" \n Expiration_date: {self.expiration_date} \n Subscription_fee: {self.subscription_fee}$ " \
               f"\n Cost_per_minute: {self.cost_per_minute}$"

    def time_of_reality(self):
        days = (self.expiration_date - date(2020,12,11)).days
        print("Сьогоднішня дата = 2020-12-11")
        return f"До закінчення дії тарифу залишилось = {days} днів"

    def call_cost(self):
        duration_call = int(input("Тривалість дзвітка (хвилини) = "))
        return f"Вартість дзвітка тривалістю {duration_call} хвилин = {duration_call * self.cost_per_minute}$"

    def sum_subscription_fee(self):
        number = (self.expiration_date - self.date_of_creation).days
        d = number//31
        c = 0
        if d > 0:
            c+=1
        c += d
        if c == 0:
            c+= 1
        return f"Сума сплаченої абонплати за проміжок від {self.date_of_creation} до " \
               f"{self.expiration_date} = {c * self.subscription_fee}$"


tarif = Tariff_plan("SuperNet+", date(2020,12,4), date(2020,12,24), 20, 1)
print(tarif)
print(tarif.time_of_reality())
print(tarif.call_cost())
print(tarif.sum_subscription_fee())

