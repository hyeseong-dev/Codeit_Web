f = open('C:/Users/hyese/OneDrive/바탕 화면/main/Codeit_Web/파이썬/응용하기/chicken.txt',encoding='utf-8')

sum_ = 0
days = 0

for line in f:
    data = line.strip().split(': ')
    amount = int(data[1])
    sum_ += amount
    days += 1
print(f'월간 평균 판매액: {int(sum_/days)}원')