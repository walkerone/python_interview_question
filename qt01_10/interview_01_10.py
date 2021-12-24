import time
# import datetime
import os
import sys

# 1.有一个jsonline格式的文件file.txt大小约为10K](#1有一个jsonline格式的文件filetxt大小约为10k
# 解决方法总结 https://blog.csdn.net/u012733099/article/details/84286626
# def get_lines():
#     with open('file.txt', 'rb') as f:
#         return f.readlines()  # 返回的是列表

# 方法1
# 文件太大，一次，最后读取少于内存大小的数据，且读取次数要合理
# def get_lines():  # 赋值给一个变量，调用一次 __next__() 打印一次
#     print('walker_walker')
#     with open('file.txt', 'rb') as f:
#         for i in f:
#             yield i
#
#
# if __name__ == '__main__':
#     for e in get_lines():  # 生成器，调用的时候就返回一次
#         print(e)  # Process each row of data
#

# --------------------------------------
# 方法_2
# 现在要处理一个大小为10G的文件，但是内存只有4G，如果在只修改get_lines 函数而其他代码保持不变的情况下，应该如何实现？需要考虑的问题都有那些？
# def get_lines():  # 读取时时每次指定到小，读不到的时候 break
#     with open('file.txt', 'rb') as f:
#         while True:
#             data = f.read(3 * 3)
#             if not data:
#                 break
#             yield data
#
#
# if __name__ == '__main__':
#     for e in get_lines():  # 生成器，调用的时候就返回一次
#         # print(e)
#         time.sleep(0.1)
#         print(e, end='')  # Process each row of data

# 问题2-------------------
# 2.补充缺失的代码](#2补充缺失的代码
# 函数的嵌套，写一个方法自己调用自己
# import os
#
# # 补充1  walker------------
# def func(path_direct):
#     for child in os.listdir(path_direct):
#         s_child = os.path.join(path_direct, child)
#         if os.path.isdir(s_child):
#             func(s_child)  # 如果是文件夹，自己再调用自己，
#         else:
#             print(s_child)
#
#
# func(r'F:\report')
# ----------------
# 问题3 输入日期， 判断这一天是这一年的第几天？

# import datetime
#
#
# def day_year():
#     # year = input("请输入年份: ")
#     # month = input("请输入月份: ")
#     # day = input("请输入天: ")
#
#     year = '2021'
#     month = '6'
#     day = '22'
#     date1 = datetime.date(year=int(year), month=int(month), day=int(day))
#     date2 = datetime.date(year=int(year), month=1, day=1)
#     print(date1)
#     print(type(date1))
#     print(date1 - date2)
#
#     print((date1 - date2).days + 1)
#     print((date1-date2).seconds + 1)
#     return (date1 - date2).days + 1
#
# day_year()
# ------------------

# 4 打乱一个排好序的list对象alist？
import random

#
# alist = [1, 2, 3, 4, 2, 5]
# # 方法一
#
# random.shuffle(alist)
#
# print(alist)

# 问题4  随机数 import random
#
# def make_code(size=4):
#     res = ''
#     for i in range(size):
#         s1 = chr(random.randint(65, 90))  # 大写
#         s3 = chr(random.randint(97, 122))
#         s2 = str(random.randint(0, 9))
#         res += random.choice([s1, s2, s3])
#     return res
#
#
# print(make_code(6))
# -----------------------
# nums = [-3, 4, 7, 10, 13, 21, 43, 77, 89]
# find_num = 8


# def binary_search(find_num, l):
#     print(l)
#     if len(l) == 0:
#         print('找的值不存在')
#         return
#     mid_index = len(l) // 2
#
#     if find_num > l[mid_index]:
#         # 接下来的查找应该是在列表的右半部分
#         l = l[mid_index + 1:]
#         binary_search(find_num, l)
#     elif find_num < l[mid_index]:
#         # 接下来的查找应该是在列表的左半部分
#         l = l[:mid_index]
#         binary_search(find_num, l)
#     else:
#         print('find it')
#
#
# binary_search(find_num, nums)

# 问题解决方法 二进制查找
# lt = [-3, 4, 7, 10, 13, 21, 43, 77, 89]
# find_num = 5
#
#
# def walker_search(find_num, lt):
#     l_lenth = len(lt)
#     if l_lenth == 0:
#         print('数据不在里面呦')
#         return
#     mid_index = l_lenth // 2
#     if find_num < lt[mid_index]:
#         lt = lt[:mid_index]
#         walker_search(find_num, lt)
#     elif find_num > lt[mid_index]:
#         lt = lt[mid_index:]
#         walker_search(find_num, lt)
#     else:
#         print(lt[mid_index])
#         print('find it out')
#
#
# walker_search(7, lt)


# 2、lamdab用于定义匿名函数
# print(lambda x,y:x+y)


# 3、调用匿名函数
# 方式一：
# res=(lambda x,y:x+y)(1,2)
# print(res)

# 方式二：
# func=lambda x,y:x+y
# res=func(1,2)
# print(res)

# 4、匿名用于临时调用一次的场景：更多的是将匿名与其他函数配合使用

salaries = {
    'siry': 3000,
    'tom': 7000,
    'lili': 10000,
    'jack': 2000
}
# 需求1：找出薪资最高的那个人=》lili
# res=max([3,200,11,300,399])
# print(res)

# res=max(salaries)
# print(res)


salaries = {
    'siry': 3000,
    'tom': 7000,
    'lili': 10000,
    'jack': 2000
}
# 迭代出的内容    比较的值
# 'siry'         3000
# 'tom'          7000
# 'lili'         10000
# 'jack'         2000

# def func(k):
#     return salaries[k]

# ========================max的应用
# res=max(salaries,key=func) # 返回值=func('siry')
# print(res)

# res=max(salaries,key=lambda k:salaries[k])
# print(res)

# ========================min的应用
# res=min(salaries,key=lambda k:salaries[k])
# print(res)


# ========================sorted排序
# salaries={
#     'siry':3000,
#     'tom':7000,
#     'lili':10000,
#     'jack':2000
# }
# res = sorted(salaries, key=lambda k: salaries[k], reverse=True)
# print(res)

# ========================map的应用(了解)
# l=['alex','lxx','wxx','薛贤妻']
# new_l=(name+'_dsb' for name in l)
# print(new_l)

# res=map(lambda name:name+'_dsb',l)
# print(res) # 生成器
# ========================filter的应用（了解）
# l=['alex_sb','lxx_sb','wxx','薛贤妻']
# res=(name for name in l if name.endswith('sb'))
# print(res)

# res=filter(lambda name:name.endswith('sb'),l)
# print(res)

# ========================reduce的应用(了解)
# from functools import reduce
#
# res = reduce(lambda x, y: x + y, [1, 2, 3], 10)  # 16
# print(res)
#
# res = reduce(lambda x, y: x + y, ['a', 'b', 'c'])  # 'a','b'
# print(res)

# 问题 5.现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
# 方法1
# d = {'asdf': 24, 'gee': 52, 'iee': 12, 'kee': 33}
# res = sorted(d, key=lambda k: d[k], reverse=True)
# print(res)
# res_second = sorted(d.items(), key=lambda x: x[0],reverse=True)
# x[0] 代表用key进行排序，x[1] 代表用value进行排序
# print(res_second)
# -------------
# 6.字典推导式
iterable = [("sd", "sdfd"), ('eee', 'sdfsd')]
d = {key: value for (key, value) in iterable}
print(d)
# 7.请反转字符串 "aStr"?
# print("aStr"[::-1])

# 将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
# old_str = "k:1 |k1:2|k2:3|k3:4"


# 方法1实现
# def get_dict(data=old_str):
#     new_dict = {}
#     for item in data.split('|'):
#         second_item = item.split(":")
#         print(second_item)
#         new_dict[second_item[0]] = second_item[1]
#     print(new_dict)
#
#
# #
# #
# get_dict()
# 方法2实现
# res = {key: v for t in old_str.split("|") for key, v in (t.split(':'),)}  # why 加括号
# print(res)
