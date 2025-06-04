class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
def get_Circle(r):
    return Circle(r)
c=get_Circle(5)
print("area of Circle:",c.area())
