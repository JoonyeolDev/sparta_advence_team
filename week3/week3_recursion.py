# dfs bfs 찾아보기

# # 재귀함수
# def recursion(n):
#     print(n)
#     recursion(n+1)
# recursion(1)
# #RecursionError: maximum recursion depth exceeded while calling a Python object

# import sys
# print(sys.getrecursionlimit())

# 팩토리얼
def factorial(n):
    if n<=0: return 1
    return n*factorial(n-1)

print(factorial(16)) # 20922789888000

# 피보나치
def fibonacci(a,b,n,count=2):
    if count == n: return b
    return fibonacci(b,a+b,n,count+1)

print(fibonacci(0,1,12))

# 파스칼
def pascal(n, a=[1]):
    if len(a)==n: return a
    return pascal(n, [1]+[a[i-1]+a[i] for i in range(1,len(a))]+[1])

for i in range(1,8):
    print(pascal(i))

