# -*- encoding: utf8 -*-
from math import pi 
from abc import ABC, abstractmethod

'''
아래 Paint 클래스를 봅시다. 

class Paint: 
    def __init__(self):
        self.shapes = []
    
    def add_shape(self,shape):
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else: 
            print('넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다.')

위의 add_shape()메소드에서의 isinstance()메소드를 통해서 처음 들어오는 파라미터 첫번째가 Shape클래스인지 아닌지
bool값을 보낸다. 

LBYL                            - Look Before You Leap(뛰기 전에 살펴보라)
                                 : 하나하나씩 점검하고 일을 진행할 것.

EAFP(파이썬 스러운 스타일)       - Easier to Ask for Forgiveness than Permission(허락보단 용서가 쉽다.)
                                : 빠르게 실행하고 그 결과를 피드백해서 일을 진행할 것.

지금 Paint클래스는 LBYL 스타일로 작성되었는데요. 
만약 EAFP스타일로 변경한다면, 아래 주석의 코드와 같다.

    def __init__(self):
        self.shapes = []
    
    def add_shape(self,shape: Shape):
        # 그림판에 도형 인스턴스 Shape를 추가함. 단, shpae는 추상 클래스 Shape 인스턴스여야함.
        self.shapes.append(shape)

    def total_area_of_shapes(self):
        # 그림판에 있는 모든 도형의 넓이의 합을 구함
        total_area = 0 

        for shape in self.shapes:
            try: 
                total_area += shape.area()
            except(AttributeError, TypeError):
                print('그림판에 area 메서드가 없거나 잘못 정의되어 있는 인스턴스 {shape}가 있습니다.')

    def total_perimeter_of_shapes(self):
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        res_str = '그림판 안에 있는 도형들:\n\n'
        for shape in self.shapes: 
            res_str += str(shape) +'\n'
        return res_str



'''
class Shape:
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


class Paint: 
    ''' 넓이와 둘레를 구하는 area(), parimeter()메소드가 없어 Shape클래스를 상속 시키지 않았음'''
    def __init__(self):
        self.shapes = []
    
    def add_shape(self,shape: Shape):
        # 그림판에 도형 인스턴스 Shape를 추가함. 단, shpae는 추상 클래스 Shape 인스턴스여야함.
        self.shapes.append(shape)

    def total_area_of_shapes(self):
        # 그림판에 있는 모든 도형의 넓이의 합을 구함
        total_area = 0 

        for shape in self.shapes:
            try: 
                total_area += shape.area()
            except(AttributeError, TypeError):
                print(f'그림판에 area 메서드가 없거나 잘못 정의되어 있는 인스턴스 {shape}가 있습니다.')

        return total_area

    def total_perimeter_of_shapes(self):
        total_perimeter = 0 

        for shape in self.shapes:
            try: 
                total_perimeter += shape.perimeter()
            except(AttributeError, TypeError):
                print(f'그림판에 perimeter 메서드가 없거나 잘못 정의되어 있는 인스턴스 {shape}가 있습니다.')

        return total_perimeter


    def __str__(self):
        res_str = '그림판 안에 있는 도형들:\n\n'
        for shape in self.shapes: 
            res_str += str(shape) +'\n'
        return res_str


circle = Circle(4)
rectangle = Rectangle(3,4)

cylinder = Cylinder(4,3)

paint_program = Paint()

paint_program.add_shape(circle)
paint_program.add_shape(rectangle)
paint_program.add_shape(cylinder)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())

print(paint_program)