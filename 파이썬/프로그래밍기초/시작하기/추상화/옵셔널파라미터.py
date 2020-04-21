# 옵셔널 파라미터란, 함수의 인자값에 기본값을 주는것을 말합니다. 
# 파라미터의 기본값을 설정해두면 함수 호출을 할 때 파라미터에 해당되는 값을 넘겨주지 않았을 경우, 그 파라미터는 기본값을 갖게 됩니다. 이런 파라미터를 optional parameter라고 부릅니다. 아래의 코드에서 마지막 파라미터를 써주지 않으면 nationality는 "한국"의 값을 갖게 되는거죠.
def myself(name, age, nationality = "한국"):
    print("내 이름은 %s" % name)
    print("나이는 %d살" % age)
    print("국적은 %s" % nationality)

myself("코드잇", 1)            # 기본값이 설정된 파라미터를 바꾸지 않을 때
print()
myself("코드잇", 1, "미국")     # 기본값이 설정된 파라미터를 바꾸었을 때

"""
Optional parameter는 모두 마지막에 있어야 합니다. 아래와 같이 마지막이 아닌 경우에는 말이 안 되죠?
"""

# def myself(name, nationality = "한국", age):
#     print("내 이름은 %s" % name)
#     print("나이는 %d살" % age)
#     print("국적은 %s" % nationality)

# myself("코드잇", 1)            # 기본값이 설정된 파라미터를 바꾸지 않을 때
# myself("코드잇", "미국", 1)     # 기본값이 설정된 파라미터를 바꾸었을 때