## list method

# len : 리스트의 길이를 반환하는 함수
joonyeol = [1, 2, 3, 4, 5]
print(len(joonyeol)) # 5


# del : 리스트에서 특정 인덱스를 삭제하는 연산자
del joonyeol[2]
print(joonyeol) # [1, 2, 4, 5]


# append : 리스트의 맨 뒤에 새로운 요소를 추가하는 메서드
joonyeol = [1, 2, 3, 4, 5]
joonyeol.append(6)
print(joonyeol) # [1, 2, 3, 4, 5, 6]


# sort : 리스트를 오름차순으로 정렬하는 메서드
joonyeol = [3, 2, 4, 1, 5]
joonyeol.sort()
print(joonyeol) # [1, 2, 3, 4, 5]


# reverse : 리스트의 요소 순서를 반대로 뒤집는 메서드
joonyeol.reverse()
print(joonyeol) # [5, 4, 3, 2, 1]


# index : 리스트에서 특정 요소의 인덱스를 반환하는 메서드
joonyeol = ["apple", "banana", "cherry"]
print(joonyeol.index("banana")) # 1


# insert : 리스트의 특정 인덱스에 요소를 삽입하는 메서드
joonyeol = [1, 2, 3, 4, 5]
joonyeol.insert(2,10)
print(joonyeol) # [1, 2, 10, 3, 4, 5]


# remove : 리스트에서 특정 인덱스를 제거하는 메서드
joonyeol = [1, 2, 3, 4, 5]
joonyeol.remove(3)
print(joonyeol) # [1, 2, 4, 5]


# pop : 리스트에서 마지막 요소를 빼낸 뒤, 그 요소를 삭제하는 메서드
joonyeol = [1, 2, 3, 4, 5]
joonyeol.pop(3)
print(joonyeol) # [1, 2, 3, 5]


# count : 리스트에서 특정 요소의 개수를 세는 메서드
joonyeol = [1, 2, 3, 3, 4, 5]
print(joonyeol.count(3)) # 2


# extend : 리스트를 확장하여 새로운 요소들을 추가하는 메서드
joonyeol = [1, 2, 3]
joonyeol.extend([4, 5, 6])
print(joonyeol) # [1, 2, 3, 4, 5, 6]


# += 연산자를 사용해서도 구현할 수도
joonyeol = [1, 2, 3]
joonyeol += [4, 5, 6]
print(joonyeol) # [1, 2, 3, 4, 5, 6]
