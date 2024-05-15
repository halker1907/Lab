import tkinter as tk
CANVAS_BG = 'red'
"""
1.список списка или список строк
2.Полностью заполнить лабиринт стенами
3.Количество колонн и рядов - нечетное
4.бульд начинает сносить стены в четных клетках
5.если в двух клетках от него стены - ломает обе
6.когда во всех четных клетках нет стен лабиринт проходим
7.надо по границам обрисовать стеной, и сделать вход с выходом
    '░'
"""
window = tk.Tk()
window.geometry("250x200")
canvas = tk.Canvas(
    window,
    width=250,
    height=200,
    bg=CANVAS_BG,
    highlightthickness=0
)
canvas.pack(expand=True)
canvas.update()
row = [
    '▓',
]
window.mainloop()