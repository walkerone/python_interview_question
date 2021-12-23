import time
import datetime
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

import datetime


def day_year():
    year = input("请输入年份: ")
    month = input("请输入月份: ")
    day = input("请输入天: ")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    print((date1 - date2).days + 1)
    return (date1 - date2).days + 1
day_year()
