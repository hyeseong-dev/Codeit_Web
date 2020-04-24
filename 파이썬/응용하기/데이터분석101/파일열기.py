from random import randint

f = open('C:/Users/hyese/OneDrive/바탕 화면/main/Codeit_Web/파이썬/응용하기/chicken.txt','r', encoding='utf-8')
lines = f.readlines()
for i in lines:
    print(i)
f.close()
