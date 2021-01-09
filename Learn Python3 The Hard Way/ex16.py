from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURE.")

input("?")

print("Opening the file...")
target = open(filename, 'w') #打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件

print("Truncating the file.Goodbye!")
#target.truncate() #清空

print("Now I'm going to ask you for three line.")

line1 = input("line 1:")#读取
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(line1)#写入文件
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#附加题3
line = line1 + '\n' + line2 + '\n' + line3 + '\n'
target.write(line)

print("And finally, we close it.")
target.close()#关闭文件

#附加题2
file = open(filename)
print(file.read())
file.close()