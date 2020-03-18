"""for 循环原理"""
list01 = [1,2,5,7]  # 可迭代对象：具有 __iter__() 方法的，可返回迭代器的对象
"""原理3步："""
iterator = list01.__iter__() #（1）获取迭代器对象
while True:
    try:  #(2)循环迭代，如果获取了全部元素，则执行 except 语句
        iterator.__next__()
    except:  # （3）捕获StopIteration异常，跳出循环
        break


# import sys
# sys.path.append()    自行添加项目根目录
"""练习：输入成绩，并对其进行判断"""
def get_score():
    while True:
        try:
            score = int(input("请输入成绩"))
        except:  # 当输入不正确后，则进入 except 语句
            print("输入有误")
            continue # 跳过本次循环
        if 1 <= score <= 100:
            return score   # 当执行进入 if 语句，则跳出循环
        print("成绩不再范围内")

'''当项目中有很多有可能出现异常的地方需要 try 语句进行判断，可以将其提出做成一个方法，一遍后续的复用'''
dict01 = {"张三丰":101,"张无忌":102,"赵敏":102}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key,dict01[key])
    except:
        break