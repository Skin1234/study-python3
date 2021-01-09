things = ['a','b','c','d']
print(things[1])

things[1] = 'z'
print(things[1])

print(things)

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = "SF"#直接赋值会添加到字典末尾
print(stuff['city'])

print(stuff)

stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
print(stuff[2])
print(stuff)

del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)

states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#添加
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#输出
print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#字典之间操作
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#获取打印字典内容
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

#get()获取字典内容
print('-' * 10)
state = states.get('Texas')#没有返回None
if not state:
    print("Sorry, no Texas.")


city = cities.get('TX', 'Does Not Exist')#获取‘TX'的值，如果没有，返回第二个参数内容
print(f"The city for the state 'TX' is: {city}")