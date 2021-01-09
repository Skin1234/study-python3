#整理所学内容

'''
此部分为多行注释
'''
#接受输入控制在RUN->Edit Configurations->Paremeter(参数之间用空格间隔)
from sys import argv
script, first, second, third, filename= argv#运行时传参赋值给前面的变量

#输出的参数可以计算
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

#带参输出
car = 100
print(f"一共有{car}辆车车")

#带参数的串赋给变量
x = f"一共有{car}辆\n"
print(x, car)

#字符串中用{}占位，用format传参
#三引号包含多行串
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}{}"
print(joke_evaluation.format(hilarious,car))
formatter = "aaa{} {} {} {}"
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))

#字符串相加
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)

#用\转义符号
backslash_cat = "I'm \\ a \\ cat."
print(backslash_cat)

#在每一个打印行末尾放一个 end=' ' ，是为了告诉 print 不要另起一行。
print("How old are you?", end=' ')
age = input()
print(f"So, you're {age} old.")

#input()打印完不换行接受输入
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
print(f"So, you're {age} old, {height} tall and {20} heavy.")


print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")#重复输入
print("If you do want that, hit RETURN.")
input("?")
print("Opening the file...")



file = open(filename, "r+")#读写
content = file.read()#用读打开文件读出内容

print(f"光标位置：{file.tell()}")#获取光标位置
print(f"content:\n{content}")
file.seek(5)
file.truncate()#文件以文本形式打开文件不会被截取：https://blog.csdn.net/weixin_39630484/article/details/86032024
print(f"光标位置：{file.tell()}")
content_again = file.read()
print("content:\n",content_again)


target = open(filename, 'w')#用写打开文件赋值给文件对象
#target.truncate()#用于截断文件，如果指定了可选参数 size，则表示截断文件为 size 个字符。 如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除。
line1 = input("line 1: ")
target.write(line1)
target.write("\n")
target.close()


def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(filename)
print("First let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

