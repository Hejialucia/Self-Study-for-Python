# Python基本语法元素
# 语法知识点：
# 1. 整数类型
# pow(x,y)函数:计算x的y次方; pow(2,power(2,15))
# 四种进制表示形式:十进制;二进制0b/0B开头(0b010);
#                八进制0o/0O开头(0o010);十六进制0x/0X开头(0x010)
# 2. 浮点数类型
# 浮点数间运算存在不确定尾数 0.1 + 0.2 == 0.3 (False)
# round(x,d)函数:对x四舍五入，d是小数截取位数  round(0.1+0.2, 1)  == 0.3 (True)
# 浮点数可以采用科学计数法，使用e/E作为幂的符号 <a>e<b> 表示 a*10的b次方
# 3. 复数类型  a+bj称为复数，a是实部，b是虚部
# z = 1.23e - 4 + 5.6e + 89j   z.real获得实部1.23e - 4     z.image获得虚部5.6e + 89
# 4.数值运算操作符
# x/y:产生浮点数  x//y:整除得整数   x % y:取余数
# x ** y: y是整数时，幂运算，x的y次方，相当于pow(x,y)函数; y是小数时，开方，10**0.5表示根号10
# 二元操作符有对应的增强赋值操作符  x=x op y
# x += y ; x -= y ; x *= y ; x /= y ; x //= y ; x %= y ; x **= y
#  整数 > 浮点数 > 复数    123+4.0=127.0
# 5.数值运算函数
# abs(X): x的绝对值 abs(-10.01) - 10.01
# divmod(x,y): 商余 (x//y,x%y) divmod(10,3) - (3,1)
# pow(x,y[,z]): 幂余 (x**y)%z pow(3,pow(3,99),10000) - 4587
# round(x,[,d]) 四舍五入，d是保留位数默认0  round(-10.123,2) - -10.12
# max(x1,x2...xn) 和 min(x1,x2...xn) 最大值最小值
# int(x) int(1.23) - 1; int("1.23") - 1
# float(x) float(12) - 12.0; float("1.23") - 1.23
# complex(x) complex(4) - 4+0j

# 天天向上力量
# 1. 千分之一的力量
# 1.001的365次方   0.999的365次方
dayup = pow(1.001, 365)
daydown = pow(0.999,365)
print("向上:{:.2f}, 向下:{:.2f}".format(dayup,daydown))
# 2. 千分之五和百分之一的力量
# 笨。。
dayup = pow(1.005, 365)
dayup1 = pow(1.01, 365)
daydown = pow(0.995, 365)
daydown1 = pow(0.99, 365)
print("向上少:{:.2f}, 向下少:{:.2f}".format(dayup,daydown))
print("向上多:{:.2f}, 向下多:{:.2f}".format(dayup1,daydown1))
# 聪明。。
dayfactor = 0.005
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor,365)
print("向上:{:.2f}, 向下:{:.2f}".format(dayup,daydown))
# 3. 工作日的力量(平时进步，周末退步)
dayup = 1.0
daynormal = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup * (1 - daynormal)
    else:
        dayup = dayup * (1 + daynormal)
print("工作日向上:{:.2f}".format(dayup))
# 4. 工作日努力到什么水平可以和每天努力1%结果一样？
def dayUP(df):      #def 用于定义函数; df占位
    dayup = 1
    for i in range (365):
        if i % 7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.8:
    dayfactor += 0.001
print("工作日的努力程度是:{:.3f}".format(dayfactor))

# 字符串类型及操作
# 1. 索引和切片:使用[]获取字符串中的一个或多个字符
# 索引:返回字符串中单个字符     <字符串>[M]    "今天星期"[2]; TempStr[-1]
# 切片:返回字符串中一段字符子串   <字符串>[M:N]  "今天温度"[7:19]; TempStr[0:-1]
# 切片高级用法: <字符串>[M:N] 可缺M或N
#             <字符串>[M:N:K] 根据步长K对字符串切片 "0123456789"[1:8:2] - 1357 (从1开始到8之前步长2)
#             <字符串>[::-1] 倒序 "0123456789"[::-1] - "9876543210"
# 2. 转义符 \
# 转义符表达特定字符的本意 \之后的字符当作字符本意理解   "周五(\")" - 周五(")
# 转义符组合     "\b"回退  "\n"换行(光标移动到下行首)  "\r"回车(光标移动到本行首)
# 3. 字符串操作符: 由0个或多个字符组成的有序字符序列
# x + y ~ 连接两个字符串x和y
# n * x 或 x * n ~ 复制n次字符串x
# x in s ~ 如果x是s的子串，返回True，否则返回False

# 获取星期字符串
# 方法一
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
weekId = eval(input("请输入星期数字："))
pos = (weekId - 1) * 3
print(weekStr[pos: pos+3])
# 稍微简单的方法二
weekStr = "一二三四五六日"
weekId = eval(input("请输入星期数字："))
print("星期"+ (weekStr[weekId-1]))

# 字符串处理函数
# len(x) eg: len("123四五六") - 6
# str(x) 任意类型x所对应的字符串形式 str(1.23) - "1.23" ; str([1,2]) - [1,2]
# hex(x) 或 oct(x) 整数x的十六进制或八进制的小写形式字符串 hex(425) - "0x1a9" ; oct(425) - "0o651"
# chr(u) u为Unicode编码，返回其对应的字符
# ord(x) x为字符，返回其对应的Unicode编码

# 十二星座
for i in range(12):
    print(chr(9800 + i), end=" ")

# 字符串的处理方法
# 方法特指<a>.<b>()函数中的<b>()
# str.lower() 或 str.upper()
# str.split(sep=None) 返回一个列表，用sep(要在str中)把str分隔
#           eg: print("Acd,B123,X".split(","))
# str.count(sub) 返回sub在str中出现的次数 "an apple".count("a") - 2
# str.replace(old,new) eg: "python".replace("n","n1k") - python1k
# str.center(width[,fillchar]) str在width居中 eg: "python".center(20,"=")
# str.strip(chars) 从str去掉左右两侧的chars eg: "= python=".strip(" =np") - "ytho"
# str.join(iter) 在iter中除最后元素外每个元素后增一个str,主要用于字符串分隔
#           eg: ",".join("1234") - "1,2,3,4"

# 字符串类型的格式化 .format()方法
# 用法1
print(("在{0}那天，我和{1}摘了{2}朵花".format("2018-1-1","C",10)))
print(("在{2}那天，我和{0}摘了{1}朵花".format("2018-1-1","C",10)))
# 用法2: 槽内部的格式 <填充> <对齐> <宽度> <,> <.精度> <类型>
print("{0:*^20}".format("HJL"))
print("{0:=>10}".format("最厉害"))
print("0:,.f".format(12345.678))
print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425))
print("{0:e},{0:E},{0:f},{0:%}".format(3.14))

# time库
# 用处: 计算机时间的表达;提供获取系统时间并格式化输出功能;提供系统级精确计时工能，用于程序性能分析
# 格式: import time
#      time.<b>()
# 三类函数: 时间获取: time()  ctime()  gmtime()
# 时间格式化: strftime()  strptime()
# 程序计时: sleep()   perf_copunter()

# 时间获取
import time
print(time.time())
print(time.ctime())
print(time.gmtime())

# 时间格式化
t =  time.gmtime()
print(time.strftime("%Y-%m-%d %B %b %A %a %H:%M:%S %I%p",t))
timeStr = '2018-01-26 12:55:20'
print(time.strptime(timeStr,"%Y-%m-%d %H:%M:%S"))

# 程序计时
# 测量时间 perf_counter()
start = time.perf_counter()
end = time.perf_counter()
print("{0:.90f}".format(eval("end-start")))
# 产生时间 sleep()
def wait():
    time.sleep(3.3)
# 当前程序休眠3.3秒

# 文本进度条
import time
scale = 10      # 文本进度条的大概宽度
print("-------Game-------")
for i in range(scale+1):
    a = '*' * i     # 字符串与整数的乘积表示字符串被重复的次数
    b = '.' * (scale - i)       #剩余进度
    c = (i/scale) * 100     #输出的百分比
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------Finish------")

# 文本进度条单行动态刷新:用打印的字符覆盖之前的字符
import time
for i in range (101):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.1)

# 完整文本进度条
import time
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))

# 文本进度条的不同设计函数
# Linear (Constant) f(x)= x
# Early Pause (Speeds up)  f(x)= x + (1-sin(x*π*2 + π/2)/-8
# Late Pause (Slows down)   f(x)= x + (1-sin(x*π*2 + π/2)/8
# Slow Wavy (Constant)  f(x)= x + sin(x*π*5)/20
# Fast Wavy (Constant)  f(x)= x + sin(x*π*20)/80
# Power (Speeds up) f(x)=
# Inverse Power (Slows down)    f(x)=
# Fast Power (Speeds up)    f(x)=
# Inverse Fast Power (Slows down)   f(x)=
# tips: 开始慢一些，后期越来越快更符合用户心理

