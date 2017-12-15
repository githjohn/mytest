#抓重点
#深浅拷贝
# import copy
#浅copy之copy一层 不会在往下曾
#深copy 要用import copy 独立模块
#x=copy.copy()#浅copy
#x=copy.deepcopy(要copy的列表) #深copy 互相不影响
#假如要取一部分内容
s=[[1,2],'w','e']
#b=s 指向全部都指向地址了
#所以都会修改 （还是因为列表的原因）
# 他们共享了一个内存空间 所以不会创建
# 所以要用copy
#s2=[2,'z','x']
s2=s.copy()#字面上的意思
#看http://www.cnblogs.com/johnnyzhou/articles/8024862.html
#修改基本类型 不会发生变化  但是修改类表
#他们指向的问题，所以修改类表他们都会变化
#s2=[:] #全部取出赋值 因为指针的问题

#重点
# set（集合）只有这一种创建方式
#特性 掉重复的字符,
# 关系测试
# 【交集s.intersection(b) s&b 交集
#并集s.union(d) 合并起来 a=t | s 并集
#差集s.difference(b) 返回 s有b里面没有的 s-b 差集
# 对称交集s.symmetric_difference(b) 返回都没有的 s^b 对称交集
# （不重复 无序 迭代 迭代器）
#里面的内容要要是不可变
#s=set('as d')#{'a', 's', ' ', 'd'}
#s1=['sdf','sgf','sd','sd']
#s2=set(s1)
#添加
#.add('u')  随机的添加一个元素
#.update([12,"sd"]) 更新的意思  把这个字符拆分添加
#删除  .remove()  直接删除
#.pop() 随机删除
#.clear() 清空集合 del s

#父集 超集
#s={12,"sd","a","b"}
#b={12,"sd"}
#print(s.issuperset(b)) #s>b 父  True or false
#s.issubset(b)  #s<b子

#函数
#http://www.cnblogs.com/johnnyzhou/articles/8039747.html
#减少重复代码  方便代码 更易扩展  保持代码一致性
#def add(w,e):形参
#   print(w+e)
#add(5,7) 实参
#import time
#time_format="%Y-%m-%d %X" #指定时间格式
#print(time.strftime(time_format)) #显示当前时间
#参数  必须参数  默认参数
#def input_student(name="a",age=2)
#不定长参数  def add(*args) 类似于元祖 所以要循环
#def add(**args) 这个可以传入多个 创建成字典
#def print_info(*arg,**args) 固定格式
#要是有默认参数  放左边 （name关键字参数，a=3默认参数，*a,**a）
#return 返回内容
#作用域
#有优先级 局部作用域不能修改全局变量
# count = 10
# def outher():
#         global count 声明说全局的  这样就可以修改了
#         print(count) #查找然后系统任务是全局的
#         count = 4#所以现在修改之后上面报错  因为局部变量 不能修改全局变量
#nonlocal count 要是在第三层用这个声明是全局变量













