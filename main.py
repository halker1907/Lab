import tkinter as tk
import app_ganerate
CANVAS_BG = 'red'
WINDOW_BG = 'black'
COLOR_PLAYER = 'yellow'
EMPTY = '█'
WALL = '░'
EXIT = 'X'
MAZE_COLORS = {
    WALL: 'black',
    EXIT: 'red',
    EMPTY: 'green',
}

class App():
    def __init__(self, cols, rows):
        self.window = tk.Tk()
        self.cols = cols
        self.rows = rows
        self.min_side = min(self.window.winfo_screenwidth() // self.cols, self.window.winfo_screenheight() // self.rows) 
        self.tile_size = self.min_side // max(cols, rows)
        self.maze = None
        self.player = None
        self.is_running = False
        self.window.attributes('-fullscreen', True, bg=WINDOW_BG) 
        self.window.bind('<Key>', self.on_key)
        self.canvas = tk.Canvas(
            self.window,
            width=self.cols * self.tile_size,
            height=self.rows * self.tile_size,
            highlightthickness=0
            )
        self.canvas.pack(expand=True, fill='both')
        self.draw_maze()
        self.window.mainloop()
    
    def draw_maze(self):
        for row_idx, row in enumerate(self.maze):#энумерейт возвращяет кортежи
            for col_idx, col in enumerate(row):
                self.canvas.create_rectangle(
                    col_idx * self.tile_size,
                    row_idx * self.tile_size,
                    col_idx * self.tile_size + self.tile_size,
                    row_idx * self.tile_size + self.tile_size,
                    fill=MAZE_COLORS[col]
                    )
        
    def start(self):
        self.maze = app_ganerate.generate_maze(cols=self.cols, rows=self.cols)
        self.draw_maze()
        self.player = Player(self, self.rows - 2, 1, self.tile_size, COLOR_PLAYER)
        self.is_running = True


    def on_key(self, event: tk.Event) -> None:
        if event.keysym == 'Escape':
            self.window.destroy()
'''
TODO во втором файле сделать GUI 
'''
class Player:
    def __init__(self, game: App, row: int, col: int, size: int, color: str) -> None:
        self.game = game
        self.col = col
        self.row = row
        self.size = size
        self.color = color
        self.draw()



    def draw(self):
        self.game.canvas.create_rectangle(
            self.col * self.game.tile_size,
            self.row * self.game.tile_size,
            self.col * self.game.tile_size + self.game.tile_size,
            self.row * self.game.tile_size + self.game.tile_size,
            fill=self.color
        )
    def move(self):
        pass
            
App(51, 27)