def multiply_three_numbers(*args):
    result = 1
    for i in args: 
        result = result * i 
    return print(result)

# 테스트 코드
multiply_three_numbers(7, 3, 5)
multiply_three_numbers(21, 4, 9)
multiply_three_numbers(-7, 6, 3)