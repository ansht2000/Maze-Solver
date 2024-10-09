from graphics import *

class Cell:
    def __init__(self, top_left: Point, bottom_right: Point, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = top_left.get_x()
        self.__y1 = top_left.get_y()
        self.__x2 = bottom_right.get_x()
        self.__y2 = bottom_right.get_y()
        self.__win = window
    
    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line=line, fill_color="black")
        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line=line, fill_color="black")
        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line=line, fill_color="black")
        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line=line, fill_color="black")