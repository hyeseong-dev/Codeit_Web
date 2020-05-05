# -*- encoding: utf8 -*-

# 개
# class Dog: 
#     def __init__(self, speed_value: float):
#         self.speed = speed_value

#     def run(self):
#         print(f'강아지가 {self.speed}km/h의 속도로 달립니다')

# class Cat:
#     def __init__(self, speed_value: float):
#         self.speed = speed_value

#     def run(self):
#         print(f'고양이가 {self.speed}km/h의 속도로 달립니다')

# # 개 한 마리 생성

# dog = Dog(30)

# # 고양이 한 마리 생성
# cat = Cat(15)


# # 동물원에 강아지, 고양이 추가 
# zoo = []
# zoo.append(dog)
# zoo.append(cat)

# for animal in zoo: 
#     animal.run()
'''
지금 Dog 클래스와 Cat 클래스는 둘다 run 메소드를 갖고 있습니다. 
zoo라는 리스트에 Dog 인스턴스 하나와 Cat 인스턴스 하나를 추가했는데요. 
그리고나서 zoo 리스트에 있는 모든 인스턴스를 animal 변수에 대입해서 run 메소드를 호출하고 있습니다.
이렇게 클래스들이 공통적으로 갖고 있는 메소드를 호출하면 상속 없이도 다형성을 적용할 수 있는데요.


이런 코드에 대한 설명으로 틀린 것을 고르세요.

1
코드를 실행되기 전까지는 문제가 있는지 알 수 없다.

2
이 방식을 사용하면 개발자의 실수로 에러가 나기 쉽다.

3
이 방법은 코드로 구현하는 게 복잡하지 않기 때문에 간단한 프로그램을 만들 때 사용되기도 한다.

4
다른 방법들에 비해서 빨리 구현할 수 있기 때문에 권장되는 다형성 적용 방법이다.

[퀴즈 해설]
단순히 여러 클래스에 같은 메소드 이름을 정의하는 방식으로 다형성을 적용하면 실수를 하기가 쉽고 
코드의 유지 보수가 어려워 집니다. 
따라서 되도록 상소과 함께 다형성을 적용하는 것이 좋습니다. 위 코드를 상속을 사용해서 다시 적용해 보면 다음과 같습니다. 
'''

from abc import ABC, abstractmethod

# 동물을 나타내는 추상 클래스 

class Animal(ABC): 

    @abstractmethod
    def run(self):
        pass 

# 강아지 
class Dog(Animal):
    def __init__(self, speed_value):
        self.speed = speed_value 

    def run(self):
        print(f'강아지가 {self.speed}km/h의 속도로 달립니다')

# 고양이  :
class Cat(Animal):
    def __init__(self, speed_value):
        self.speed = speed_value 

    def run(self):
        print(f'고양이가 {self.speed}km/h의 속도로 달립니다')

dog = Dog(30)
cat = Cat(300)

zoo = []
# Animal 추상 클래스의 인스턴스인 경우에만 zoo 리스트에 추가 가능함

if isinstance(dog, Animal):
    zoo.append(dog)
if isinstance(cat, Animal):
    zoo.append(cat)

for animal in zoo:
    animal.run()

