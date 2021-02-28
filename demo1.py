# -*- coding = utf-8 -*-
# @Time : 2021/1/17 16:25
# @Author : 王子杰
# @File : demo1.py
# @Software: PyCharm

import random

play = int(input("请输入剪刀(0)、石头(1)、布(2)\n"))
print("你的输入为：",play)

robot = random.randint(0,2)
print("随机生成的数字为：",robot)

if (play == 0 and robot == 1) or (play == 1 and robot == 2) or (play == 2 and robot == 0):
    print("哈哈，你输了！")
elif (play == 0 and robot == 2) or (play == 1 and robot == 0) or (play == 2 and robot == 1):
    print("嘿嘿，你赢了！")
else:
    print("卧槽，平局！")