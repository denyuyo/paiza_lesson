# list関数

# append関数　リストの末尾に要素を追加
team.append("戦士")

# リストの要素を上書き
team[0] = "ドラゴン"

# リストの要素を削除
team.pop(0)



#文字列をカンマで分割

team_str = "勇者,戦士,忍者,魔法使い"
print(team_str.split(","))

#英文の単語数を数える

str = "One cold rainy day when my father was a little boy he met an old alley cat on his street"

words = len(str.split())
print(words)