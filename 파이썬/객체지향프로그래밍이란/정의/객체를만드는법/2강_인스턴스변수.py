class User:
    pass

user1 = User()
user2 = User()
user3 = User()

user1.name = '김대위'
user1.email = 'captain@codeit.kr'
user1.password = '12345'

user1.name = '강영훈'
user1.email = 'younghoon@codeit.kr'
user1.password = '5678'

user1.name = '최지웅'
user1.email = 'jiwoong@codeit.kr'
user1.password = '!@#dd'

print(user1.email)
print(user2.email)

# 인스턴스 변수를 사용하려면 꼭! 그전에 정의해야한다. 
# print(user3.age) # <--age라는 인스턴스 변수를 정의하지 않았음.