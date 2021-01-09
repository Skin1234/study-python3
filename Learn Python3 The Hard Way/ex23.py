import sys
script, encoding, errors = sys.argv
#递归遍历整篇文本
def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
#<===> 左边是 Python 用来存储字符串的数字字节或者“原始”（raw）字节
#输出中 b' ' 是为了告诉 Python 这是“字节”（bytes）。
# 这些原始字节之后被“加工”（cooked）然后显示在右边，以便让你看到你的终端呈现出来的真正的字符。
def print_line(line, encoding, errors):
    next_lang = line.strip()#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    raw_bytes = next_lang.encode(encoding, errors = errors)#编码为二进制
    cooked_string = raw_bytes.decode(encoding, errors = errors)#解码为原始字符

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, errors)
