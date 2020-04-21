def calculate_change(payment, cost):
    change = payment - cost # 거스름돈 총액
    
    
    fifty_thousand = change//50_000   #5만원 지폐
    ten_thousand = (change % 50_000) //10_000      #1만원 지폐
    five_thousand = (change % 10_000)//5_000 # 5천원 지폐
    one_thousand =  (change % 5_000)//1_000 # 1천원 지폐
    
    print('50000원 지폐: {}장'.format(fifty_thousand))
    print('10000원 지폐: {}장'.format(ten_thousand))
    print('5000원 지폐: {}장'.format(five_thousand))
    print('1000원 지폐: {}장'.format(one_thousand))


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

