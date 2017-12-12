#三级菜单
#可以一层一层进入到所有曾
#可以在每层返回上一层
#可以在任意曾推出 主菜单
menu = {
    "火车":{"河南省":
                    {"郑州站":{},"漯河站":{},"信阳站":{}},
            "湖北省":
                    {"武汉站":{},"武昌站":{}}},

    "地铁":{"线路11":
                    {"李子园":{},"曹杨路":{},"江苏路":{}},
            "线路9":
                    {"徐家汇":{},"松江新城":{},"九亭":{}}},

    "公交":{"1223":
                    {'荣和怡景园':{},'自来水厂':{},'大渡口':{}},
            "嘉定区间":
                    {'乐购':{},'新玛特':{},'家乐福':{}}}
        }
current_layer = menu #存储选择的字典
parent_layers = [] #记住上层的
while True:
    for key in current_layer:  #显示
        print(key)
    choice = input(">>:").strip() #用户选择输入
    if len(choice) == 0:continue #判断是否输入
    if choice in current_layer: #判断是否是字典里面的
         parent_layers.append(current_layer) #将内容存储在变量里面
         current_layer = current_layer[choice] #将选择的列表覆盖掉原来的
    elif choice == "b":  #退出功能
        current_layer = parent_layers.pop()  #因为是列表 所以 会按照顺序删除。
        print("-----------")
        print(current_layer)  #打印显示
        print("-----------")
    else:
        print("无此项")

