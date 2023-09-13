# 辞書

skills = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}

print(skills)
# キーワード索引
level = "職業"
print(skills[level])

# 辞書要素追加

skills = {"職業":"戦士", "体力":100, "魔法力":200, "ゴールド":380}
# 長さ
print(len(skills))
# データ追加
skills["属性"] = "炎"
# 更新
skills["職業"] = "魔法使い"
# 削除
del skills["体力"]
print(skills)

# ループ処理

# 辞書のおさらい
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(enemies["中ボス"])

for rank in enemies:
    print(enemies[rank] + "が、あらわれた！")
for (rank, enemy) in enemies.items():
    print(rank + "の" + enemy + "が、あらわれた！")

# ループ合計計算

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0

for score in points.values():
    sum += score

print(sum)