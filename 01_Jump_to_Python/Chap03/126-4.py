# coding: cp949

coffee_number = 10
menu = 0
while True:

    while True:
        print("<Menu>")
        print("1. Ŀ�Ǳ���\n2. Ŀ���ܷ� Ȯ��\n3. ���α׷� ����\n");
        menu = int(input("�޴��� �����ϼ���: "))
        print("")
        break
     
        
    while menu==1:
        money = int(input("�ݾ��� �Է��ϼ���: ")) 
    
        if money < 300:
            print("�ݾ��� %d ���ڶ��ϴ�." %(300-money))
            break
        elif money == 300:
            print("Ŀ�Ǹ� �ݴϴ�")
            coffee_number = coffee_number - 1
            break
        elif money >300:
            print("Ŀ�Ǹ� �ݴϴ�.\n ���� �Ž������� %d�Դϴ�." %(money-300))
            coffee_number = coffee_number - 1
            break
        else :
            print("���� �ٽ� �����ְ� Ŀ�Ǹ� ���� �ʽ��ϴ�")

            print("���� Ŀ���� ���� %d�� �Դϴ�.\n" %coffee_number)
            break

        if not coffee_number:
            print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.")
            break

    if menu==2:
        print("���� Ŀ���� ���� %d �Դϴ�" %coffee_number)
    
    if menu==3:
        print("���α׷��� �����մϴ�")
        break


