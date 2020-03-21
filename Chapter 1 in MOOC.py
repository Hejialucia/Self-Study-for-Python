# Python基本语法元素
# 语法知识点：
# 1.注释：单行注释：#开头；多行注释'''      '''
# 2.索引：返回字符串中单个字符 <字符串>[M] 如上；
#  切片：返回字符串中一段字符子串 <字符串>[M：N] Tem[1:3] - 取出字符串中第一个第二个字符但不到第三个
# 3.评估函数eval() - 去掉参数最外侧引号并执行余下语句的函数
# eg: eval("1") - 1; eval("1+2") - 3; eval('"1+2"') - "1+2"; eval('print("Hello")') - Hello

# 计算圆的面积
r = 25
area = 3.1415 * r * r
print(area)
print("{:.2f}".format(area))

# 同切圆绘制
import turtle
turtle.pensize(2)
turtle.circle(10)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)

# 五角星绘制
import color as color
from turtle import*
color('red','red')
begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill()

# 温度转换 摄氏度-华氏度
TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1])-32) / 1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0:-1])+ 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")

# HelloWorld
Number = eval(input())
if Number == 0:
    print("Hello World")
elif Number > 0:
     print("He\nll\no \nWo\nrl\nd")
else:
    for i in "Hello World":
        print(i)

# 数值运算
# 1.
M = input()
result = eval(M)
print("{:.2f}".format(result))
# 2.
s = input()
print("{:.2f}".format(eval(s)))


# 货币转换
# 1.
Money = input()
if Money[0:2] == "RMB":
    USD = (eval(Money[3:]) / 6.78)
    print("USD{:.2f}".format(USD))
elif Money[0:2] == "USD":
    RMB = (eval(Money[3:]) * 6.78)
    print("RMB{:.2f}".format(RMB))
# 2.
CurStr = input()
if CurStr[:3] == "RMB":
    print("USD{:.2f}".format(eval(CurStr[3:]) / 6.78))
elif CurStr[:3] in ['USD']:
    print("RMB{:.2f}".format(eval(CurStr[3:]) * 6.78))

    
