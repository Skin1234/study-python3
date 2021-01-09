#print(f" {变量名}")  f:format,表示告诉python3,这个字符串需要格式化，把这些变量放在这{}内可进行计算，{}内可调用函数得到返回值
#所有函数均有返回值，函数未写return,会隐含含有return None

if __name__ == '__main__':
    my_name = 'Zed A.Shaw'
    my_age = 35
    my_height = 74
    my_weight = 180
    my_eyes = 'Blue'
    my_teeth = 'White'
    my_hair = 'Brown'

    def test():
        centimeters = 1
        kilograms = 1
        inches = 30.48 * centimeters
        pounds = 0.45 * kilograms

        print(f"5inches = {5*inches}")
        print(f"10pounds = {round(10* pounds)}")#四舍五入取整

        return 1

    print(f"result is {test()}")
    print(f"Let'stalk about {my_name}.")

    print(f"He's {my_height} inches tall.")

    print(f"He's {my_weight} pounds heavy.")

    print("Actually that's not too heavy.")

    print(f"He's got {my_eyes} eyes and {my_hair} hair.")

    print(f"His teeth are usually {my_teeth} depending on the coffee.")

    total =my_age + my_height + my_weight

    print(f"If I add {my_age}.{my_height}, and{my_weight}I get {total}.")