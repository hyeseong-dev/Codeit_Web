class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이 

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민번호"""
        self.name = name 
        self.__age = age 
        self.__resident_id = resident_id 
    
    # def __authenticate(self, id_field):
    #     ''' 본인이 맞는지 확인하는 메소드'''
    #     return self.__resident_id == id_field

    def authenticate(self, id_field):
        ''' 본인이 맞는지 확인하는 메소드'''
        return self.__resident_id == id_field
    
    def can_drink(self):
        '''음주 가능 나이인지 확인하는 메소드'''
        return self.__age >= Citizen.drinking_age

    def __str__(self):
        '''주민 정보를 문자열로 리턴하는 메소드'''
        return self.name + "씨는 " + str(self.__age) + '살입니다!'

kyusik = Citizen('최규식', 25,'123456')
# print(kyusik.__resident_id) # AttributeError: 'Citizen' object has no attribute '__resident_id 발생
# print(kyusik.__age)  # 바로 위와 동일한 오류 발생 

print(kyusik.authenticate('123456') ) # 메소드 없다고 에러남.