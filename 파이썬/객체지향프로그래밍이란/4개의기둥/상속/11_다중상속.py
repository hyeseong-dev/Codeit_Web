# -*- encoding: utf8 -*-
'''
엔지니어이면서 테니스선수인 클래스를 만들어보자.

super()를 썻을때 어느 부모 클래스를 가져오는지 알 수 없음.
'''

class Engineer: 
    
    def __init__(self, favorite_language):
        self.favorite_language = favorite_language

    def program(self):
        print(f'{self.favorite_language}(으)로 프로그래밍합니다.')
    

class TennisPlayer:
    def __init__(self, tennis_level):
        self.tennis_level = tennis_level
    
    def play_tennis(self):
        print(f'{self.tennis_level} 반에서 테니스를 칩니다.')



class EngineerTennisPlayer(Engineer,TennisPlayer): # 더 추가하고 싶으면  콤마 넣고, 클래스명 적기!

    def __init__(self, favorite_language, tennis_level):
        Engineer.__init__(self,favorite_language)
        TennisPlayer.__init__(self,tennis_level)

# 다중 상속을 받는 클래스의 인스턴스 생성
younghoon = EngineerTennisPlayer('파이썬','초급')

# 두 부모 클래스의 메소드들을 상속 받았는지 확인 
younghoon.program()
younghoon.program()