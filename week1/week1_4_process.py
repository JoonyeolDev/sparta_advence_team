from multiprocessing import Process
import os
## 프로세스 만들기
print('hello, os')
print('my pid is', os.getpid()) # my pid is 89784

def joonyeol():
    print('child process', os.getpid()) # child process 194140
    print('my parent is', os.getppid()) # my parent is 193068

if __name__ == '__main__':
    print('parent process', os.getpid()) # parent process 193068
    child = Process(target=joonyeol).start()


## 동일한 작업을 하는 프로세스 생성하기
def joonyeol():
    print('hello, os')

if __name__ == '__main__':
    child1 = Process(target=joonyeol).start() # hello, os
    child2 = Process(target=joonyeol).start() # hello, os
    child3 = Process(target=joonyeol).start() # hello, os


## 각기 다른 작업을 하는 프로세스 생성하기
def yoon():
    print('my name is yoon')

def joon():
    print('my name is joon')

def yeol():
    print('my name is yeol')

if __name__ == '__main__':
    child1 = Process(target=yoon).start() # my name is yoon
    child2 = Process(target=joon).start() # my name is joon
    child3 = Process(target=yeol).start() # my name is yeol