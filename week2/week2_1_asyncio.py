# list = [1,3,4,2]
# list.reverse()
# list+=[1,2,3,4]
# list.insert(4,10)
# print(list)

# dic = {'a':1,'b':2,'c':3}
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# ===========================================
def my_coroutine_joon():
    while True:
        value = yield
        print('Received value : ',value)

# 코루틴 객체 생성
co = my_coroutine_joon()

# 코루틴 실행 준비
next(co)

# 값을 보내기
co.send("Hello, world")

def my_generator():
    yield 1
    yield 2
    yield 3

# 같은 함수를 실행하지만 결과가 다름
gen = my_generator()
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3

def my_coroutine_yeol():
    while True:
        x = yield
        print('Received:', x)

co = my_coroutine_yeol()
next(co)

co.send(10) # Received: 10
co.send(20) # Received: 20
co.send(30) # Received: 30

phone_book = {'joon':'123-3214', 'yeol':'321-1231', 'yoon':'456-9877'}

def search():
    name = yield
    while True:
        if name in phone_book:
            phone_number = phone_book[name]
        else:
            phone_number = 'Cannot find the name in the phone book.'
        name = yield phone_number

# 코루틴 객체 생성
search_coroutine = search()
next(search_coroutine)

# 검색 예시
result = search_coroutine.send('joon')
print(result)

result = search_coroutine.send('yeol')
print(result)

result = search_coroutine.send('yoon')
print(result)

import asyncio
import random

async def fetch_data():
    print("데이터를 가져오는 중...")
    await asyncio.sleep(1) # 데이터를 가져오는데 1초가 걸린다고 가정
    return random.randint(1, 100)

async def main():
    data = await fetch_data()
    print(f"가져온 데이터: {data}")

asyncio.run(main())

