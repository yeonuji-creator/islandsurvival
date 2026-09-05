import random, time
import game_text as g
import pygame

pygame.init()

# 나중에 지우기
inventory = {
        '물': 3,
        '고기' : 3,
        '목재' : 3,
        '돌' : 0,
        '풀' : 0,
        '가죽' : 0,
        '석영' : 0, 
        '아름다운결정' : 0,
        '레전드신기한꽃' : 0,
        '돈' : 0
    }

def sell(inventory):

    trader = random.choice(["빡빡이주민", "친절한말랑말랑괴물", "살아있는쵸코칩쿠키", "항상웃고있는핸드폰"])

    g.onebyone(f"당신은 {trader}을(를) 만났습니다!")

    g.onebyone(f"당신의 인벤토리: {inventory}")

    if trader == "빡빡이주민":
        g.onebyone('빡빡이주민: 안녕하세요!!! 저한테 물건을 팔면 돈을 드리겠습니다.')
        g.onebyone("팔 물건을 고르세요: ", "")
        sell_some = input()
        if inventory[sell_some] > 0:
            g.onebyone("팔 개수를 고르세요.", "")
            sell_num = int(input())

            if sell_num <= inventory[sell_some]:
                g.onebyone(f"당신은 {sell_some}을(를) 팔았습니다.")
                inventory[sell_some] -= sell_num

            else:
                g.onebyone("아 뭐야!!! 없잖아!!!")
        


sell(inventory)
