def while_loop(numbers,num,d):
    i = 0
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + d
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

def for_loop(numbers,num,d):
    i = 0
    for i in range(0,num,d):
        print(f"At the top i is {i}")
        numbers.append(i)

        #i = i + d
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")



numbers = []
num = 6
d = 2
#while_loop(numbers,num,d)
for_loop(numbers,num,d)
print("The numbers:")

for num in numbers:
    print(num)