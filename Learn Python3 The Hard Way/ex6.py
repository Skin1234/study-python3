#"+"可以衔接两个字符串

if __name__ == '__main__':

    types_of_people = 10
    x = f"There are {types_of_people} types of people."

    binary = 'binary'
    do_not = "don't"
    y = f"Those who know {binary} and those who {do_not}"

    print(x)
    print(y)

    print(f"I said:{x}")
    print(f"I also said:'{y}'")

    hilarious = False

    joke_evaluation = "{}{}Isn't that joke so funny?!"
    print(joke_evaluation.format(hilarious,hilarious))#使用此格式输出，若参数与串中元组数不同则会报出元组下标越界得错误

    w = "This is the left side of..."
    e = "astring with a right side."

    print(w + e)