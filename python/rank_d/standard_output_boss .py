# 整数を改行ありで 1,000 行出力

for i in range(1, 1001):
        print(i)
        
# 1,000 までの数値をすべて、半角スペース区切りで出力

for i in range(1, 1001):
        print(i, end=' ' if i < 1000 else '\n')