# # 풀이 방법 1
# i = 1
# while i<=100:
#     if i%8==0 and i%12 !=0: print(i)
#     i+=1

# 풀이방법 2
i = 1
while 1:
    if i%8==0 and i%12 !=0:
        print(i)
    elif i > 100:
        break
    else:
        pass
    i+=1

