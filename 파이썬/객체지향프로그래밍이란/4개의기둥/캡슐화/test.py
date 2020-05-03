# -*- encoding: utf-8 -*-
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

young = Citizen('홍길동',19,'12345678')

print(young._Citizen__age)