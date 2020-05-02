"""
실습과제
이전에 작성했던 User 클래스를 문서화해봅시다. 문서화 결과에는 아래의 내용이 포함되어야 합니다.


1 User 클래스: SNS의 유저를 나타내는 클래스
2 __init__ 메소드: 이름, 이메일, 비밀번호를 인스턴스 변수로 갖고, 인스턴스가 생성될 때마다 클래스 변수 count를 1씩 증가시킨다
3 say_hello 메소드: 유저의 이름을 포함한 인사 메시지를 출력한다
4 __str__ 메소드: 유저 정보를 정의된 문자열 형태로 리턴한다
5 number_of_users 메소드: 총 유저 수를 출력하는 클래스 메소드
"""

class User:
    """ SNS의 유저를 나타내는 클래스"""
    user_num = 0

    def __init__(self,name,email,pasword):
     """이름, 이메일, 비밀번호를 인스턴스 변수로 소유 """
        self.name = name
        self.email = email
        self.pasword = pasword

        User.user_num +=1

    def say_hello(self):
     """유저의 이름을 포한한 인사 메시지를 출력 """
        print( f'Hello! {self.name}')
    
    def __str__(self):
    """ 유저 정보를 정의된 문자열 형태로 리턴"""
        return f'유저: {self.name}, 이메일: {self.email}, 비밀번호: *****'
    
    @classmethod
    def number_of_users(cls):    
     """총 유저수를 출력하는 메소드 """
        print(f'총 유저수" {cls.user_num}')
help(User)