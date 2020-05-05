"""
_ 언더바 1개일때는
setter,getter 메소드를 사용할때, 그리고 클래스 밖에서 외부의 접근을 막을때 사용합니다. 

__ 언더바 2개는 상속 받게될때 변수나 메서드 명이 같은 경우 이를 피하기 위해 사용합니다. 

"""

class Citizen: 
    """주민 클래스"""
    drinking_age = 19 # 음주가능 나이 

    def __init__(self, name,age,resident_id):
        """ 이름, 나이, 주민번호 """
        self.name = name 
        self.age = age
        self._resident_id = resident_id

    def authenticate(self, id_field):
        """ 본인이 맞는지 확인하는 메서드"""
        return self._resident_id == id_field
    
    def can_drink(self):
        """음주 가능 나이인지 확인해주는 메서드"""
        return self._age>= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메서드"""
        return f'{self.name} 씨는 {self._age} 살입니다!'
    
    def get_age(self):
        """숨겨 놓은 인스턴스 변수 _age의 값을 받아오는 메소드"""
        return self._age 
    
    def set_age(self, value=0):
        """ 숨겨 놓은 인스턴스 변수 _age의 값을 설정하는 메소드"""
        if value < 0: 
            print('나이는 0보다 작을 수 없습니다. 기본 값 0으로 설정하겠습니다.')
            self._age = value
        else: self._age = value

    @property # getter 메서드 
    def age(self):
        print("나이를 리턴합니다.")
        return self._age
    
    @age.setter# setter 메서드 
    def age(self,value):
        print("나이를 설정합니다.")
        if value < 0: 
            print('나이는 0보다 작을수 없습니다. 기본 값 0으로 초기화')
            self._age = 0
        else: 
            self._age = value



young = Citizen('hong gil dong', 15, '87654321')
print(young.age) # getter메서드로 출력하는 방법 ()가 없어야함. 

young.age = 30 #age 바로 뒤에 ()붙이면 오류 뜬다. 
print(young.age)













"""
property 데코레이터 
변수의 값을 읽거나 설정하는 구문 
-> 아예 다른 의미로 실행

Quiz
Citizen 클래스에는 age와 _age중 어떤 인스턴스 변수가 있는건가요?

정답: _age입니다. 
걍 age는 _age에 대한 getter메소드, setter메소드의 이름입니다.

property 데코레이터의 장점! 
1. 캡슐화 전 사용하던 코드를 캡슐화 후 수정X

만약 property 데코레이터 없이 getter/setter로 적용한다면 
print(get_age())
set_age(30) 
print(get_age()) 과 같이 적용해야 한다.

가장 좋은 점은 원래 변수이름을 가진 메서드를 만들기에 헷갈릴 일이 없어진다. 

@property
def age(self):
    return self._age

@age.setter
def age(self,value):
    self._age = value

"""