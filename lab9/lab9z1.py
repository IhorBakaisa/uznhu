# База даних співробітників фірми містить наступні дані: паспортні дані, освіта,
# спеціальність, посада, оклад. Передбачити процедури додавання, вилучення записів та
# пошуку записів за довільним запитом. Дані зберігаються в масиві.

class Datebase:
    def __init__(self, passport_data, education, specialty, position, salary):
        self.passport_data = passport_data
        self.education = education
        self.specialty = specialty
        self.position = position
        self.salary = salary

    def __str__(self):
        person = {"Passport_data": f"{self.passport_data}", "Education": f"{self.education}", "Specialty": f"{self.specialty}"
            , "Position": f"{self.position}", "Salary": f"{self.salary}"}
        return person

    def push(self):
        b = input("Введіть запис який потрібно додати = ")
        value = input(f"Введіть значення яке потрібно присвоїти запису {b} = ")
        person = {"Passport_data": f"{self.passport_data}", "Education": f"{self.education}",
                  "Specialty": f"{self.specialty}"
            , "Position": f"{self.position}", "Salary": f"{self.salary}"}
        person[b] = value
        return person


    def remove(self):
        a = input("Введіть запис який потрібно вилучити = ")
        person = {"Passport_data": f"{self.passport_data}", "Education": f"{self.education}",
                  "Specialty": f"{self.specialty}"
            , "Position": f"{self.position}", "Salary": f"{self.salary}"}
        del(person[f"{a}"])
        return person

    def find(self):
        c = input("Введіть запис який потрібно знайти = ")
        person = {"Passport_data": f"{self.passport_data}", "Education": f"{self.education}",
                  "Specialty": f"{self.specialty}"
            , "Position": f"{self.position}", "Salary": f"{self.salary}"}
        return f"{c}: {person[c]}"

vis = Datebase("2003.8.7", "Higher", "system_analysis", "student", 1)
print(vis.__str__())
print(vis.remove())
print(vis.push())
print(vis.find())