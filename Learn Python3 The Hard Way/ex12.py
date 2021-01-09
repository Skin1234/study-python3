#python3的inpu()不再限制输入格式，默认为字符串处理

if __name__ == "__main__":
    age = input("How old are you?")
    height = input("How tall are you?")
    weight = input("How much do you weight?")

    print(f"So,you're {age} old,{height} tall and {weight} heavy.")


    print("hahaha:",input())       //会先运行input(),然后打印