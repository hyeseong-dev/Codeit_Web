# -*- encoding: utf8 -*-
from math import pi 

""" EquailateralTriangle은 현재 사각형, 원과 마찬가지로 Shape 클래스로부터 상속 받고 있습니다.

하지만, 여기서 차이점은 있습니다. 
바로 정삼각형 클래스는 원과 사각형 클래스처럼 area(), perimeter() 메서드를 오버라이딩 하지는 않습니다.

만약 아래에서 정삼각형 클래스로 인스턴스를 만들고 페인트 클래스의 인스턴스에 정삼각형 인스턴스를 넣어서 넓이와 둘레를 구하려고 하면 오류가 발생한다. 

왜? 정삼각형의 부모 클래스에 비록 area(), perimeter()가 있지만 pass로 했기 때문에 paint클래스의 전체 둘레와 넓이를 구하는 곳에서 값을 처리하지 못해 오류가 발생함.
"""

class Shape:
    ''' 도형 클래스 '''
    def area(self):
        # '''도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩 할 것'''
        pass

    def perimeter(self):
        # '''도형의 둘레를 리턴: 자식클래스가 오버라이딩 할 것'''
        pass

class Rectangle(Shape): 

    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width + self.height)
    def __str__(self):
        return f'밑변 {self.width}, 높이 {self.height}인 직사각형'

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius * self.radius
    def perimeter(self):
        return 2*pi * self.radius
    def __str__(self):
        return f'반지름 {self.radius}인 원'

class Cylinder:

    def __init__(self, radius, height):
        self.radius = radius 
        self.height = height 
    def __str__(self):
        return f'밑면 반지름 {self.radius}, 높이 {self.height}인 원기둥'

class EquilateralTriangle(Shape):

    def __init__(self,side):
        self.side = side

class Paint: 

    def __init__(self):
        self.shapes = []
    
    def add_shape(self,shape):
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else: 
            print('넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다.')
    def total_area_of_shapes(self):
        return sum([shape.area() for shape in self.shapes])
    
    def total_perimeter_of_shapes(self):
        return sum([shape.perimeter() for shape in self.shapes])
    def __str__(self):
        res_str = '그림판 안에 있는 도형들:\n\n'
        for shape in self.shapes: 
            res_str += str(shape) +'\n'
        return res_str

triangle = EquilateralTriangle(4)
paint_program = Paint()
paint_program.add_shape(triangle)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())