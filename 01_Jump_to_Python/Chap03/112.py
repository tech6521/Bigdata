# coding: cp949
#money =1
#money =7
money = 0
if money:
    print("택시를 타고 가라")
#  print("도착했습니다") <- indentation 맞지 않아 에러
#    print("목적지에 도착했습니다")
else:
    print("걸어가라")
#  print("도착했습니다") <- indentation 맞지 않아 에러
#    print("도착했습니다") <- 동일한 코드가 중복이됨
                       # <-프로그램 수정시 동일 코드 로직변경이 누락될 가능성이 있습
print("목적지에 도착했습니다.") # <- 중복코드 제거
print("프로그램 종료합니다")

    
