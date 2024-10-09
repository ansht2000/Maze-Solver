from graphics import *


def main():
    win = Window(800, 600)
    line = Line(Point(0, 0), Point(300, 300))
    line_2 = Line(Point(800, 600), Point(300, 300))
    win.draw_line(line=line, fill_color="black")
    win.draw_line(line=line_2, fill_color="red")
    win.wait_for_close()

main()