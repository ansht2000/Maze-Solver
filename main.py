from graphics import *
from cell import Cell

def main():
    win = Window(800, 600)
    line = Line(Point(0, 0), Point(300, 300))
    line_2 = Line(Point(800, 600), Point(300, 300))
    win.draw_line(line=line, fill_color="black")
    win.draw_line(line=line_2, fill_color="red")
    cell = Cell(Point(100,100), Point(150, 150), window=win)
    cell.draw()
    for i in range(0, 800, 50):
        for j in range(0, 600, 50):
            cell = Cell(Point(i, j), Point(i + 50, j + 50), win)
            cell.draw()
    win.wait_for_close()

main()