# -*- encoding: utf8 -*-
from math import pi, sqrt
from abc import ABC, abstractmethod

class Shape(ABC):
    ''' 도형 클래스 '''
    @abstractmethod
    def area(self):
        # '''도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩 할 것'''
        pass

    @abstractmethod
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
    def area(self):
        return sqrt(3) * self.side * self.side/4 # 정삼각형 넓이 공식 
    def perimeter(self):
        return 3 * self.side

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