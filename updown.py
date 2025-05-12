import random

value = (random.randint(0,100))

while True:
    num = int(input("0-100 사이의 숫자를 입력하세요"))
    if value > num:
        print("up!")
    elif value < num:
        print("down!")
    else:
        print("정답입니다!")
        break

