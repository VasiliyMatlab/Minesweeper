import tkinter as tk
from random import shuffle

class MyButton(tk.Button):
    BUTTON_WIDTH = 3            # размер кнопки
    FONT = "Calibri 15 bold"    # шрифт

    def __init__(self, master, x, y, number, *args, **kwargs) -> None:
        super(MyButton, self).__init__(master, width=MyButton.BUTTON_WIDTH,\
            font=MyButton.FONT, *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False

    def __repr__(self) -> str:
        return f"MyButton {self.number} {self.is_mine} {{{self.x}, {self.y}}}"


class MineSweeper:
    window = tk.Tk()    # создание окна
    ROWS    = 5         # кол-во строк
    COLUMNS = 5         # кол-во столбцов
    MINES  = 10         # кол-во мин

    def __init__(self) -> None:
        # Создаем кнопки
        self.buttons = list()
        count = 1
        # Цикл по строкам
        for i in range(MineSweeper.ROWS):
            temp = list()
            # Цикл по столбцам
            for j in range(MineSweeper.COLUMNS):
                btn = MyButton(MineSweeper.window, x=i, y=j, number=count)
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
                count += 1
            self.buttons.append(temp)

    # Обработчик нажатия кнопки
    def click(self, clicked_button: MyButton):
        print(clicked_button)
        if clicked_button.is_mine:
            clicked_button.config(text="*", background="red", \
                disabledforeground="black")
        else:
            clicked_button.config(text=clicked_button.number, \
                disabledforeground="black")
        clicked_button.config(state="disabled")

    # Создание кнопок
    def create_widgets(self):
        # Цикл по строкам
        for i in range(MineSweeper.ROWS):
            # Цикл по столбцам
            for j in range(MineSweeper.COLUMNS):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    # Старт игры
    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.print_buttons()
        MineSweeper.window.mainloop()
    
    # Вывод кнопок в консоль
    def print_buttons(self):
        for row in self.buttons:
            print(row)

    # Расстановка мин
    def insert_mines(self):
        mines_indexes = self.get_mines_places()
        for row in self.buttons:
            for btn in row:
                if btn.number in mines_indexes:
                    btn.is_mine = True

    # Генерация расположения мин
    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.ROWS*MineSweeper.COLUMNS + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]

game = MineSweeper()
game.start()