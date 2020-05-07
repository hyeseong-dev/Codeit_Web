# -*- encoding: utf-8 -*-
"""
파이썬에서 캡슐화를 하기 위해 변수나 메소드를 숨기려면 이름 앞에 밑줄 2개(__)를 붙여야 한다고 배웠습니다. 
그런데 사실 여기에는 특별한 원리가 숨어있습니다. 
"""

class Citizen: 
    """주민 클래스"""
    drinking_age = 19 # 음주가능 나이 

    def __init__(self, name,age,resident_id):
        """ 이름, 나이, 주민번호 """
        self.name = name 
        self.set_age(age)
        self.__resident_id = resident_id

    def authenticate(self, id_field):
        """ 본인이 맞는지 확인하는 메서드"""
        return self.__resident_id == id_field
    
    def can_drink(self):
        """음주 가능 나이인지 확인해주는 메서드"""
        return self.__age>= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메서드"""
        return f'{self.name} 씨는 {self.__age} 살입니다!'
    
    def get_age(self):
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
        return self.__age 
    
    def set_age(self, value=0):
        """ 숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 메소드"""
        if value < 0: 
            print('나이는 0보다 작을 수 없습니다. 기본 값 0으로 설정하겠습니다.')
            self.__age = value
        else: self.__age = value

# young = Citizen('harry potter',29, '123456')
# print(young.__str__())
# young.set_age()
# print(young.__str__())

"""
지금 Citizen 클래스의 변수 
    - __age
    - __resident_id
    는 클래스 밖에서 접근할 수 없는데요. 

    여기서 잠깐, Citizen 클래스의 내부를 들여다 봅시다. 다음 코드를 보세요. 
"""

# 시민 인스턴스 생성 

young = Citizen('younghoon kang',15, '87654321') # (1)
# print(dir(young))                               # (2) 

"""
(1) Citizen 클래스로 young라는 인스턴스를 하나 생성할게요. 
(2) dir이라는 함수를 사용하면 인스턴스가 갖고 있는 모든 변수와 메소드를 볼 수 있는데요. 

young 인스턴스의 모든 변수 및 메소드를 이름을 확인해 봅시다. 
위 코드를 실행하면 아래와 같이 실행됩니다. 

['_Citizen__age', '_Citizen__resident_id', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'authenticate', 'can_drink', 'drinking_age', 'get_age', 'name', 'set_age'

가장 앞에 있는 _Citizen__age, _Citizen__resident_id가 보이조? 이것이 바로 우리가 이름 앞에 밑줄 2개 붙였던 변수 __age, __resident_id입니다. 이게 무슨 말이냐고?

사실 변수나 메소드 이름 앞에 밑줄 두 개 (__)를 쓰면, 파이썬은 그 앞에 추가적으로 '_클래스 이름'을 덧붙여서 이름을 바꿔버립니다. 이걸 파이썬에서는 네임 맹글링(Name mangling)이라고 부릅니다. 맹글링(mangling)의 동사형인 mangle은 영어로 '마구 썰다','엉망진창으로 만들다'라는 뜻입니다. 여기서는 이름을 새로운 형태로 변환하는 것을 맹글링이라고 합니다. 그러니깐 방금 보신 것 처럼

     - __age는 _Citizen__age로 
     - __resident_id는 _Citizen__resident_id로 

     바뀌는 겁니다. 

     그럼 이 바뀐 이름으로는 클래스 밖에서도 접근할 수 있지 않을까요? 아래 코드는 바뀐 이름으로 변수에 접근하는 코드입니다. 
"""

print(young._Citizen__age)
print(young._Citizen__resident_id)

young._Citizen__age = -10
print(young)

"""
출력 결과를 보니 바뀐 이름으로는 클래스 밖에서도 접근이 가능하네요. 

정리하면 클래스 안에서 이름 앞에 밑줄2개(__)를 붙인 변수나 메소드는 네임 맹글링되어 아예 새로운 이름을 갖게 됩니다. 그리고 새 이름으로는 클래스 밖에서 접근이 가능합니다. 그럼 결국 클래스 밖에서도 접근할 수 있는 방법이 있으니깐 캡슐화가 안 된 거 아닐까요? 네, 맞습니다. 캡슐화가 안 된 겁니다. 아까는 밑줄 2개(__)만 붙이면 된다더니 무슨 말이냐구요?

사실 파이썬은 언어 차원에서 캡슐화를 지원하지 않습니다. private라는 키워드를 변수 이름 앞에 붙이면, 외부로부터의 접근이 완벽히 차단됩니다. 파이썬처럼 바뀐 새 이름으로 접근할 수 있다거나 하는 방법도 없습니다. Java에서는 캡슐화가 완벽하게 되는 것이조.add()

하지만 파이썬이 캡슐화를 지원하지 않는다고 해서 캡슐화를 아예 무시하는 것은 아닙니다. 파이썬 세계의 개발자들은 조금 다른 방식으로 캡슐화를 하는데요. 다음 파트에서 설명 이어집니다.
"""