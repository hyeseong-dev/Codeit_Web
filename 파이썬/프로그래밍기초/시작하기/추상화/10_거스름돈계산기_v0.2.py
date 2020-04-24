# 바로 이렇게 직관적으로 코딩이 가능하면 중급 초의 실력!

def calculate_change(payment, cost):
    money_list = [50000, 10000, 5000, 1000]

    change = payment - cost
    money_count_list = []
    for money in money_list:
        money_count = change // money
        money_count_list.append(money_count)
        change %= money

    for idx in range(len(money_list)):
        print("%d원 지폐: %d장" % (money_list[idx], money_count_list[idx]))

# 테스트
calculate_change(100000, 33000)
print()
# calculate_change(500000, 378000)
