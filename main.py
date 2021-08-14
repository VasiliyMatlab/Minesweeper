import tkinter as tk


class MineSweeper:
    # Создаем окно
    window = tk.Tk()
    ROWS    = 10 # кол-во строк
    COLUMNS = 7  # кол-во столбцов
    BUTTON_WIDTH = 3 # размер кнопки
    FONT = "Calibri 15 bold" # шрифт

    def __init__(self) -> None:
        # Создаем кнопки
        self.buttons = list()
        # Цикл по строкам
        for i in range(MineSweeper.ROWS):
            temp = list()
            # Цикл по столбцам
            for j in range(MineSweeper.COLUMNS):
                btn = tk.Button(MineSweeper.window, \
                    width=MineSweeper.BUTTON_WIDTH, font=MineSweeper.FONT)
                temp.append(btn)
            self.buttons.append(temp)

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
        self.print_buttons()
        MineSweeper.window.mainloop()
    
    # Вывод кнопок в консоль
    def print_buttons(self):
        for row in self.buttons:
            print(row)


game = MineSweeper()
game.start()