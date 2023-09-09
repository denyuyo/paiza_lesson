# list関数

# append関数　リストの末尾に要素を追加
team.append("戦士")

# リストの要素を上書き
team[0] = "ドラゴン"

# リストの要素を削除
team.pop(0)



#文字列をカンマ分割

team_str = "勇者,戦士,忍者,魔法使い"
print(team_str.split(","))

#英文の単語数

str = "One cold rainy day when my father was a little boy he met an old alley cat on his street"

words = len(str.split())
print(words)

# 標準入力から読み込んだURLを分割
# https://paiza.jp/cgc/users/ready

url_str = input().rstrip()
print(url_str.split("/"))

# 読み込んだ複数行を出力する

import sys
for line in sys.stdin.readlines():
    msg = line.rstrip()
    print(msg + "が現れた")

# 複数行のカンマ区切りデータを出力する

import sys

for line in sys.stdin.readlines():

    data = line.strip().split(',')

    enemy_name = data[0]
    enemy_count = data[1]

    output = f"{enemy_name}が{enemy_count}匹現れた"
    print(output)

# じゃんけんプログラム

import random
# 標準入力から1行取得
line = input().rstrip()

# カンマで分割して、リストに代入
janken = line.split(",")

# リストの要素数を変数に代入
num = len(janken)

# リストの中身を出力
print(janken)

# ランダムに選んだリストの要素を出力
print(janken[random.randrange(num)])
