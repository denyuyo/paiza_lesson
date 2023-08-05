# sがpaizaと一致する場合はYESを、一致しない場合はNOを出力

def check_paiza(s):
    if s == "paiza":
        return "YES"
    else:
        return "NO"

input_string = input()
result = check_paiza(input_string)
print(result)

# Nが 100 以下の場合はYESを、そうではない場合はNOを出力

N = int(input())

if N <= 100:
    print("YES") 
else: 
    print("NO")


# 式 A × B ≦ C が成立している場合はYESを、そうではない場合はNOを出力

A, B, C = map(int, input().split())

if A * B <= C:
    print("YES")
else:
    print("NO")

# ある占いでは、箱の中に 1~9 までのいずれかの数字が書かれている玉を取り出し、その玉に書かれている数字から運勢を占う。玉に書かれている数字が 7 の時は大吉となる。占いで取り出した玉に書かれている数字が 1 つ与えられる。大吉かどうかを判定せよ

n = int(input())

if n == 7:
    print("Yes")
else:
    print("No")