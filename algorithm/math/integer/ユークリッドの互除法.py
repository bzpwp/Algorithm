# 最大公約数
import math
x,y = map(int,input().split())
math.gcd(x, y)

# ユークリッドの互除法
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

# 拡張ユークリッドの互除法

def extgcd(a, b):
    d = a
    if b != 0:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
    else:
        x = 1
        y = 0
    return d, x, y

# ax + by = 1

# 入力
a, b = map(int,input().split())

# 拡張ユークリッドの互除法
def extgcd(a, b):
    d = a
    if b != 0:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
    else:
        x = 1
        y = 0
    return d, x, y

d, x, y = extgcd(a, b) # d = GCD

print(d,x,y)



import math

def ans(a,b,c,d): #c,dは初項
    # c + a*x = d + b*yが成り立つ一般項     # 7 + 14*x = 11 + 22*y
    # a*x - b*y = d - c    # 14*x - 22*y = 4
    e, x1, y1 = extgcd(a, b)
    print(e, x1, y1)
    # a*x1 + b*y1 = e               # 14*(-3) + 22*2 = 2
    # (a/e)*x1 + (b/e)*y1 = 1       # 7*(-3) + 11*2 = 1
    # (a/e)*x - (b/e)*y = (d - c)/e     # 7*x - 11*y = 2
    if (d - c)%e != 0 or ((d - c) != 0 and ((d - c)//e != -1 and (d - c)//e != 1)):
        return False, 0, 0 #解無し
    elif (d - c)//e == 1: #(a/e)*x - (b/e)*y = 1
        #(a/e)(x-x1)=(b/e)(y+y1)    # 3(x-0) = 5(y+(-1))
        #(y+y1) = (a/e)*X   # ((y+(-1)) = 3*X 
        # y = (a/e)*X - y1  # y = 3*X - (-1)
        # d + b*yに代入     # 5 + 10*yに代入
        # d + b*((a/e)*X - y1) #一般項     # 5 + 10*(3*X - (-1))
        # = (a*b)/e * X + d - b*y1
        # max(c, d)以上の最小の項 = 一般項の初項
        # (a*b)/e * X + d - b*y1 >= max(c, d)となる最小のX
        # X >= (max(c, d) - d + b*y1)/((a*b)/e)
        X = math.ceil((max(c, d) - d + b*y1)/((a*b)/e))
        return True, int(d + b*((a/e)*X - y1)), int((a*b)/e) #初項、増分

    elif (d - c)//e == -1: #(a/e)*x - (b/e)*y = 1
            #(a/e)(x+x1)=(b/e)(y-y1)    # 1(x+0) = 1(y-1)
            #(y-y1) = (a/e)*X   # y-1 = X 
            # y = (a/e)*X + y1  # y = X - (-1)
            # d + b*yに代入     # 3 + 6*yに代入
            # d + b*((a/e)*X + y1) #一般項     # 3 + 6*(X - (-1))
            # = (a*b)/e * X + d + b*y1
            # max(c, d)以上の最小の項 = 一般項の初項
            # (a*b)/e * X + d + b*y1 >= max(c, d)となる最小のX
            # X >= (max(c, d) - d - b*y1)/((a*b)/e)
            X = math.ceil((max(c, d) - d - b*y1)/((a*b)/e))
            return True, int(d + b*((a/e)*X + y1)), int((a*b)/e) #初項、増分
    elif (d - c) == 0:
            # (a/e)*x = (b/e)*y     # 3*x = 2*y
            # y = (a/e)*X           # y = 3*X
            # d + b*yに代入         # 3 + 4*yに代入
            # d + b*((a/e)*X) #一般項   # 3 + 4*(3*X)
            # max(c, d)以上の最小の項 = 一般項の初項
            # d + b*((a/e)*X) >= max(c, d)となる最小のX
            # X >= (max(c, d) - d)/((a*b)/e)
            X = math.ceil(max(c, d) - d)/((a*b)/e)
            return True, int(d + b*((a/e)*X)), int((a*b)/e) #初項、増分

x,y= ans(6,10,3,5)
print(x,y)

    
