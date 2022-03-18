import turtle, line, rectangle, polygon, circle, ellipse


class Figures:
    def __init__(self, figure, i, t):
        w = []
        for j in range(i):
            print(f"Enter {j + 1} argument:")
            w.append(int(input()))

        self.figure = figure(w, t)

    def draw(self):
        self.figure.draw()


if __name__ == '__main__':
    win = turtle.Screen()
    t = turtle.Turtle()
    print('Welcome to Draw Room!')

    print('[!] Let\'s draw Line')
    f = Figures(line.Line, 1, t)
    t.color('red')
    f.draw()
    t.setpos(0, 0)

    print('[!] Let\'s draw Rectangle')
    f = Figures(rectangle.Rectangle, 2, t)
    t.color('green')
    f.draw()
    t.setpos(0, 0)

    print('[!] Let\'s draw Polygon')
    f = Figures(polygon.Polygon, 2, t)
    t.color('blue')
    f.draw()
    t.setpos(0, 0)

    print('[!] Let\'s draw Circle')
    f = Figures(circle.Circle, 1, t)
    t.color('purple')
    f.draw()
    t.setpos(0, 0)

    print('[!] Let\'s draw Ellipse')
    f = Figures(ellipse.Ellipse, 1, t)
    t.color('orange')
    f.draw()
    t.setpos(0, 0)

    win.mainloop()

