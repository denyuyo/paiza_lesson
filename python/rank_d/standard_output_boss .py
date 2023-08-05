# 整数を改行ありで 1,000 行出力

for i in range(1, 1001):
        print(i)
        
# 1,000 までの数値をすべて、半角スペース区切りで出力

for i in range(1, 1001):
        print(i, end=' ' if i < 1000 else '\n')

# ゼロ・プラス・マイナスを繰り返し判定する

n = int(input())
print(n)

for i in range(n):
        num = int(input())
if num == 0:
        print(f"{num}は0")
elif num > 0:
        print(f"{num}はプラス")
else:
        print(f"{num}はマイナス")