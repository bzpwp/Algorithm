t = int(input())



def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

for i in range(t):
    n = int(input())
    x, y = factorization(n)
    if x[1] == 1:
        print(y[0],x[0])
    else:
        print(x[0],y[0])
