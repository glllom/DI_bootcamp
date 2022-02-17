from random import randint
from time import sleep
import pyautogui

SIZE_X = 20
SIZE_Y = 10
class Cell:
    def __init__(self, alive=True):
        self.alive = alive

class World:
    def __init__(self, size_x, size_y):
        self.cells = []
        for y in range(size_y):
            self.cells.append([])
            for _ in range(size_x):
                self.cells[y].append(Cell(randint(0, 1) == 1))

    def get_neighbours(self, x, y):
        neighbours = 0
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    qx, qy = x-1+j, y-1+i
                    if qx < 0 or qy < 0:
                        continue
                    try:
                        # noinspection PyUnresolvedReferences
                        neighbours += int(self.cells[qy][qx].alive)
                    except IndexError:
                        continue
        return neighbours

    def new_generation(self):
        for y in range(SIZE_Y):
            for x in range(SIZE_X):
                if self.cells[y][x].alive and self.get_neighbours(x, y) not in [2, 3]:
                    self.cells[y][x].alive = False
                elif not self.cells[y][x].alive and self.get_neighbours(x, y) == 3:
                    self.cells[y][x].alive = True

    def show(self):
        for row in self.cells:
            print(*(chr(11035) if cell.alive else chr(11036) for cell in row))


w = World(SIZE_X, SIZE_Y)

for _ in range(10):
    pyautogui.click(x=800, y=800)
    pyautogui.hotkey('Alt', 'l')
    w.show()
    w.new_generation()
    sleep(2)


