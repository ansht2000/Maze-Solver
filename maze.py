from graphics import *
from cell import Cell
import time
import random

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
            seed = None
        ):
        self.cells = [[None for j in range(num_cols)] for i in range(num_rows)]
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self.reset_visited(self.cells)

    def get_cell_from_indices(self, i: int, j: int):
        cell = Cell(Point(self.__x1 + j * self.__cell_size_x, self.__y1 + i * self.__cell_size_y), Point(self.__x1 + (j + 1) * self.__cell_size_x, self.__y1 + (i + 1) * self.__cell_size_y), self.__win)
        return cell

    def _create_cells(self):
        # loop through each cell in the maze in row-major order
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                # calculate positions of cells based on the number of the cell in the array
                cell = self.get_cell_from_indices(i, j)
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

    def _break_walls_r(self, i: int, j: int):
        self.cells[i][j].visited = True
        while True:
            to_visit = []
            # pick which cells to visit next
            # top
            if i > 0 and not self.cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # bottom
            if i < self.__num_rows - 1 and not self.cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # left
            if j > 0 and not self.cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self.__num_cols - 1 and not self.cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            # if there are no cells to visit, draw the cell and break
            if len(to_visit) == 0:
                self.cells[i][j].draw()
                return
            # randomly choose a cell to visit next
            cell_to_visit = random.choice(to_visit)
            # top
            if cell_to_visit[0] == i - 1:
                self.cells[i][j].erase(["top"])
                self.cells[i - 1][j].erase(["bottom"])
            # bottom
            if cell_to_visit[0] == i + 1:
                self.cells[i][j].erase(["bottom"])
                self.cells[i + 1][j].erase(["top"])
            # left
            if cell_to_visit[1] == j - 1:
                self.cells[i][j].erase(["left"])
                self.cells[i][j - 1].erase(["right"])
            if cell_to_visit[1] == j + 1:
                self.cells[i][j].erase(["right"])
                self.cells[i][j + 1].erase(["left"])
            self._animate()
            # call break_walls recursively on the cell to visit
            self._break_walls_r(cell_to_visit[0], cell_to_visit[1])

    def reset_visited(self, cells: list[Cell]):
        for cell_list in cells:
            for cell in cell_list:
                cell.visited = False
        





        
