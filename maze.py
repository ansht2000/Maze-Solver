from graphics import *
from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1: int,
            y1: int,
            num_rows: int,
            num_cols: int,
            cell_size_x: int,
            cell_size_y: int,
            win: Window = None,
        ):
        self.cells = [[None for j in range(num_cols)] for i in range(num_rows)]
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        # loop through each cell in the maze in row-major order
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                # calculate positions of cells based on the number of the cell in the array
                cell = Cell(Point(self.__x1 + j * self.__cell_size_x, self.__y1 + i * self.__cell_size_y), Point(self.__x1 + (j + 1) * self.__cell_size_x, self.__y1 + (i + 1) * self.__cell_size_y), self.__win)
                self.cells[i][j] = cell
                cell.draw()
                self._animate()
        # for i in range(self.__num_rows):
        #     for j in range(self.__num_cols):
        #         self.cells[i][j].draw()
        #         self._animate()
    
    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(.05)

    def _break_entrance_and_exit(self):
        top_left: Cell = self.cells[0][0]
        bottom_right: Cell = self.cells[self.__num_rows - 1][self.__num_cols - 1]
        top_left.erase(["top"])
        bottom_right.erase(["bottom"])
        
