#使用pycharm给python程序传递参数 https://blog.csdn.net/counte_rking/article/details/78837028


from sys import argv

script, first, second, third= argv
if __name__ == "__main__":
    print("The script is called:", script)
    print("Your first variable is:", first)
    print("Your second variable is:", second)
    print("Your third variable is:", third)
