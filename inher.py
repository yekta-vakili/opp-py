class Shape:
    def __init__(self):
        self.Environment = 0
        self.Area = 0
    def out1(self):
        pass
    def out2(self):
        pass



class Rectangle(Shape):  
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.Environment = (self.height+self.width)*2
        self.Area = self.height*self.width
    def out1(self):
        return self.Environment
    def out2(self):
        return self.Area    


class Circle(Shape):  
    def __init__(self, radius=0):
        self.radius = radius
        self.Area = (self.radius * self.radius * 3.14)
        self.Environment = self.radius*2*3.14
    def out1(self):
        return self.Environment
    def out2(self):
        return self.Area 


shapes = [Rectangle(6, 10), Circle(20)]
print("Area of rectangle is:", str(shapes[0].out1()))
print("Environment of rectangle is:", str(shapes[0].out2()))
print("=============================")
print("Area of circle is:", str(shapes[1].out1()))
print("Environment of circle is:", str(shapes[1].out2()))