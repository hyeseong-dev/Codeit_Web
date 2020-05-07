class Citizen:
    """ 주민 클래스 """
    drinking_age = 19 # 음주 가능 나이 
"""
지금까지 우리는 __age의 getter메서드와 setter메서드를 만든것. 

그런데 왜?? __resident_id는 주민번호이므로 매우 민감한 정보이다. 
그러므로 외부에서 해당 객체의 속성을 읽고 수정할 수 있는 getter,setter메서드를 만들지 않은 이유이다.

오해 하지마세요~
authenticate() 메서드의 return self.__resident_id == id_field는 
__resident_id의 정보를 조회하거나 수정하는것이 아닌 id_filed 변수의 값과 비교해서 동일한지 아닌지 참, 거짓을 확인하는 것일 뿐임.
"""
class Citizen:

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

    def get_age(self): # getter 메서드
        """ 인스턴스 속성 __age, __resident_id를 외부에서 접근하여 가져오기 위해 만든 메서드"""
        return self.__age

    def set_age(self,age): # setter 메서드
        """ 인스턴스 속성 __age, __resident_id를 외부에서 접근하여 수정하기 위해 만든 메서드"""
        self.__age = age

"""
캡슐화 정리 

1. 클래스 밖에서 접근 못하게 할 변수, 메소드 정하기
2. 변수나 메소드 이름 앞에 언더바 2개 붙이기
3. 변수에 간접 접근할 수 있게 메소드 추가하기 -> getter/setter or 다른 용도의 메서드


"""