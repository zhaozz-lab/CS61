# coding:utf-8
#---- Condition
# import sys
# #---- 捉迷藏的游戏
# import threading, time
# class Hider(threading.Thread):
#     def __init__(self, cond, name):
#         super(Hider, self).__init__()
#         self.cond = cond
#         self.name = name
#     def run(self):
#         time.sleep(1) #确保先运行Seeker中的方法
#         self.cond.acquire() #b
#         print(self.name + ': I have blind')
#         self.cond.notify()

#         self.cond.wait() 
                         
#         print(self.name + ': I find you')
#         self.cond.notify()
#         self.cond.release()
          
#         print(self.name + ': I wined')
# class Seeker(threading.Thread):
#     def __init__(self, cond, name):
#         super(Seeker, self).__init__()
#         self.cond = cond
#         self.name = name
#     def run(self):
#         self.cond.acquire()
#         self.cond.wait()    #a    #释放对琐的占用，同时线程挂起在这里，直到被notify并重新占有琐。
#                             #d
#         print(self.name + 'I am finding you ')
#         self.cond.notify_all()
#         self.cond.wait()    #e
#                             #h
#         self.cond.release()
#         print(self.name + 'ai')
# cond = threading.Condition()
# seeker = Seeker(cond, 'seeker')
# hider = Hider(cond, 'hider')
# seeker.start()
# hider.start()



def pig_latin(w):
    if starts_with_a_vowel(w):
        return w + 'ay'
    return pig_latin(w[1:] + w[0])

 # def starts_with_a_vowel():
 #  pass
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-2)+fib(n-1)
print(fib(6)) 

def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n]= f(n)
        return cache[n]
    return memorized
fib = memo(fib)
print(fib(40))


from threading import Condition
step1_finish = 0
start_step2 = Condition()
B=[2,0]
C=[0,5]
M=[[1,2],[1,2]]
A=[0,0]
V = [[1,2]]
def do_step_1(index):
    A[index] = B[index] + C[index]
    print(A)
    start_step2.acquire()
    step1_finish += 1
    if(step1_finish==2):
        start_step2.notify_all()
    start_step2.release()

def do_step_2(index):
    start_step2.wait()
    V[index] = M[index].A

print("test")
print("test")

# do_step_1(0)
# do_step_2(1)
# print(A)
# print(V)