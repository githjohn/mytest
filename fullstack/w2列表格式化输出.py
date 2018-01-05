
#---列表
#a=[1,2,3,4]
#print(a[-1:])#最后一个数字[4]
#print(a[0:])#从0位置开始取到最后[1, 2, 3, 4]
#print(a[1:-1])#位置1开始取 -1最后一个位置不取[2, 3]
#print(a[1:-1:1])#传递给后面从一开始[2, 3]
#print(a[1::2])#从左到右隔一个去取 另立门户 [2, 4]
#print(a[3::-1])#翻转过来取值[4, 3, 2, 1]
#print(a[-2::-1])#-1是倒过来取值 [3, 2, 1]
#添加append insert
#a.append('xuepeng')#默认插到最后一个位置
#a.insert(1,'xuepeng') #将数据插入到任意一个位置
#修改
#a[1]='haidilao'
#a[1:3]=['a','b'] #从第一个位置开始到第二个位置修改 最后一个不算
#print(a)#[1, 'a', 'b', 4]
#删除 remove pop del
#c=["a","a","a","a"]
#c.remove("a") #只删除一个
#a.remove(a[0])
#a.pop(1)#会返回删除的值
#del a[0]
#del a
#count:计算某元素出现次数
#t=['to', 'be', 'or', 'not', 'to', 'be'].count('to')
#extend
#a = [1, 2, 3]
#b = [4, 5, 6]
#a.extend(b)
#index根据内容找位置
#a = ['wuchao', 'jinxin', 'xiaohu','ligang',['wuchao', 'jinxin']]
#first_lg_index = a.index("ligang")
#print("first_lg_index",first_lg_index)
#reverse该方法没有返回值  倒序排序
#a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang']
#a.reverse()
# x = [4, 6, 2, 1, 7, 9]
# x.sort(reverse=True)#  该方法没有返回值
# print(x)
# for i in range(1,101,2): #2 步长
#     print("loop:",i)
#-------格式化输出
# name = input("Name:")
# age = int(input("Age:"))
# job = input("Job:")
# salary = input("Salary:")
# if salary.isdigit(): #长的像不像数字,比如200d , '200'
#     salary = int(salary)
# msg = '''
# --------- info of %s --------
# Name: %s
# Age : %d
# Job : %s
# Salary: %f
# You will be retired in %s years
# -------- end ----------
# ''' % (name,name ,age ,job ,salary, 65-age )
# print(msg)
