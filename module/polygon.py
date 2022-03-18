class Polygon:
    __slots__ = ['__side', '__amount', '__t']

    def __init__(self, sides,t):
        self.__side = sides[0]
        self.__amount = sides[1]
        self.__t = t

    def draw(self):
        for _ in range(self.__amount):
            self.__t.forward(self.__side)
            self.__t.right(360 / self.__amount)


if __name__ == '__main__':
    l = Polygon(120,3)
    l.draw()
