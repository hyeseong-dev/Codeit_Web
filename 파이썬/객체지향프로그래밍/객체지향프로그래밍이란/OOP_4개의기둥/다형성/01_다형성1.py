# -*- encoding: utf8 -*-
from math import pi 

'''
그림판을 만들어 다형성 수업을 시작해 봅시다.

첫째, 직사각형을 나타내는 직사각형 클래스를 만들어 봅시다. 
'''

class Rectangle: 
    '''직사각형 클래스'''
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        '''직사각형의 넓이를 리턴함'''
        return self.width * self.height
    
    def perimeter(self):
        '''직사각형의 둘레를 리턴'''
        return 2*(self.width + self.height)
    
    def __str__(self):
        '''직사각형의 정보를 문자열로 리턴'''
        info_rectangle = f"""
너비: {self.width}, 높이: {self.height}
둘레: {self.perimeter()}, 넓이: {self.area()} 
                        """
        return info_rectangle


class Circle:

    def __init__(self, radius): 
        self.radius = radius
    
    def area(self):
        '''원의 넓이를 리턴'''
        return pi * self.radius * self.radius # pi * r의 2제곱근

    def perimeter(self):
        '''원의 둘레를 리턴'''
        return 2 * pi * self.radius # 2*pi * r    

    def __str__(self):
        '''원의 정보를 문자열로 리턴'''
        return f'반지름: {self.radius}, 넓이: {self.area()}, 둘레: {self.perimeter()} '


class Paint: 
    ''' 그림판으로 프로그램 클래스'''
    def __init__(self):
        self.shapes = []
    
    def add_shape(self,shape):
        '''그림판으로 도형을 추가'''
        self.shapes.append(shape)
    
    def total_area_of_shapes(self):
        '''그림판에 있는 모든 도형의 넓이를 구한다'''
        return sum([shapes.area() for shape in self.shapes])

    def total_perimeter_of)shapes(self):
        ''' 그림판에 이쓴ㄴ 모든 도형의 둘레를 구한다.'''
        return sum([shape.perimeter() for shape in self.shapes])
    
    def __str__(self):
        ''' 그림판에 있는 각 도형들의 정보를 출력'''
        res_str = '그림판 안에 있는 도형들:\n\n'
        for shape in self.shapes: 
            res_str += str(shape) +'\n'
        return res_str





rect = Rectangle(10,12)

print(rect.__str__())

