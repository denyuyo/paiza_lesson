# 2 つの文字列 S, T が入力される。S, T を改行区切りで出力

S = input()
T = input()
print(S)
print(T)

# 整数 A, B が与えられる  。A と B の差 D と積 P を半角スペース区切りで出力

a, b = map(int, input().split())
print(a - b, a * b)


# 整数 A, B, C が与えられる。以下のアルゴリズムを実行

#   変数 N を 0 で初期化する
#   N に A を足した値を N へ代入する
#   N に B をかけた値を N へ代入する
#   N を C で割ったあまりを N へ代入する
#   N を出力する

N = 0

A, B, C = map(int, input().split())

N += A
N *= B
N %= C

print(N)

# ある電車に a 人が乗っている。駅に到着した時に b 人が降りて新たに c 人が乗車する時、電車に乗っている乗客人数を求めよ

a, b, c = map(int, input().split())
print(a - b + c)
