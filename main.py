import tkinter as tk
import app_ganerate
CANVAS_BG = 'red'
WINDOW_BG = 'yellow'
EMPTY = '█'
WALL = '░'
EXIT = 'X'
MAZE_COLORS = {
    WALL = 'black'
    EXIT = 'red'
    EMPTY = 'green'
}
TODO: #сделать в др файле штуку которая будет делать мейз generate_maze(COLS=self.cols, ROWS=self.cols)

class App():
    def __init__(self):
        self.window = tk.Tk()
        self.cols = 51
        self.rows = 27
        self.tile_size = 40
        self.maze = app_ganerate.generate_maze(COLS=self.cols, ROWS=self.cols)
        self.window.attributes('-fullscreen', True) 
        self.window.bind('<Key>', self.on_key)
        self.canvas = tk.Canvas(
            self.window, highlightthickness=0)
        self.canvas.pack(expand=True, fill='both')
        self.draw_maze()
        self.window.mainloop()
    
    def draw_maze(self):
        for row_idx, row in enumerate(self.maze):#энумерейт возвращяет кортежи
            for col_idx, col in enumerate(self.row):
                self.canvas.create_rectangle(col_idx * self.tile_size + self.tile_size, row_idx * self.tile_size, col_idx * self.tile_size + self.tile_size, row_idx * self.tile_size, fill=MAZE_COLORS[col])

    def on_key(self, event: tk.Event) -> None:
        if event.keysym == 'Escape':
            self.window.destroy()
'''
TODO во втором файле сделать GUI 
'''