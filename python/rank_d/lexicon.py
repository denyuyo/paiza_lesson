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