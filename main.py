from graphics import *
from cell import Cell
from maze import Maze

def main():
    # win = Window(800, 600)
    # line = Line(Point(0, 0), Point(300, 300))
    # line_2 = Line(Point(800, 600), Point(300, 300))
    # win.draw_line(line=line, fill_color="black")
    # win.draw_line(line=line_2, fill_color="red")
    # cell = Cell(Point(100,100), Point(150, 150), window=win)
    # cell.draw()
    # for i in range(0, 800, 100):
    #     for j in range(0, 600, 100):
    #         cell = Cell(Point(i, j), Point(i + 50, j + 50), win)
    #         cell2 = Cell(Point(i + 50, j + 50), Point(i + 100, j + 100), win)
    #         cell.draw()
    #         cell2.draw()
    #         cell.draw_move(cell2)
    # cell = Cell(Point(100,100), Point(150, 150), window=win)
    # cell.draw()
    # cell2 = Cell(Point(150,100), Point(200, 150), window=win)
    # cell2.draw()
    # cell.draw_move(cell2)
    # c1 = Cell(Point(50, 50), Point(100, 100), win)
    # c1.has_right_wall = False
    # c1.draw()

    # c2 = Cell(Point(100, 50), Point(150, 100), win)
    # c2.has_left_wall = False
    # c2.has_bottom_wall = False
    # c2.draw()

    # c1.draw_move(c2)

    # c3 = Cell(Point(100, 100), Point(150, 150), win)
    # c3.has_top_wall = False
    # c3.has_right_wall = False
    # c3.draw()

    # c2.draw_move(c3)

    # c4 = Cell(Point(150, 100), Point(200, 150), win)
    # c4.has_left_wall = False
    # c4.draw()

    # c3.draw_move(c4, True)
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    win.wait_for_close()

main()