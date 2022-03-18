class Ellipse:
    __slots__ = ['__side', '__t']

    def __init__(self, side, t):
        self.__side = side[0]
        self.__t = t

    def draw(self):
        for i in range(2):
            self.__t.circle(self.__side, 90)
            self.__t.circle(self.__side // 2, 90)


if __name__ == '__main__':
    l = Line(int(input('Enter line size:\n')))
    l.draw()
