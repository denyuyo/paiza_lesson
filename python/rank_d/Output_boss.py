# 10 個の文字列 S_1, S_2, S_3, ...を改行区切りで出力

s_list = input().split() 
for s in s_list:
    print(s)

# 1,000 行以内の出力

N = int(input())

for i in range(1, N + 1):
    print(i)

# 文字列one two three four fiveを半角スペースで出力

input_str = "one two three four five" 
words = input_str.split()  # 文字列を半角スペースで区切ってリストに格納

for word in words:
    print(word)

# 大きな数値を 3 けたごとにカンマ区切りで出力

n = int(input())

n_str = str(n)
reversed_n_str = n_str[::-1]

formatted_n_str = ",".join(reversed_n_str[i:i+3] for i in range(0, len(reversed_n_str), 3))

final_result = formatted_n_str[::-1]

print(final_result)

# 文字列と整数の組からの選択 

N = int(input())

data = []
for _ in range(N):
    s, a = input().split()
    data.append((s, int(a)))

print(f"{data[7][0]} {data[7][1]}")

# 行ごとに要素数の異なる整数列の入力

N = int(input()) 

matrix = [] 

for _ in range(N):
    row = list(map(int, input().split()[1:]))
    matrix.append(row)

for row in matrix:
    print(" ".join(map(str, row)))