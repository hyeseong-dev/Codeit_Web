# 화씨 온도에서 섭씨 온도로 바꿔주는 함수 
def f_2_c(fhr):
    return round((fhr - 32)*5 / 9,2)

sam_tem_li = [40,15,32,64,-4,11] 
print('화씨 온도 리스트: ' + str(sam_tem_li))

i = 0 
while i<len(sam_tem_li):
    sam_tem_li[i] = f_2_c(sam_tem_li[i])
    i+=1
print('섭씨 온도 리스트'+str(sam_tem_li))

