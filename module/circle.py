class Circle:
    __slots__ = ['__side', '__t']

    def __init__(self, side, t):
        self.__side = side[0]
        self.__t = t

    def draw(self):
        self.__t.circle(self.__side)


if __name__ == '__main__':
    l = Circle(int(input('Enter line size:\n')))
    l.draw()
