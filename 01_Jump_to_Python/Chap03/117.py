# coding: cp949
#money = 2000
money =int(input("얼마를 가지고 있습니까? ")) # input값으로 받는것은 무조건 string으로 처리
#card = 1 <- 카드 소지 여부만 판단하므로 정수형은 메모리 공간을 낭비함
#card = True
card = input("카드를 소유하고있습니까? (y/n) :")
if card == 'y':
    card = True
else:
    card = False

if money > 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
