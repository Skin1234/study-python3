
《笨方法学Python3》

在线书籍：https://www.bookstack.cn/read/LearnPython3TheHardWay/spilt.1.learn-py3.md



笔记：
ps:手敲代码，网络上有很多代码资源。代码中小游戏自制，后续有时间会升级小游戏（1v1battle）

1.#单行注释
'''
多行
注释
'''
2.coding=utf-8或者coding=gbk用来防止中文乱码
3.运算优先级：括号，指数，乘，除，加，减
4.python不需要先定义变量类型
5.print(f" {变量名}")  f:format,表示告诉python3,这个字符串需要格式化，把这些变量放在这{}内可进行计算，{}内可调用函数得到返回值
6.所有函数均有返回值，函数未写return,会隐含含有return None
7.joke_evaluation = "{}{}Isn't that joke so funny?!"
print(joke_evaluation.format(hilarious,hilarious))#使用此格式输出，若参数与串中元组数不同则会报出元组下标越界得错误
8.fat_cat = '''#变量内容为多行字符串
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
9.使用pycharm给python程序传递参数 ：RUN->Edit Configurations->Paremeter(参数之间用空格间隔)https://blog.csdn.net/counte_rking/article/details/78837028
10.在每一个打印行末尾放一个 end=' ' ，是为了告诉 print 不要另起一行。
11.input()打印完不换行接受输入
age = input("How old are you? ")
12.def print_two(*args):#args这是告诉 Python 取所有的参数给函数，然后把它们放在 args 里放成一列
    arg1,arg2 = args
    print(f"arg1: {arg1},arg2: {arg2}")
13.函数赋值的几种不同的方式：直接给它数字，或者变量，亦或是数学运算，甚至是数学运算和变量的结合。
14.fileObject.readline(size)一行行按顺序读取
15.fileObject.seek(offset[, whence])方法用于移动文件读取指针到指定位置。 offset -- 开始的偏移量，也就是代表需要移动偏移的字节数。whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
16.输出结果隔行，readline() 函数返回文件中每行最后的 \n 。又在 print 函数的结尾加上一个 end = " " 来避免给每行加上两个 \n 。
17.逐行读取文件内容的三种方法：https://blog.csdn.net/zhengxiangwen/article/details/55148287																																																																																				
18.file.truncate()#文件以文本形式打开文件不会被截取https://blog.csdn.net/weixin_39630484/article/details/86032024																																																																																																																																																																																																																																																																																							
19.列表list：一个按顺序从头到尾组成的某种东西的容器  weight = [1,2,3,4] elements = []
20.range(0,6) = [0,1,2,3,4,5]
21.对象与实例的区别[https://blog.csdn.net/qq_43317529/article/details/83038765]
22.一个桶里有鱼，三条三文鱼，其中一条叫Marry.；类：鱼、三文鱼。Marry:对象/实例。和所属关系有关。三文鱼可以是鱼的一个实例，marry可以是三文鱼的一个实例，对象属于某个类。
23.[菱形继承https://zhuanlan.zhihu.com/p/106399496]创建类继承object,适用广度优先遍历父类
24.多继承：一个子类从多个父类继承。（多个父类如果有重叠的名称会造成歧义。）如若使用python的多重继承，要理解MRO。https://note.qidong.name/2020/05/python-super-mro/
25.编码过程：过程如下：
把问题写或者划下来。
提炼出关键概念，并进行研究。
为这些概念创建一个类的层级和对象关系图。（把你所写所画的东西里面所有的名词和动词列一个表出来，然后写下它们之间是如何相互关联的）、
等类的层级结构梳理清楚之后，写一些基本的代码框架，只是一些类和它们的函数
写下这些类的代码，并测试运行。
重复和改进。
26.设计一个工程的过程。https://www.bookstack.cn/read/LearnPython3TheHardWay/spilt.48.learn-py3.md
27.python继承.隐式继承：子类继承父类内容，子类不重写。显示继承：子类继承父类并重写。既用子类又用父类：利用super调用父类。
28.代码规则[https://www.python.org/dev/peps/pep-0008/]
导入的模块名全小写，类名首字母大写无符号链接，类型变量名首字母大写无符号链接，全局变量__a__，函数名全小写用下划线链接，变量名全小写下划线链接，常量__全大写__,继承设计：公共属性无前导下划线。。。
29.ex45类互调。https://blog.csdn.net/lovemysea/article/details/73521936
30.python中各种变量https://blog.csdn.net/helloxiaozhe/article/details/79139256
40.判断实例属于哪个类https://blog.csdn.net/weixin_41010198/article/details/89359586
41.类内不宜打印东西，要打印出来打印。
42.使用setup.py安装本地包/模块。https://www.cnblogs.com/maociping/p/6633948.html
在安装目录，新建一setup.py ,编辑完内容后输入python setup.py           build python setup.py install
43.ubuntu克隆代码 git clone 源码链接
44.引用自己的代码包，每一个包必须有一个__init__.py文件，表示初始化包，必须有。python setup.py develop。
45.ubuntu 运行python 的无限循环时，使用Ctrl+d退出。
46.pycharm引用目录下文件报错https://blog.csdn.net/weixin_42613871/article/details/110545815
原因：pycharm不会将当前文件目录自动加入自己的sourse_path。
解决：右键make_directory as-->sources path将当前工作的文件夹加入source_path就可以了。
注意：Mark Directory as Sources Root 之后，如果换了一个工程文件，去打包成可执行文件时，可能会导致打包时出现问题。这时只需要在当前工程的文件夹下再次Mark Directory as Sources Root ，就可以正常打包文件了
47.python调用其他文件https://www.cnblogs.com/AmyHu/p/10654500.html
48.测试：
nose使用。https://www.cnblogs.com/liaofeifight/p/5148717.html
doctest使用。https://learnku.com/docs/pymotw/doctest-testing-through-documentation/3465
49.利用conda创建env多版本虚拟环境https://blog.csdn.net/a493823882/article/details/87888509创建：conda create -n your_env_name python=X.X 激活：source activate your_env_name 展示：conda conda env list   退出虚拟环境：conda deactivate your_env_name  删除：conda remove -n your_env_name --all   


