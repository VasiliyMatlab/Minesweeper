import tkinter as tk
from random import shuffle

# Цвета цифр
colors = {
    0: "#ffffff",
    1: "#038cfc",
    2: "#02cc24",
    3: "#a88402",
    4: "#91008a",
    5: "#cc2a02",
    6: "#1400ab",
    7: "#366946",
    8: "#3b2626",
}


class MyButton(tk.Button):
    BUTTON_SIZE = 3             # размер кнопки
    FONT = "Calibri 15 bold"    # шрифт

    def __init__(self, master, x, y, number=0, *args, **kwargs) -> None:
        super(MyButton, self).__init__(master, width=MyButton.BUTTON_SIZE,\
            height=MyButton.BUTTON_SIZE, font=MyButton.FONT, *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0
        self.is_open = False

    def __repr__(self) -> str:
        return f"MyButton {self.number} {self.is_mine} {{{self.x}, {self.y}}}"


class MineSweeper:
    window  = tk.Tk()   # создание окна
    ROWS    = 10        # кол-во строк
    COLUMNS = 10        # кол-во столбцов
    MINES   = 10        # кол-во мин

    def __init__(self) -> None:
        # Создаем кнопки
        self.buttons = list()
        # Цикл по строкам
        for i in range(MineSweeper.ROWS + 2):
            temp = list()
            # Цикл по столбцам
            for j in range(MineSweeper.COLUMNS + 2):
                btn = MyButton(MineSweeper.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
            self.buttons.append(temp)

    # Обработчик нажатия кнопки
    def click(self, clicked_button: MyButton):
        print(clicked_button)
        if clicked_button.is_mine:
            clicked_button.config(text="*", background="red", \
                disabledforeground="black")
            clicked_button.is_open = True
        else:
            if clicked_button.count_bomb:
                color = colors.get(clicked_button.count_bomb, "black")
                clicked_button.config(text=clicked_button.count_bomb, \
                    disabledforeground=color)
                clicked_button.is_open = True
            else:
                self.breadth_first_search(clicked_button)
        clicked_button.config(state="disabled", relief=tk.SUNKEN)

    # Открытие свободных клеток (алгоритм обхода в ширину)
    def breadth_first_search(self, btn: MyButton):
        queue = [btn]
        while queue:
            # Открываем текущую кнопку
            cur_btn = queue.pop()
            color = colors.get(cur_btn.count_bomb, "black")
            if cur_btn.count_bomb:
                cur_btn.config(text=cur_btn.count_bomb, \
                    disabledforeground=color)
            else:
                cur_btn.config(text='', disabledforeground=color)
            cur_btn.is_open = True
            cur_btn.config(state="disabled", relief=tk.SUNKEN)
            # Обрабатываем соседей
            if not cur_btn.count_bomb:
                x, y = cur_btn.x, cur_btn.y
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        '''if not abs(dx-dy) == 1:
                            continue'''
                        next_btn = self.buttons[x+dx][y+dy]
                        '''if not next_btn.is_open and \
                                1<=next_btn.x<=MineSweeper.ROWS and \
                                1<=next_btn.y<=MineSweeper.COLUMNS and \
                                next_btn not in queue:'''
                        # Если кнопка не была открыта, не барьерная и 
                        # ее нет в очереди, то добавляем в очередь
                        if not next_btn.is_open and next_btn.number != 0 and \
                                next_btn not in queue:
                            queue.append(next_btn)

    # Создание кнопок
    def create_widgets(self):
        # Цикл по строкам
        for i in range(1, MineSweeper.ROWS + 1):
            # Цикл по столбцам
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    # Отображение открытого поля
    def open_all_buttons(self):
        # Цикл по строкам
        for i in range(MineSweeper.ROWS + 2):
            # Цикл по столбцам
            for j in range(MineSweeper.COLUMNS + 2):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(text="*", background="red", \
                        disabledforeground="black")
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, "black")
                    btn.config(text=btn.count_bomb, \
                        disabledforeground="black", fg = color)

    # Старт игры
    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.count_mines_in_buttons()
        self.print_buttons()
        #self.open_all_buttons()
        MineSweeper.window.mainloop()
    
    # Вывод кнопок в консоль
    def print_buttons(self):
        for i in range(1, MineSweeper.ROWS + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print('B', end='')
                else:
                    print(btn.count_bomb, end='')
            print()

    # Расстановка мин
    def insert_mines(self):
        mines_indexes = self.get_mines_places()
        count = 1
        # Цикл по строкам
        for i in range(1, MineSweeper.ROWS + 1):
            # Цикл по столбцам
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                btn.number = count
                if btn.number in mines_indexes:
                    btn.is_mine = True
                count += 1

    # Подсчет кол-ва мин вокруг каждой ячейки
    def count_mines_in_buttons(self):
        # Цикл по строкам
        for i in range(1, MineSweeper.ROWS + 1):
            # Цикл по столбцам
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[i+row_dx][j+col_dx]
                            if neighbour.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb

    # Генерация расположения мин
    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.ROWS*MineSweeper.COLUMNS + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]

game = MineSweeper()
game.start()