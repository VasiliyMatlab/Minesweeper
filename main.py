import tkinter as tk

ROWS    = 5 # кол-во строк
COLUMNS = 7 # кол-во столбцов

# Создаем окно
window = tk.Tk()
#
FONT = "Calibri 15 bold"

# Создаем кнопки
buttons = list()
BUTTON_WIDTH = 3
# Цикл по строкам
for i in range(ROWS):
    temp = list()
    # Цикл по столбцам
    for j in range(COLUMNS):
        btn = tk.Button(window, width=BUTTON_WIDTH, font=FONT)
        btn.grid(row=i, column=j)
        temp.append(btn)
    buttons.append(temp) 

window.mainloop()