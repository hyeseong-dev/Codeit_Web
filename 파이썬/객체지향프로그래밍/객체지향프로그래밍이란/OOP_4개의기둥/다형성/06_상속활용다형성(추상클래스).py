# -*- encoding: utf8 -*-
from math import pi 
from abc import ABC, abstractmethod
""" 
이전에서는 EquilateralTriangle 클래스를 만들고 area(), perimeter()를 오버라이딩하지 않고 Shape클래스를 상속받고 paint클래스의 인스턴스를 이용해 전체 넓이와 둘레를 구하려다가 오류가 난걸 확인했습니다. 

이때 해결 할 수 있는 방법이 바로 추상 클래스입니다. 

추상 클래스!!! 
: 여러 클래스들의 공통점을 추상화해서 모아놓은 클래스

자~ shpae클래스를 추상클래스로 만들어 봅시다.

여기서 도형(Shape)클래스는 : 넓이와 둘레를 어떻게든 계산할 줄 아는 어떤것이라고 정의해 둔것 

몇 가지 문법을 추가하여 Shpes 클래스에 수식해야할 것들이 필요합니다. 
0. from abc import ABC, abstractmethod 요렇게 임포트해줘야함. 

여기서 ABC는 (Abstract Base Class)의 줄임말입니다.

1. 추상 메서드 : 자식 클래스 오버라이딩 필요

!!!!중요!!!! 
추상 클래스로는 인스턴스를 만들 수 없습니다. 
즉, Shape(ABC)클래스로는 인스턴스를 직접적으로 생성할 수 없음.
"""

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


shape = Shape()
""" 
위의 추상 클래스로는 인스턴스를 생성 불가(X) 
추상클래스는 인스턴스를 생성하기 위한 목적이 없습니다. 
추상클래스는 여러 클래스의 공통점을 담아두고 다른 클래스들이 상속 받는 부모 클래스가 되려는 목적으로 존재한다.

즉 클래스는 1. 일반 클래스
            2. 추상 클래스
            로 구분 되어진다.
"""

triangle = EquilateralTriangle(4)
paint_program = Paint()
paint_program.add_shape(triangle)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())