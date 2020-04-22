# 실습과제
# 10보다 작은 2 또는 3의 배수는 2, 3, 4, 6, 8, 9이며, 이들의 합은 32입니다.


# while문과 if문을 활용하여, 1000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써보세요.


# 333167

# <주의> 문제에 해당하는 정답만 출력하셔야 합니다.  

# <주의> 자동 채점 과제이기 때문에, 문제의 조건에 정확히 따라주시기 바랍니다.
# i = 1
# result = 0
# for i in range(1,1000):
#     if i%2 == 0 or i%3 == 0:
#         result += i
# print(result)

# result,i = 1,1
# while i < 1000: 
#     if i%2 == 0 or i%3 == 0:
#         result += i
#     i+=1
# print(result)

# 다른 풀이 방법
# print(sum([i for i in range(1,1000) if i%2 == 0 or i%3 == 0]))



# result2 = list(map(lambda a : a if a%2 == 0 or a%3==0 else continue , a))  
# print(sum(result2))
