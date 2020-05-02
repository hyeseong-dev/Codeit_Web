"""
현상태로는 __age에 접근 할 수 없어 나이를 알수 없고 수정도 불가능함.
즉, Citizen 클래스를 못씀.

이것에 대한 해결책은 변수에 접근할 수 있는 메소드를 별도로 만들어 준다.

캡슐화의 두 번째 정의 
객체의 속성과 그것을 사용하는 행동을 하나로 묶는것

즉, __age에 접근 가능한 메서드는 
1. can_drknk 메소드
2. get_age 메소드
3. set_age 메소드
라는 3개의 채널(메소드)들을 통해서만 접근하고 값을 가져오고 수정 할 수 있음.
"""
class Citizen:
    """ 주민 클래스 """
    drinking_age = 19 # 음주 가능 나이 

    def __init__(self, name, age, resident_id): 
        """이름, 나이, 주민등록번호 """
        self.name = name
        self.__age = age
        self.__resident_id = resident_id

    def authenticate(self, id_field):
        """ 본인이 맞는지 확인하는 메소드 """
        return self.__resident_id == id_field
    
    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드 """
        return self.__age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name+"씨는 " + str(self.__age) + "살입니다!"

    def get_age(self):
        """ 인스턴스 속성 __age, __resident_id를 외부에서 접근하여 가져오기 위해 만든 메서드"""
        return self.__age

    def set_age(self,age):
        """ 인스턴스 속성 __age, __resident_id를 외부에서 접근하여 수정하기 위해 만든 메서드"""
        self.__age = age


young = Citizen('Young Hoon Kang', 18, '87654321') 
print(young.get_age()) # 해당 객체의 값을 불러 올수 있다. 

young.set_age(20)
print(young.get_age())