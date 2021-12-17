import time
import datetime
import os
import sys


# 1.有一个jsonline格式的文件file.txt大小约为10K](#1有一个jsonline格式的文件filetxt大小约为10k
# 解决方法总结 https://blog.csdn.net/u012733099/article/details/84286626
# def get_lines():
#     with open('file.txt', 'rb') as f:
#         return f.readlines()  # 返回的是列表


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
# 现在要处理一个大小为10G的文件，但是内存只有4G，如果在只修改get_lines 函数而其他代码保持不变的情况下，应该如何实现？需要考虑的问题都有那些？
def get_lines():  # 读取时时每次指定到小，读不到的时候 break
    with open('file.txt', 'rb') as f:
        while True:
            data = f.read(3 * 3)
            if not data:
                break
            yield data


if __name__ == '__main__':
    for e in get_lines():  # 生成器，调用的时候就返回一次
        time.sleep(0.01)
        print(e, end='')  # Process each row of data
