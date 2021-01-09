#def创建函数
#python使用缩进表示函数作用区域


def print_two(*args):#args这是告诉 Python 取所有的参数给函数，然后把它们放在 args 里放成一列
    arg1,arg2 = args
    print(f"arg1: {arg1},arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_one(arg1):
    print(f"arg1: {arg1}")


def print_none():
    print("I got nothin.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
