from sys import argv

script, filename = argv

txt = open(filename) #返回的是一个文件对象

print(f"Here's your file {filename}:")
print(txt.read()) #打印文件内容

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)


print(txt_again.read())

txt_again.close()