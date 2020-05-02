# 이전 영상에서 혹시 이상한점을 느끼셨나요? 변수 age, resident_id나 메소드 authenticate의 이름 앞에 밑줄두 개(__)를 추가하니 클래스 외부에서 접근할 수 없었습니다. 그런데 비슷한 모양의 __init__apthemdhk __str__메소드는 잘 사용할 수 있습니다. 코드로 살펴봅시다. 

class Citizen:
    """ 주민 클래스 """
    drinking_age = 19 # 음주 가능 나이 

    def __init__(self, name, age, resident_id): 
        """이름, 나이, 주민등록번호 """
        self.name = name
        self.__age = age
        self.__resident_id = resident_id

    def __authenticate__(self, id_field):
        """ 본인이 맞는지 확인하는 메소드 """
        return self.__resident_id == id_field
    
    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드 """
        return self.__age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name+"씨는 " + str(self.__age) + "살입니다!"



# Citizen 인스턴스 생성
young = Citizen('Young Hoon Kang', 18, '87654321') # 
print(young.__str__()) # 출력 Young Hoon Kang씨는 18살입니다. 
print(young.__authenticate__('87654321')) # 에러 발생!!!!

""" 
이 코드의 마지막 부분에서 __str__ 메소드는 잘 실행 되지만, __authenticate메소드는 에러가 발생합니다. 왜요?

파이썬에서는 변수나 메소드 이름 앞에 밑줄 __개가 있더라도 이름 뒤에도 밑줄 2개 __가 있으면 일반 변수나 메소드처럼 클래스 밖에서라도 접근 할 수 있습니다. 메소드 이름 앞 뒤에 밑줄 2개가 있으면 파이썬이 정한 특수한 상황에서 자동으로 실행되는 '특수 메소드'를 나타낸다고 배웠습니다. 이렇게 특수 메서드를 나타내기 위한 표시인데 앞에 밑줄 달랑 2개가 있다라는 이유로 접근한다면 문제가 있겠지!?

정리하면, 


1. __str__ 메소드는 이름 앞 뒤에 모두 밑줄 2개가 있기 때문에 일반 메소드와 동일하게 사용할 수 있고, 
2. 인스턴스 변수 __resident_id는 앞에만 밑줄 __개가 있어서 외부에서 접근 할 수 없는 겁니다. 
__resident_id__로 바뀌면 일반 변수처럼 사용 가능합니다. 

"""

# class Citizen:
#     """주민 클래스"""
#     drinking_age = 19 # 음주 가능 나이

#     def __init__(self, name, age, resident_id):
#         """이름, 나이, 주민등록번호"""
#         self.name = name
#         self.__age = age
#         self.__resident_id__ = resident_id

#     def authenticate(self, id_field):
#         """본인이 맞는지 확인하는 메소드"""
#         return self.__resident_id__ == id_field

#     def can_drink(self):
#         """음주 가능 나이인지 확인하는 메소드"""
#         return self.__age >= Citizen.drinking_age

#     def __str__(self):
#         """주민 정보를 문자열로 리턴하는 메소드"""
#         return self.name + "씨는 " + str(self.__age) + "살입니다!"

# # 주민 인스턴스 생성
# young = Citizen("younghoon kang", 18, "87654321")

# print(young.__str__()) # 출력: younghoon kang씨는 18살입니다!
# print(young.__resident_id__)) # 출력: "87654321"
# print(young.__authenticate("87654321")) # 에러가 난다!!!

