print(1 == 3 and False)#逻辑与
print("- - - - - - - - - - - - - - - - - - - - ")
with open("ex15_sample.txt","r") as f:#和with结合使用，主要用于文件的读写操作，省去了关闭文件的麻烦。
    print(f.read())
import traceback as a#导入模块是对模块进行重命名。
try:
    while 1/0 < 0:
        print(True)
except Exception as e:
    print(f"e={e}")#和except组合使用，将捕获到的异常对象赋值给e。
    a.print_exc()
print("- - - - - - - - - - - - - - - - - - - - ")
assert 1==2,'1 不等于 2' #断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况
print("- - - - - - - - - - - - - - - - - - - - ")