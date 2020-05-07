# -*- encoding: utf8 -*-
from math import pi 

'''
3개의 클래스를 사용해 봅시다.(Rectangle, Circle, Paint)

다형성은 말 그대로 다(많을 다) 형성(형태와 성질)을 뜻한다. 
즉, 여러가지 많은 성질과 형태를 가진것을 다형성이라고 합니다. 

아래의 shape 객체는 어떤 경우에는 Circile객체의 인스턴스 속성을 갖고 어떨때는 Rectangle의 인스턴스 속성을 갖는 카멜레온 같은 놈이 되는 것입니다.

다시 한번 명심 해야할 것은 해당 다형성을 갖추기 위해서는, 
두 가지 클래스가 사전에 같은 이름의 area()메소드와 perimeter()라는 공통분모가 있기에 가능한 것임.
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
        info_rectangle = f"""너비: {self.width}, 높이: {self.height}"""
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
        return sum([shape.area() for shape in self.shapes]) # area()메소드는  원이나 네모에 있는 area()메소드를 소환해서 여기서 해당 도형의 넓이를 계산해서 리스트에 값을 추가하고 마무리로 sum()메소드에 의해 도형1,도형2,도형n개가 전체의 넓이 합을 구할 수 있게 되는 원리
        """ 여기서 shape가 Rectangle인스턴스와 Circle인스턴스를 가리키고 있는 것을 다형성이 있다라고 정의 내릴 수 있다. (둘다 area(), perimeter()를 가지고 있음.) """

    def total_perimeter_of_shapes(self):
        ''' 그림판에 있는 모든 도형의 둘레를 구한다.'''
        return sum([shape.perimeter() for shape in self.shapes])
    
    def __str__(self):
        ''' 그림판에 있는 각 도형들의 정보를 출력'''
        res_str = '그림판 안에 있는 도형들:\n\n'
        for shape in self.shapes: 
            res_str += str(shape) +'\n'
        return res_str


rectangle = Rectangle(3,7)
circle = Circle(4)

paint_program = Paint()

''' 이 다음엔 그림판에 원과 직사각형을 추가하겠습니다.'''
paint_program.add_shape(rectangle)
paint_program.add_shape(circle)

''' 그림판에 있는 모든 도형들의 넓이의 합을 구해 봅시다.'''
print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())

