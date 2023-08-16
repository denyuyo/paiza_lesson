# randint関数を使用してランダムな目を出力

import random
dice = random.randint(1,6)
print("サイコロの目は" + str(dice) + "です。")

enemy = random.randint(50,99)
print("モンスターに、"+str(enemy)+"のダメージを与えた。")

# スライムの合計体重を出力

import random
number = random.randint(1, 10)
print("体重100キロのスライムが" + str(number) + "匹あらわれた")
weight = 100
print("スライムの合計体重は" + str(weight * number) + "キロです")
