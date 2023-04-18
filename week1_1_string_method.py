## string method

# count : 문자열 내에서 특정 문자가 몇 개나 있는지 셈
joonyeol = "Hellow, World"
count = joonyeol.count('l')
print(count) # 3


# find : 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아줌
# 없을 경우 -1 return
position = joonyeol.find("World")
print(position) # 8


# index : 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아줌
# 없을 경우 ValueError
try:
    position_2 = joonyeol.index("World")
    print(position_2) # 8
except ValueError:
    print("찾는 문자열이 없습니다.")


# join : 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 메서드
fruits = ["apple", "banana", "cherry"]
joined_fruits = ", ".join(fruits)
print(joined_fruits) # apple, banana, cherry


# upper : 문자열 내에서 모든 소문자를 대문자로 바꾸는 메서드
# lower : 문자열 내에서 모든 대문자를 소문자로 바꾸는 메서드
uppercate_joonyeol = joonyeol.upper()
print(uppercate_joonyeol) # HELLOW, WORLD

lowercate_joonyeol = joonyeol.lower()
print(lowercate_joonyeol) # hellow, world


# replace : 문자열 내에서 특정 문자열을 다른 문자열로 바꾸는 메서드
replaced_joonyeol = joonyeol.replace("World", "Python")
print(replaced_joonyeol) # Hellow, Python


# split : 문자열을 특정 문자를 기준으로 나누는 메서드(결과는 리스트 형태로 반환)
fruits_split = joined_fruits.split(", ")
print(fruits_split) # ['apple', 'banana', 'cherry']
