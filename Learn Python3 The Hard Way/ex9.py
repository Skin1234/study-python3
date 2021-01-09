#print函数内使用三个引号的内容原样打印


if __name__ == "__main__":
    days = "Mon The Wed Thu Fri Sat Sun"
    months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

    print("Here are the days:",days)
    print("Here are the months:",months)

    print("""
    There's something going on here.
    With the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.
    """)