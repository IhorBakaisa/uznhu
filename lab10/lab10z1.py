# Об’єкт “Текст”
# поля:
#   ▪ для зберігання тексту;
#   ▪ для зберігання тематики вказаного тексту;
# методи:
#   ▪ визначення кількості символів у тексті;
#   ▪ визначення кількості слів (між словами один пробіл);
#   ▪ заміни кожного входження однієї букви на іншу;
#   ▪ видалення слова з вказаним порядковим номером.

class Text:
    def __init__(self, contens, text_theme):
        self.contens = contens
        self.text_theme = text_theme

    def __str__(self):
        return f"Text: \n Contens: {self.contens} \n Text_theme: {self.text_theme}"

    def number_of_characters(self):
        return f"Кількість символів у тексті = {len(self.contens)}"

    def number_of_words(self):
        words = len(self.contens.split())
        return f"Кількість слів у тексті = {words}"

    def letter_replacement(self):
        letter1 = input("Введіть букву яку потрібно замінити = ")
        letter2 = input("Введіть букву на яку потрібно замінити = ")
        a = list(self.contens)
        for i in range(len(a)):
            if a[i] == letter1:
                a[i] = letter2
        replacement = "".join(a)
        return replacement

    def delete_words(self):
        number = int(input("Введіть порядковий номер слова, який потрібно видалити = "))
        splitContens = self.contens.split()
        del splitContens[number-1]
        splitContens = " ".join(splitContens)
        return splitContens

abs = Text("I write laboratory work", "work")
print(abs)
print(abs.number_of_characters())
print(abs.number_of_words())
print(abs.letter_replacement())
print(abs.delete_words())

