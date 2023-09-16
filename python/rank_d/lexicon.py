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

# 辞書の整列
weapons = {"ぎんがのつるぎ":182, "ハイパーノヴァ":131, "ときのおうしゃく":76}
print(sorted(weapons))
print(weapons)
print(sorted(weapons.items()))

# RPGアイテム一覧再現

# 画像用辞書
item_images = {
    "剣":"http://paiza.jp/learning/images/sword.png",
    "盾":"http://paiza.jp/learning/images/shield.png",
    "回復薬":"http://paiza.jp/learning/images/potion.png",
    "クリスタル":"http://paiza.jp/learning/images/crystal.png"
}
# アイテムの並び順配列
item_orders = ["クリスタル", "回復薬", "盾", "剣", "回復薬", "回復薬"]
# アイテム名を取り出す
for item_name in item_orders:
# 画像ファイル名を取り出す
    print("<img src='" + item_images[item_name] + "'>")
    print(item_name + "<br>")

# 画像用辞書(Lv.2)
items_images = {
    "剣": "http://paiza.jp/learning/images/sword.png",
    "盾": "http://paiza.jp/learning/images/shield.png",
    "回復薬": "http://paiza.jp/learning/images/potion.png",
    "クリスタル": "http://paiza.jp/learning/images/crystal.png"
}
# アイテム数を標準入力から取得
item_count = int(input())
# アイテム名を入力し、対応する画像を表示
for _ in range(item_count):
    item_name = input().rstrip()
    if item_name in items_images:
        print(f"<img src='{items_images[item_name]}'>")
