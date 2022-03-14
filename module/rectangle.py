class Rectangle:
    __slots__ = ['__sides', '__t']

    def __init__(self, sides, t):
        self.__sides = sides
        self.__t = t

    def draw(self):
        for side in self.__sides:
            self.__t.forward(side)
            self.__t.left(90)


if __name__ == '__main__':
    l = Rectangle([120,60,120,60])
    l.draw()

