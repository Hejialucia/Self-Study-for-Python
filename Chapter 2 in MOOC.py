# 语法知识点：
# 模块：库Library、包Package、模块Module
# turtle.setup(width,height,startx,starty) - setup()设置窗体大小及位置，不是必须的
#           窗体长， 窗体宽， 窗体相对于整个屏幕的相对位置
# turtle空间坐标体系：四象限   turtle.goto()：任何位置的海龟到达某一坐标位置
# turtle.goto( 100, 100)
# turtle.goto( 100,-100)
# turtle.goto(-100,-100)
# turtle.goto(-100, 100)
# turtle.goto( 0, 0)
# turtle.fd(d): 海龟的正前方向运行
# turtle.bk(d): 海龟的反方向运行
# turtle.circle(r,angle): 以海龟当前位置 左侧的某一个点为圆心 进行曲线运行
# turtle.seth(angle): 改变海龟行进方向(绝对角度)，只改变方向但不行进

# turtle.colormode(mode) mode:1.0 - RGB小数值；mode:255 - RGB整数值
# 库引用的概念 import 库名; 库名.函数名(函数参数)
# 3个用法：1. import turtle 后续需要turtle.函数名(函数参数)  - 不会出现函数重名
#        2. from turtle import* 后续直接用函数名(函数参数)  - 可能会发生函数名字冲突
# 最佳    3. import 库名 as 库别名; 库别名.函数名(函数参数)

# 画笔基本控制函数  - 画笔操作后一直有效
# turtle.penup() 别名:turtle.pu() 不显示
# turtle.pendown() 别名:turtle.pd() 开始画
# turtle.pensize(width)  别名:turtle.width(width) 画笔宽度
# turtle.pencolor(color)  别名:turtle.color(color) 画笔颜色
# color三种形式："颜色字符串"；rgb小数值；(rgb元组值)
#
# 画笔运动函数 - 控制海龟行进：走直线/曲线
# turtle.forward(d) 别名:turtle.fd(d) 向前行走直线; d - 行进距离可以为负
# turtle.circle(r,extent = None) - 根据半径r绘制extent角度的弧型;
# r:默认圆心在海龟[左侧]r距离的位置;extent:绘制角度，默认360度整圆
# turtle.circle(100)    turtle.circle(-100,90)

# 画笔方向控制函数
# turtle.setheading(angle) 别名:turtle.seth() - 改变行进方向
#       turtle.seth(45) - 绝对坐标下转45度
# turtle.left(angle)
# turtle.right(angle)
#
# 循环语句和range函数
# for 变量 in range(参数): 被执行语句    range的参数就是循环的次数
# for 后的变量是每次循环的计数,0到次数-1
# for i in range(5):
#     print(i)
#     print("Hello：",i)
# print 将输出的各种信息中间逗号分隔开，自动生成空格
# range()函数 - 产生循环计数序列
# 用法1: range(N) 产生0到N-1的整数序列 共N个   range(5) - 01234
# 用法2: range(M,N) 产生M到N-1的整数序列 共N-M个 range(2,5) - 234

# 蟒蛇绘制
import turtle       # import 保留字引入一个绘图库：turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range (4):
    turtle.circle(40,80)
    turtle.circle(-40, 80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()

# Z字形
turtle.left(45)
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)

# 叠边形绘制
import turtle as t
t.pensize(2)
for i in range(9):
    t.fd(150)
    t.left(80)  #720/9

# 六边形绘制
# 笨。。
turtle.fd(50)
turtle.right(60)
turtle.fd(50)
turtle.right(60)
turtle.fd(50)
turtle.right(60)
turtle.fd(50)
turtle.right(60)
turtle.fd(50)
turtle.right(60)
turtle.fd(50)
turtle.done()
# 聪明。。
import turtle as t
t.pensize(2)
for i in range(6):
    t.fd(150)
    t.left(60)

# 风车
# 笨。。
import turtle as t
t.pensize(3)
t.seth(-90)
for i in range(4):
    t.fd(150)
    t.right(90)
    t.circle(-150,45)
    t.right(90)
    t.fd(150)
    t.left(135)
t.done()
# 聪明。。
import turtle as t
t.pensize(2)
for i in range(4):
    t.seth(90*i)
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0,0)
t.done()

