#d调用format后，新的字符串会顶替原来位置上的值

if __name__ == '__main__':
    formatter = "{}{}{}{}"

    print(formatter.format(1,2,3,4))
    print(formatter.format("one","two","three","four"))
    print(formatter.format(True,False,False,True))
    print(formatter.format(formatter,formatter,formatter,formatter))
    print(formatter.format("Try your","Own text here","Maybe a poem","Or a song about fear"))