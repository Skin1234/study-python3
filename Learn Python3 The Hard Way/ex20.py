#fileObject.readline(size)一行行按顺序读取
#fileObject.seek(offset[, whence])方法用于移动文件读取指针到指定位置。 offset -- 开始的偏移量，也就是代表需要移动偏移的字节数。whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
#readline() 里面的代码能够扫描文件的每个字节，当它发现一个 \n 字符，它就会停止扫描这个文件，然后回到它发现的地方。文件 f 就负责在每次调用 readline() 之后维持文件的当前位置，以此来保证它能阅读到每一行。
#输出结果隔行，readline() 函数返回文件中每行最后的 \n 。又在 print 函数的结尾加上一个 end = " " 来避免给每行加上两个 \n 。

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)#fileObject.seek(offset[, whence])方法用于移动文件读取指针到指定位置。


def print_a_line(line_count, f):#不能跳行读取
    print(line_count, f.readline())#fileObject.readline(size)用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#print(current_file.tell())#读取文件指针位置
rewind(current_file)#读取完文件后光标会在文件的最后

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
