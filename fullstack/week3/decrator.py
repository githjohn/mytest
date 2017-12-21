#http://www.cnblogs.com/alex3714/articles/5765046.html
#装饰器 为之前函数添加新的功能
import time
#修改功能  执行时间
#开放，功能扩展
# 封闭原则，修改功能 不能在函数里面修改
#代码不能重复  重复用函数解决
#这个算是模块
# def show_time(f): #装饰器函数
#     def inner():
#         start=time.time()#获取当前时间 一串数字多少秒 时间戳  1970开始
#         f()
#         time.sleep(1)
#         end=time.time()
#         print("spend %s"%(end-start))
#     return inner
# @show_time #foo=show_time(foo)  py 给我们的做法
# def foo():
#     print('this is')
#在改进
#foo=show_time(foo)
# foo()
#優化
#功能函数加参数
# def show_time(f): #装饰器函数
#     def inner(*x,**y):
#         start=time.time()#获取当前时间 一串数字多少秒 时间戳  1970开始
#         f(*x,**y)
#         time.sleep(1)
#         end=time.time()
#         print("spend %s"%(end-start))
#     return inner
# @show_time #foo=show_time(foo)  py 给我们的做法
# def add(*a,**b):
#     sums=0
#     for i in a:
#         sums+=i
#     print(sums)
# add(2,4,5)
#装饰器加参数
#功能函数加参数
def logger(flag=''): #用了闭包的做法 上面参数下面用
    def show_time(f): #装饰器函数
        def inner(*x,**y):
            start=time.time()#获取当前时间 一串数字多少秒 时间戳  1970开始
            f(*x,**y)
            time.sleep(1)
            end=time.time()
            print("spend %s"%(end-start))
            if flag=='true':
                print('添加日志')
        return inner
    return show_time
@logger('true') #@show_time(foo)
def add(*a,**b):
    sums=0
    for i in a:
        sums+=i
    print(sums)
add(2,4,5)
#联系登录
user,passwd='alex',123
#存储状态
login_status = False
def login():
    if login_status == False:
        username = input("username:")
        userpasswd = input("passwd:")
        if  username==user  and  passwd==userpasswd:
            print("welcome to ")
            login_status=True

    else:
        pass
#模拟京东不同页面
def home():
    print("welcome to home page")
def finance():#金融
    print("welcome to home page")
def book():
    print("welcome to home page")

#生成器

#迭代器

# time  random  json  pickle

#列表生成器
def f(n):
    return n**3
s=[f(x) for x in range(10)]#列表生成器 全部放内存里面  卡顿  一次性都能出来
s1=(f(x) for x in range(10)) #生成器对象 厨师 想吃什么就做什么 in py2 s.next()取值 0  in py3 next(s) or s.__next__()内置特殊方法 不推荐
print(next(s1))
print(next(s1))#一个一个取 有脾气
#生成器就是一个可迭代对象
for i in s1:
    print(i)
#生成器2种创建方式
#s1=(f(x) for x in range(10))
#yield
def foo():
    print(1)
    count=yield 1 #赋值
    print(2)
    yield 2
#send
b=foo()
b.send(None)#第一次没有next 就要加none
test=("112",1)
a,b=test #分别取出元祖里面的元素   如果要是多了不匹配就报错
#什么是可迭代器
l=[1,2,3]
l.__iter__()#对象有这个方法就是可。。
#迭代器 生成器都是迭代器 反過來不一定
#time模块
time.time()
help(time)
time.clock()
#random
#os模塊
