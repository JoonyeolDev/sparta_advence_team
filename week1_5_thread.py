import threading
import os


## 코드로 스레드 만들기
# def joonyeol():
#     print('thread id', threading.get_native_id()) #thread id 197660
#     print('process id', os.getpid()) # process id 197696

# if __name__ == '__main__':
#     print('process id', os.getpid()) # process id 197696
#     thread = threading.Thread(target=joonyeol).start()


## 동일한 작업을 하는 스레드 생성하기
# def joonyeol():
#     print('thread id', threading.get_native_id())
#     print('process id', os.getpid())

# if __name__ == '__main__':
#     print('process id', os.getpid())
#     thread1 = threading.Thread(target=joonyeol).start()
#     thread2 = threading.Thread(target=joonyeol).start()
#     thread3 = threading.Thread(target=joonyeol).start()

#     # process id 198716
#     # thread id 194600
#     # process id 198716
#     # thread id 197272
#     # process id 198716
#     # thread id 197408
#     # process id 198716
#     # process는 같지만 thread는 다르다


## 각기 다른 작업을 하는 스레드 생성하기

def yoon():
    print('This is yoon')

def joon():
    print('This is joon')

def yeol():
    print('This is yeol')

if __name__ == '__main__':
    thread1 = threading.Thread(target=yoon).start()
    thread2 = threading.Thread(target=joon).start()
    thread3 = threading.Thread(target=yeol).start()

    # This is yoon
    # This is joon
    # This is yeol