i = 1 
n=120
list1 = []
while i <=120:
    if n%i == 0:
        list1.append(i)
    i+=1
print(*list1,sep='\n')
print(f'{n}의 약수는 총 {len(list1)}개입니다.')


