import turtle, line, rectangle, polygon, circle, ellipse


class Figures:
    def __init__(self, figure, i, t):
        lst = []
        for j in range(i):
            print(f"Enter {j + 1} argument:")
            lst.append(int(input()))

        self.figure = figure(lst, t)

    def draw(self):
        self.figure.draw()


if __name__ == '__main__':
    window = turtle.Screen()
    t = turtle.Turtle()
    print('Welcome to Draw Room!')

    print('[!] Let\'s draw Line')
    figure = Figures(line.Line, 1, t)
    t.color('red')
    figure.draw()
    t.setpos(0, 0)

    print('[!] Let\'s draw Rectangle')
    figure = Figures(rectangle.Rectangle, 2, t)
    t.color('green')
    figure.draw()
    t.setpos(0, 0)

    print('[!] Let\'s draw Polygon')
    figure = Figures(polygon.Polygon, 2, t)
    t.color('blue')
    figure.draw()
    t.setpos(0, 0)

    print('[!] Let\'s draw Circle')
    figure = Figures(circle.Circle, 1, t)
    t.color('purple')
    figure.draw()
    t.setpos(0, 0)

    print('[!] Let\'s draw Ellipse')
    figure = Figures(ellipse.Ellipse, 1, t)
    t.color('orange')
    figure.draw()
    t.setpos(0, 0)

    window.mainloop()

