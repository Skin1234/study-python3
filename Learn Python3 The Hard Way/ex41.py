import random
from urllib.request import urlopen
import sys

def convert(snippet,phrase):
    class_name = [w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]#capitalize() 将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。count() 方法用于统计某个元素在列表中出现的次数。random.sample（）在序列中选择定长元素返回新列表
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0,snippet.count("@@@")):
        param_cout = random.randint(1,3)#随机返回1-3之间自然数
        param_names.append(','.join(random.sample(WORDS,param_cout)))

    for sentence in snippet,phrase:#两次循环，先遍历第一个列表然后遍历第二个列表
        result = sentence[:]#复制一个列表的方式(从头到尾)

        for word in class_name:
            result = result.replace("%%%",word,1)#word替换%%%，替换1次

        for word in other_names:
            result = result.replace("***",word,1)

        for word in param_names:
            result = result.replace("@@@",word,1)


        results.append(result)

    return results#包含两个key value内容


WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []


#构建字典
PHRASES = {
    "class %%%(%%%):":"Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :"class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, call it with params self @@@.",
    "***.*** = '***'":"From *** get the *** attribute and set it to '***'."
}

#判断输入参数是否为english
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASW_FIRST = True
else:
    PHRASE_FIRST = False

#urlopen()获取链接页面并读取内容到WORDS
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding="utf-8"))

try:
    while True:
        snippets = list(PHRASES.keys())#keys()返回一个dict_keys对象,返回的是字典所有的键
        random.shuffle(snippets)#将列表所有元素随机排序

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question,answer = convert(snippet,phrase)#替换word

            if PHRASW_FIRST:
                question,answer = answer,question#将value作为问题，key进行解答

                print(question)

                input(">")
                print(f"ANSWER:{answer}\n\n")

except EOFError:
    print("\nBye")