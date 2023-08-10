# 10 個の文字列 S_1, S_2, S_3, ...を改行区切りで出力

s_list = input().split() 
for s in s_list:
    print(s)

# 1,000 行以内の出力

N = int(input())

for i in range(1, N + 1):  # 1からNまでの数値を順番に処理
    print(i)
