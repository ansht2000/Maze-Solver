from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line: "Line", fill_color: str):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"({self.__x}, {self.__y})"
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.__start = start_point
        self.__end = end_point

    def __repr__(self):
        return f"{self.__start} -> {self.__end}"

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__start.get_x(), self.__start.get_y(), self.__end.get_x(), self.__end.get_y(), fill = fill_color, width = 2
        )
