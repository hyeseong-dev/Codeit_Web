def while_practice():
    i = 100
    while True:
        if i % 23 == 0:
            print(i)
            break
        i +=1
# 코드를 입력하세요.
while_practice()

print()

def while_practice2():
    i = 100 
    while i%23 != 0:  # 이 부분이 알짜배기니깐 잘봐~! while문의 조건식을 저렇게도 쓸수 있는거야~!
        i+=1
    print(i)

while_practice2()