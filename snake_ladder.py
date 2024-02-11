def to_print(a):
    for i in a:
        print(i)


def snake(num):

   if num == 17:
       print("YOU ARE AT 7 NOW!")
       return 7
   elif num == 54:
       print("YOU ARE AT 34 NOW!")
       return 34
   elif num == 64:
       print("YOU ARE AT 60 NOW!")
       return 60
   elif num == 62:
       print("YOU ARE AT 19 NOW!")
       return 19
   elif num== 87:
       print("YOU ARE AT 36 NOW!")
       return 36
   elif num== 93:
       print("YOU ARE AT 73 NOW!")
       return 73
   elif num == 95:
       print("YOU ARE AT 75 NOW!")
       return 75
   elif num == 98:
       print("YOU ARE AT 79 NOW!")
       return 79


def ladder(num):
    if num == 1:
        print("YOU ARE AT 38 NOW!")
        return 38
    elif num == 4:
        print("YOU ARE AT 14 NOW!")
        return 14
    elif num == 9:
        print("YOU ARE AT 31 NOW!")
        return 31

    elif num == 28:
        print("YOU ARE AT 84 NOW!")
        return 84

    elif num == 21:
        print("YOU ARE AT 42 NOW!")
        return 42
    elif num == 51:
        print("YOU ARE AT 67 NOW!")
        return 67
    elif num == 72:
        print("YOU ARE AT 91 NOW!")
        return 91
    elif num == 80:
        print("YOU ARE AT 99 NOW!")
        return 99



array = []
counter = 1
for i in range(10):
    row=[]
    for j in range(10):
        row.append(counter)
        counter = counter+1
    array.append(row)

to_print(array)


def is_snake(num):
    if num in [17,54,62,64,87,93,95,98]:
        return True
    return False

def is_ladder(num):
    if num in [1,4,9,21,28,51,72,80]:
        return True
    return False

def check_win(num):
    if num == 100:
        return True

    else:
        return False

def re_enter(player):
    print(player,"Your turn")
    a = int(input("Enter dice value"))
    if a<=6:
        return a
    else:
        re_enter(player)
def play_game(pointer1,pointer2):
    while True:

        a=int(input("Player 1 enter dice value"))
        if (a<=6):
            pointer1+=a
            if (pointer1 <= 100):
                if (check_win(pointer1)):
                    print("Player 1  won")
                    break
                if is_snake(pointer1) :
                    pointer1=snake(pointer1)
                elif is_ladder(pointer1):
                    pointer1 =ladder(pointer1)

            else:
                print("The value remains same(>100)")
                pointer1=pointer1-a

            print("Player1: You are at", pointer1)

        else:
            print("Dice value cannot exceed 6")
            re_enter("Player1")


        b = int(input("Player 2 enter dice value"))

        if (b <= 6):
            pointer2 += b
            if (pointer2 <= 100):
                if (check_win(pointer2)):
                   print("Player 2  won")
                   break
                if is_snake(pointer2) :
                   pointer2=snake(pointer2)
                elif is_ladder(pointer2):
                   pointer2 =ladder(pointer2)

                print("Player2: You are at", pointer2)

            else:
                print("The value remains same(>100)")
                pointer2 = pointer2 - b

        else:
            print("The Dice value cannot exceed 6")
            re_enter("Player2")

play_game(0,0)

