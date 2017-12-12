#字典两大特点：无序，键唯一
# dic={'age':'alex','age':35,'hobby':{'girl_name':'铁锤','age':45},'is_handsome':True}
#列表创建
# a=list()
#字典的2种创建
# dic={'name':'alex'}
#第二种创建方式 dict() 工厂函数 创建一个键值对后面要加一个 "," 2个以后就不用加 相当于吧：换成了 ,
#dic2=dict((('name','alex'),('name1','alex')))
#跟上面一样
#dic3=dict([['name','alex'],['name1','alex']])
#增加
# dic1={'name':'alex'}
# dic1['age']=18
#键存在，不改动，返回字典中相应的键对应的值
#键不存在，在字典中中增加新的键值对，并返回相应的值
# ret=dic1.setdefault('age',34)
#查  通过键去查找
#dic3={'age': 18, 'name': 'alex', 'hobby': 'girl'}
# print(dic3['name'])
#查看键 dict_keys类型
#print(list(dic3.keys())) #转换成列表
#print(list(dic3.values()))
#print(list(dic3.items())) #拿出所有的键值对
#dic3={'age': 18, 'name': 'alex', 'hobby': 'girl'}
#dic3['age']=55
# dic4={'age': 18, 'name': 'alex', 'hobby': 'girl'}
# dic5={'1':'111','name':'222'}
# dic4.update(dic5)  添加进去
#要是有相同的key了 会覆盖
# dic5 = {'name': 'alex', 'age': 18, 'class': 1}
# dic5.clear() # 清空字典键值对
# del dic5['name'] #删除字典中指定键值对
# print(dic5.pop('age')) #删除字典中指定键值对，并返回该键值对的值
# a = dic5.popitem() #随机删除某组键值对，并以元组方式返回值
# del dic5        #删除整个字典
#5 其他操作以及涉及到的方法
#dic6=dict.fromkeys(['host1','host2','host3'],'test')
# #创建字典[这里面是key]后面是values不过值全部都是一样的
#dic6['host2']='abc' #可以修改
#dic6=dict.fromkeys(['host1','host2','host3'],['test1','tets2'])
#dic6['host2'][1]='test3' #这个就全部修改了 没办法就是这么任性
# print(dic6)#{'host3': ['test1', 'test3'], 'host2':
# ['test1', 'test3'], 'host1': ['test1', 'test3']}
#小练习
# av_catalog = {
#     "欧美":{
#         "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#         "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#         "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }
# av_catalog['欧美']["www.youporn.com"][1]='高清午马'
#dic={5:'555',2:'666',4:'444'}
# dic.has_keys(5)
# print(5 in dic)
#print(sorted(dic.items()))
#默认打印的是键  推荐 效率高
#dic5={'name': 'alex', 'age': 18}
# for i in dic5:
#     print(i,dic5[i])+
#元祖 去掉括号加 ,v
#for i,v in dic5.items():
#     print(i,v)
#String 操作
#""  ''  这个创建是没有区别的 在python
# a="Let's go "
# 1   * 重复输出字符串
# print('hello'*20)
# 2 [] ,[:] 通过索引获取字符串中字符,这里和列表的切片操作是相同的,具体内容见列表
# print('helloworld'[2:])
#关键字 in
# print(123 in [23,45,123])
# print('e2l' in 'hello')
# 4 %   格式字符串
#print('%s is a good teacher'%'alex')
#字符串的方法
# a='123'
# b='abc'
# d='44'
# # # c=a+b#效率不好 浪费内存
# c= '--'.join([a,b,d]) #用这个比较好
#'' 拼接 这个里面是拼接的内容 123--abc--44
# String的内置方法
st='hello kitty {name} is {age}'
#print(st.count('1'))       #  统计元素个数
#print(st.capitalize())     #  首个单词字母大写
# print(st.center(50,'#'))   #  居中 设置格式 符号
# print(st.endswith('tty3')) #  判断是否以某个内容结尾
# print(st.startswith('he')) #  判断是否以某个内容开头
# print(st.expandtabs(tabsize=20)) #st=he\tee  设置空格个数
# print(st.find('t'))        #  查找到第一个元素，并将索引值返回
# print(st.format(name='alex',age=37))  # 格式化输出的另一种方式
# print(st.format_map({'name':'alex','age':22}))
# print(st.index('t'))
# print('asd'.isalnum())#判断是否包含数字或字母的
# print('12632178'.isdecimal())#是否是10进制
# print('1269999.uuuu'.isnumeric())
# print('abc'.isidentifier()) #判断是否是非法字符
# print('Abc'.islower()) #判断是否全是小写
# print('ABC'.isupper())
# print('  e'.isspace()) #是否是个空格
# print('My title'.istitle()) #查看开头字母是否大写
# print('My tLtle'.lower()) #大写变小写
# print('My tLtle'.upper()) #小写变大写
# print('My tLtle'.swapcase()) #大小写反转
# print('My tLtle'.ljust(50,'*')) #字母在右边
# print('My tLtle'.rjust(50,'*'))#字母在左边
# print('\tMy tLtle\n'.strip()) #去掉空格
# print('\tMy tLtle\n'.lstrip()) #去掉
# print('\tMy tLtle\n'.rstrip())
#print('My title title'.replace('itle','lesson',1))
#replace替换 要是替换一部分就在后面添加 一个1或者其他
# print('My title title'.rfind('t'))
# print('My title title'.split('i',1))
# print('My title title'.title()) # title后面的T变成大写
#摘一些重要的字符串方法
#1 print(st.count('l'))
# print(st.center(50,'#'))   #  居中
# print(st.startswith('he')) #  判断是否以某个内容开头
# print(st.find('t'))
# print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
# print('My tLtle'.lower())
# print('My tLtle'.upper())
# print('\tMy tLtle\n'.strip())
# print('My title title'.replace('itle','lesson',1))
#print('My title title'.split('i',1))
