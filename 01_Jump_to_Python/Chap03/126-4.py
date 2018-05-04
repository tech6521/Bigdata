# coding: cp949

coffee_number = 10
menu = 0
while True:

    while True:
        print("<Menu>")
        print("1. 커피구매\n2. 커피잔량 확인\n3. 프로그램 종료\n");
        menu = int(input("메뉴를 선택하세요: "))
        print("")
        break
     
        
    while menu==1:
        money = int(input("금액을 입력하세요: ")) 
    
        if money < 300:
            print("금액이 %d 모자랍니다." %(300-money))
            break
        elif money == 300:
            print("커피를 줍니다")
            coffee_number = coffee_number - 1
            break
        elif money >300:
            print("커피를 줍니다.\n 여기 거스름돈은 %d입니다." %(money-300))
            coffee_number = coffee_number - 1
            break
        else :
            print("돈을 다시 돌려주고 커피를 주지 않습니다")

            print("남은 커피의 양은 %d개 입니다.\n" %coffee_number)
            break

        if not coffee_number:
            print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
            break

    if menu==2:
        print("남은 커피의 양은 %d 입니다" %coffee_number)
    
    if menu==3:
        print("프로그램을 종료합니다")
        break


