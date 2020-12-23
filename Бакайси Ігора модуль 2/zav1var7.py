# Клас “відрізок на площині” – Interval2D
#   поля
#       ▪ для зберігання координат початку і кінця відрізка;
#   методи
#       ▪ конструктор без параметрів, конструктор з параметрами,
#       ▪ копіювання;
#       ▪ введення/виведення даних;
#       ▪ знаходження точки перетину з іншим відрізком;
#       ▪ визначення довжини відрізка;
#       ▪ визначення середини відрізка;
#       ▪ перевантаження операторів + (утворюється відрізок початок якого є
#       початком першого, а кінець – кінцем другого), * (збільшення довжини відрізка у
#       вказану кількість разів зберігаючи початок відрізка незмінним).

class Interval2D:
    def __init__(self, x1=2, y1=3, x2=6, y2=8):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"Координати початку відрізка: ({self.x1},{self.y1}), Координати кінця відрізку: ({self.x2},{self.y2})."

    def __repr__(self):
        return str(self)

    def len_of_segment(self):
        len_of_segment = ((self.x2-self.x1)**2+(self.y2-self.y1)**2)**(1/2)
        return f"Давжина відрізка: {len_of_segment}"

    def middle_of_segment(self):
        xs = (self.x1 + self.x2)/2
        ys = (self.y1 + self.y2)/2
        return f"Серидина відрізка: ({xs},{ys})"

    def copy(self):
        m = []
        m.copy()
        return m

    def third_segment(self):
        x3 = float(input("x3 = "))
        y3 = float(input("y3 = "))
        x4 = float(input("x4 = "))
        y4 = float(input("y4 = "))
        print(f"Координати початку дргугого відрізка: ({x3},{y3}), Координати кінця другого відрізку: ({x4},{y4}).")
        x5 = self.x1
        y5 = self.y1
        x6 = x4
        y6 = y4
        return f"Утворився відрізок, де координати початку відрізка: ({x5},{y5}),а координати кінця відрізку: ({x6},{y6})."

    def increase_length_of_segment(self):
        k = input("Вказіть у скільки разів потрібно збільшити довжину відрізка: ")
        xk = self.x2*k
        yk = self.y2*k
        return f"Збільшений відрізок у {k} разів, початок координат ({self.x1},{self.y1}), а координати кінця відрізка ({xk},{yk}."

dec = Interval2D(3, 5, 7, 8)
print(dec)
print(dec.middle_of_segment())
print(dec.len_of_segment())
print(dec.third_segment())
print(dec.increase_length_of_segment())
