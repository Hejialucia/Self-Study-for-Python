# Python程序的控制结构
# 语法知识点：
# 1. 单分支结构
# if <条件>:
#    <语句块>
# Guess = eval(input())
# if Guess == 99:
#     print("Yes!")
# 2. 二分支结构
# if <条件>:
#    <语句块1>
# else <条件>:
#      <语句块2>
# guess = eval(input())
# if guess == 99:
#     print("Yes!")
# else:
#     print("No!")
# 紧凑形式:
# <表达式1>if<条件>else<表达式2>
# GuEss = eval(input())
# print("Yes" if GuEss == 99 else "No")
# 标准: print("猜{}了".format("对" if GuEss == 99 else "错"))
# 3. 多分支结构
# if <条件>:
#    <语句块1>
# elif:
#    <语句块2>
# else:
#    <语句块3>

# 条件组合
# x and Y; x or Y; not x

# 异常处理
# try:
#    <语句块1>
# except:
#        <语句块2>
# 或者：
# try:
#    <语句块1>
# except<异常类型>:
#        <语句块2>
# 举例1
# try:
#     num = eval(input())
#     print(num * 2)
# except:
#     print("wrong")
# 举例2
# try:
#     num = eval(input())
#     print(num * 2)
# except NameError:
#     print("wrong")
# 异常处理高级用法:
# try:
#    <语句块1>
# except:
#        <语句块2>
# else:                 # else对应的语句块3在不发生异常时执行
#      <语句块3>
# finally:              # finally对应的语句块4一定执行
#        <语句块4>

# BMI问题
# height, weight = eval (input("请输入身高(米)和体重(公斤)，并用逗号隔开："))
# BMI= weight /(height ** 2)
# print("BMI的数值为: {:.2f}".format(BMI))
# type1 = ""
# type2 = ""
# if BMI < 18.5:
#     type1 = "偏瘦"
#     type2 = "偏瘦"
# elif BMI >= 18.5 and BMI <= 24:
#     type1 = "正常"
#     type2 = "正常"
# elif BMI > 24 and BMI <= 25:
#     type1 = "正常"
#     type2 = "偏胖"
# elif BMI > 25 and BMI <= 28:
#     type1 = "偏胖"
#     type2 = "偏胖"
# elif BMI > 28 and BMI <= 30:
#     type1 = "偏胖"
#     type2 = "肥胖"
# else:
#     type1 = "肥胖"
#     type2 = "肥胖"
# print("国际是{0}，国内是{1}".format(type1,type2))

# 程序的循环结构(遍历for;无限while)
# 1. 遍历循环
# 普通遍历
# for <循环变量> in <遍历结构>:
#             <语句块>
# N次计数循环
# for i in range(N):
#                   <语句块>
# 特定次计数循环
# for i in range(M,N,K):
#                   <语句块>
# 字符串遍历循环
# for c in s:               #s是字符串, c是字符串中的每个字符
#                   <语句块>
        # eg: for c in "Python123":
        #                           print(c,end=",")
# 列表遍历循环
# for item in ls:       #ls是列表
#               <语句块>
        # eg: for item in [123,"PY",456]:
        #    print(item,end="!")
# 文件遍历循环
# for line in fi:       # 对文件进行遍历
#               <语句块>

# 2. 无限/条件循环: 由条件控制的循环运行方式
# while <条件>:
#   <语句块>

# 循环控制保留字 break / continue
# break: 跳出并结束当前整个循环，执行循环后的语句
# continue: 结束当次循环，继续执行后续次数循环
# for c in "PYTHON":
#     if c == "T":
#         continue      #当前循环结束，寻找下一次循环
#     print(c,end="!")      # P!Y!H!O!N!
# for c in "PYTHON":
#     if c == "T":
#         break      #到T后就不循环了，直接结束
#     print(c,end="!")      # P!Y!
# 双层循环
# s = "PYTHON"
# while s != "":
#     for c in s:
#         print(c,end="!")
#     s = s[:-1]              # PYTHONPYTHOPYTHPYTPYP
# 含break的双层循环(有点难)
# s = "PYTHON"
# while s != "":
#     for c in s:
#         if c == "T":
#             break           #一个break只能跳出一层循环
#         print(c,end="!")
#     s = s[:-1]              #P!Y!P!Y!P!Y!P!Y!P!Y!P!
# 循环与else的高级搭配
# 1.
# for <循环变量> in <遍历结构>:
#     <语句块1>
# else:
#     <语句块2>
# 2.
# while <条件>:
#     <语句块1>
# else:
#     <语句块2>
# 举例
# for c in "PYTHON":
#     if c == "T":
#         continue
#     print(c,end="!")
# else:
#     print("game over")      # P!Y!H!O!N!game over

# for c in "PYTHON":
#     if c == "T":
#         break
#     print(c,end="!")
# else:
#     print("game over")          # P!Y!

# random库 - 使用随机数的python标准库
# import random
# 基本随机数函数:  seed(); random()
# 扩展随机数函数:  randint();getrandbits();uniform();randrange(m,n[,k]);choice();shuffle()
# import random
# random.seed(10)       # 不给种子的话,是第一次调取时的系统时间
# print(random.random())
# print(random.random())

# 圆周率的计算
# 方法1:
# pi = 0
# N = 100
# for k in range(N):
#     pi += 1/pow(16,k) * ( 4 / (8 * k + 1) - 2/ (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
# print ("圆周率的值是: {}".format(pi))

# 方法2:
from random import random
from time import perf_counter
DARTS = 1000 * 1000
hits = 0.0
start = perf_counter()
for i in range(1,DARTS+1):
    x,y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <=1.0:
        hits = hits + 1
pi = 4 * (hits / DARTS)
print("圆周率是：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter() - start))

