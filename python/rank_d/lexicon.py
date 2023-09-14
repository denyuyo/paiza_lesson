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

# リストの整列
weapons = ["ぎんがのつるぎ", "ハイパーノヴァ", "ケイオスブレード", "ときのおうしゃく"]
print(weapons)

print(sorted(weapons))
print(sorted(weapons, reverse=True))

weapons2 = ["4.ぎんがのつるぎ", "1.ハイパーノヴァ", "1.ケイオスブレード", "2.ときのおうしゃく"]
print(sorted(weapons2))

weapons3 = ["精霊王のタクト", "神鳥の杖", "ランタンステッキ", "聖竜のえんげつとう"]
print(sorted(weapons3))

# ソート演習

apples = [310, 322, 292, 288, 300, 346]
print(sorted(apples))               # 昇順
print(sorted(apples, reverse=True)) # 逆順
# アルファベット順
words = ["pumpkin", "orange", "apple", "carrot", "onion"]
print(sorted(words))