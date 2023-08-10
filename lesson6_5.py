import random

min = 1
max = 10
target = random.randint(1, 10)
count = 0

def playGame():
    while True:
        global count, min, max, target
        keyin = int(input(f"猜數字的範圍{min} ~ {max}"))
        count += 1
        if keyin < min or keyin > 10:
            print("超出範圍")
        else:
            if keyin == target:
                print(f"猜對了！答案是{target}")
                print(f"你總共猜了{count}次")
                break
            else:
                print("猜錯了")
                if keyin < target:
                    print("再大")
                else:
                    print("再小")

    print("遊戲結束")



print("-----猜數字遊戲-----")
judge = True
while judge:
    playGame()

    confirm = input("是否再玩一次？(y/n)")
    if confirm == "n":
        judge = False
    elif confirm == "y":
        continue