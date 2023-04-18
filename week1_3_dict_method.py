## 딕셔너리 메서드

# 빈 딕셔너리 만들기
empty_joonyeol = {}
joonyeol = {"apple": 1, "banana":2, "orange":3}
print(joonyeol) # {'apple': 1, 'banana': 2, 'orange': 3}


# 딕셔너리 쌍 추가
joonyeol["grape"] = 4
print(joonyeol) # {'apple': 1, 'banana': 2, 'orange': 3, 'grape': 4}


# del : 딕셔너리에서 특정 요소를 삭제
joonyeol = {"apple": 1, "banana":2, "orange":3}
del joonyeol["apple"]
print(joonyeol) # {'banana': 2, 'orange': 3}


# 딕셔너리에서 특정 Key에 해당하는 Value를 얻는 방법 (딕셔너리에 Key가 없는 경우, KeyError)
joonyeol = {"apple": 1, "banana":2, "orange":3}
print(joonyeol["banana"]) # 2


# keys : 딕셔너리에서 모든 Key를 리스트로 만들기
joonyeol = {"apple": 1, "banana":2, "orange":3}
key_list = list(joonyeol.keys())
print(key_list) # ['apple', 'banana', 'orange']


# value : 딕셔너리에서 모든 Value를 리스트로 만들기
joonyeol = {"apple": 1, "banana":2, "orange":3}
value_list = list(joonyeol.values())
print(value_list) # [1, 2, 3]


# items : 딕셔너리의 모든키와 값을 튜플 형태의 리스트로 반환
joonyeol = {'name': 'joonyeol', 'age': 30, 'gender': 'male'}
items = joonyeol.items()
print(items) # joonyeol_items([('name', 'joonyeol'), ('age', 30), ('gender', 'male')])


# clear : 딕셔너리의 모든 요소를 삭제
joonyeol = {'name': 'joonyeol', 'age': 30, 'gender': 'male'}
joonyeol.clear()
print(joonyeol) # {}


# get : 딕셔너리에서 지정한 키에 대응하는 값을 반환 (딕셔너리에 Key가 없는 경우, None 반환)
joonyeol = {'name': 'joonyeol', 'age': 30, 'gender': 'male'}
name = joonyeol.get('name')
print(name) # joonyeol

email = joonyeol.get('email')
print(email) # None

# 기본값을 설정할 수 있음
email = joonyeol.get('email', 'unknown')
print(email) # unknown


# in : 해당 키가 딕셔너리 안에 있는지 확인
joonyeol = {'name': 'joonyeol', 'age': 30, 'gender': 'male'}
print('name' in joonyeol) # True
print('email' in joonyeol) # False
