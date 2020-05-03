"""
set_age() 메서드에 음수를 넣으면 self.__age가 음수가 되버린다. 
이런일을 막아야함. 그럼 방법은?
"""
class Citizen:
    drinking_age = 19
    def __init__(self, name, age, resident_id): 
        """이름, 나이, 주민등록번호 """
        self.name = name
        self.set_age(age) # init 메서드가 실행되면 나이가 음수가 되는걸 막아버림.
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

    def set_age(self,value): # setter 메서드
        """ 인스턴스 속성 __age, __resident_id를 외부에서 접근하여 수정하기 위해 만든 메서드"""
        if value < 0: 
            print('나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.')
            self.__age = 0
        else: 
            self.__age = value

young = Citizen('김경록',-199,'123456')
# print(young.get_age())
young.set_age(-10)
print(young.get_age())

young.set_age(19)
print(young.get_age())