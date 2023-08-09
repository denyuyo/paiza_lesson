# push_back x : A の末尾に x を追加する
# pop_back : A の末尾を削除する
# print : A を半角スペース区切りで1行に出力する

N, Q = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(Q):
    query = input().split()
    
    if query[0] == '0':
        x = int(query[1])
        A.append(x)
    elif query[0] == '1':
        A.pop()
    elif query[0] == '2':
        print(*A)
