class User:
    count = 0 

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw 

        User.count += 1 # 클래스 변수로 취급되어 인스턴스 만들때마다 count변수값이 1씩 증가
    
user1 = User('강영훈', 'younghoon@codeit.kr', '123456')
user2 = User('이윤수', 'yoonsoo@codeit.kr', '3232324')
user3 = User('서혜린', 'haelin@codeit.kr', '5545454')
user4 = User('서혜린', 'haelin@codeit.kr', '5545454')
user4 = User('서혜린', 'haelin@codeit.kr', '5545454')

print(User.count)
