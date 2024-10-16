from graphics import *

class Cell:
    def __init__(self, top_left: Point, bottom_right: Point, window: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = top_left.get_x()
        self.__y1 = top_left.get_y()
        self.__x2 = bottom_right.get_x()
        self.__y2 = bottom_right.get_y()
        self.__win = window
        self.visited = False

    def __eq__(self, other: "Cell"):
        return (
            self.__x1 == other.__x1
            and self.__y1 == other.__y1
            and self.__x2 == other.__x2
            and self.__y2 == other.__y2
        )
    
    def get_x1(self):
        return self.__x1
    
    def get_x2(self):
        return self.__x2
    
    def get_y1(self):
        return self.__y1
    
    def get_y2(self):
        return self.__y2
    
    def draw(self):
        if self.__win is None:
            return
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

    def erase(self, walls: list):
        if self.__win is None:
            # this is only here for the test cases where a window is not passed to the maze constructor
            for wall in walls:
                match wall:
                    case "left":
                        self.has_left_wall = False
                    case "right":
                        self.has_right_wall = False
                    case "top":
                        self.has_top_wall = False
                    case "bottom":
                        self.has_bottom_wall = False
            return
    
        for wall in walls:
            match wall:
                case "left":
                    self.has_left_wall = False
                    line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
                    self.__win.draw_line(line=line, fill_color="white")
                case "right":
                    self.has_right_wall = False
                    line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
                    self.__win.draw_line(line=line, fill_color="white")
                case "top":
                    self.has_top_wall = False
                    line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
                    self.__win.draw_line(line=line, fill_color="white")
                case "bottom":
                    self.has_bottom_wall = False
                    line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
                    self.__win.draw_line(line=line, fill_color="white")
    
    def draw_move(self, to_cell: "Cell", undo: bool = False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        from_point = Point((self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2)
        to_point = Point((to_cell.__x1 + to_cell.__x2) // 2, (to_cell.__y1 + to_cell.__y2) // 2)
        line = Line(from_point, to_point)
        self.__win.draw_line(line=line, fill_color=fill_color)