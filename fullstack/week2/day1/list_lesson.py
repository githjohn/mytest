#a=['wuchao','jinxin','xiaohu','sanpang','ligang']
# #-1是一直取到低
# #查  切片 []
#print(type(a[0:]))#取到最后
#print(a[1:-1])#取到倒数第二值
#print(a[1:-1:1])#传递给后面从一开始
#print(a[1::2])#从左到右隔一个去取 另立门户
#print(a[3::-1])#翻转过来取值
#print(a[-2::-1])#-1是倒过来取值
#添加append insert
#a.append('xuepeng')#默认插到最后一个位置
#a.insert(1,'xuepeng') #将数据插入到任意一个位置
#修改
#a[1]='haidilao'
#a[1:3]=['a','b']
#print(a)
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
#little_list = a[first_lg_index+1:]
#second_lg_index = little_list.index("ligang")
#print("second_lg_index",second_lg_index)
#second_lg_index_in_big_list = first_lg_index + second_lg_index +1
#print("second_lg_index_in_big_list",second_lg_index_in_big_list)
#print("second lg:",a[second_lg_index_in_big_list])
#reverse该方法没有返回值  倒序排序
#a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang']
#a.reverse()
#x = [4, 6, 2, 1, 7, 9]
#x.sort(reverse=True)  该方法没有返回值
