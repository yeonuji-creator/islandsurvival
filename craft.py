import game_text as g
import pygame

pygame.init()

inventory = {
        '물': 3,
        '고기' : 3,
        '목재' : 3,
        '돌' : 0,
        '풀' : 3,
        '가죽' : 0,
        '석영' : 0, 
        '아름다운결정' : 0,
        '레전드신기한꽃' : 0,
        '돈' : 0
    }

def craft(inventory):
    g.onebyone("제작을 시작합니다.")

    g.onebyone("제작 물건: 1. 나무 검(목재2), 2. 풀 갑옷(풀3)", "")

    g.onebyone("제작할 물건을 고르시오.", "")
    craft_some = input()

    if craft_some == "1":
        if inventory["목재"] >= 2:
            g.onebyone("나무 검을 제작했습니다.")
            inventory["목재"] -= 2

        else:
            g.onebyone("재료가 부족합니다.")

    elif craft_some == "2":
        if inventory["풀"] >= 3:
            g.onebyone("풀 갑옷을 제작했습니다.")
            inventory["풀"] -= 3

        else:
            g.onebyone("재료가 부족합니다.")


craft(inventory)

    
