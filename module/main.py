import turtle, line, rectangle, polygon, circle, ellipse


class Figures:
    def __init__(self, x, t):
        self.__x = x
        if x == 1:
            self.Line = line.Line(int(input('Enter line size:\n')),t)

        elif x == 2:
            x = int(input('Enter width size:\n'))
            y = int(input('Enter height size:\n'))
            self.Rectangle = rectangle.Rectangle([x, y, x, y], t)

        elif x == 3:
            self.Polygon = polygon.Polygon(int(input('Enter side size:\n')), int(input('Enter side amount:\n')), t)

        elif x == 4:
            self.Circle = circle.Circle(int(input('Enter radius:\n')), t)

        elif x == 5:
            self.Ellipse = ellipse.Ellipse(int(input('Enter radius:\n')), t)

    def draw(self):
        if self.__x == 1:
            self.Line.draw()

        if self.__x == 2:
            self.Rectangle.draw()

        if self.__x == 3:
            self.Polygon.draw()

        if self.__x == 4:
            self.Circle.draw()

        if self.__x == 5:
            self.Ellipse.draw()


if __name__ == '__main__':
    win = turtle.Screen()
    t = turtle.Turtle()
    print('Welcome to Draw Room!')
    print(
        'What to Draw: [1 - Line, 2 - Rectangle, 3 - Polygon(Triangle, Square, Hexagon, N-angle), 4 - Circle, 5 - Ellipse, 0 - Exit]')
    x = int(input())
    while x:
        f = Figures(x, t)
        f.draw()
        print(
            'What to Draw: [1 - Line, 2 - Rectangle, 3 - Polygon(Triangle, Square, Hexagon, N-angle), 4 - Circle, 5 - Ellipse, 0 - Exit]')
        x = int(input())
        t.clear()
        t.setpos(0,0)
        t.reset()

    t.bye()
