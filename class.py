class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """
        the point's string method.When print an object,the __str__ method is called
        """
        return str((self.x, self.y))

    def move_point(self, dx, dy):
        self.x += dx
        self.y += dy
        return (self.x, self.y)


MyPoint = Point(12, 12)
print('after initializing the point:', MyPoint)
print('after moving the point:', MyPoint.move_point(-8, 6))
