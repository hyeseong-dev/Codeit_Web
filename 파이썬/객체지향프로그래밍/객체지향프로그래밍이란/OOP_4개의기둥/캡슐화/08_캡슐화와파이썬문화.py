"""
파이썬 언어 자체는 캡슐화를 지원하지 않습니다. 
그럼 파이썬 개발자들은 캡슐화를 코드에 적용하지 않는건가?

당연히 그렇지는 안겠지요?! 

언어에서 지원하지 않지만 개발자들은 캡슐화에 대한 문하를 만들었습니다. 

방법. 
        - 변수와 메서드에 함부로 접근하지 말라는 이정표를 세우는것. 

        관례적으로,  _변수 _메서드 

        언더바 하나는 _ 클래스 밖에서 직접 접근해서 사용하지 말라는 경고 표시입니다.
        파이썬 개발자들은 이 경고 표시를 약속처럼 지킵니다.add()


"""

class Citizen: 
    """주민 클래스"""
    drinking_age = 19 # 음주가능 나이 

    def __init__(self, name,age,resident_id):
        """ 이름, 나이, 주민번호 """
        self.name = name 
        self.set_age(age)
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

young = Citizen('hong gil dong', 18, '12345678')

print(young._age) # 개발자들의 약속을 쌩까고 클래스 밖에서 호출한코드
print(young._resident_id)# 개발자들의 약속을 쌩까고 클래스 밖에서 호출한코드

# print(young._Citizen_age) # 오류 발생
young.set_age(10)
print(young.get_age())

"""
_ (언더바1개)는 아무런 기능이 없습니다. 단순히 다른 개발자에게 보내는 경고 그 이상도 그 이하도 아닙니다.

경고 의미: "이 변수/메서드는 클래스 외부에서 직접 접근하지 마세요."

만약 경고를 무시하고 클래스 외부에서 객체의 값에 직접 접근하고 수정하면 객체의 상태가 맛이가거나 코드가 엉키게 된다.

결론: 

캡슐화를 할 때는 앞으로 언더바 2개 대신-> 언더바 1개로 캡슐화를 진행합시다.

그리고 _하나를 붙이 변수에 대해서는
1. getter/setter메서드를 추가하거나.
2. geteer/setter 이외의 메서드를 사용해야 합니다.
"""