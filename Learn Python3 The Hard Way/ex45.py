"""
就编辑一个《王者荣耀1v1墨家机关道》吧，我爱玩这个，虽然不是王者，不过到王者只是时间问题。。。。= ，=
邀请一个好友与你1v1 pk，首先你选择角色，然后，对方选择角色(双方不能选择同一种英雄)。
双方进入战场，随机选择谁进行第一次攻击，玩家依次释放技能，直到某一方死去，游戏结束。
双方均拥有一座水晶塔，任一方高地塔血量为0，游戏结束。

角色分为：坦克，刺客，射手，法师，辅助。物种类别，每种类别有侧重的技能。
坦克：血量厚，输出低。
刺客：血量薄，高输出。
射手：血量薄，高输出，高攻速（连续两次攻击）。
法师：血量薄，高输出，附加控制技能（对方停止攻击一次）
辅助：血量中等厚度，输出低，可一定时间内回复自身总血量的20%。
角色总技能：使用技能（攻击、控制、回家）、躲避（躲避三次，水晶塔掉血当前量的20%）。
回家：玩家回家，对方攻击高地塔（使用三次技能攻击水晶塔）。回家的玩家满血复活。

第一版存在问题：
回家、铭文加成、辅助、塔还未编辑
法师放控制技能仍然会受到上一次攻击同等力的攻击，法师控制技能控制有问题不合理

"""

from King import *
#测试
user1 = Enemy('11111','gg')
user1.additive(10,100)
user2 = Onemy('22222','mm')
user2.additive(30,40)

num = user1.choose()
user1_role = Operation(user1).determine_role(num)
num = user2.choose()
user2_role = Operation(user2).determine_role(num)

result_oneself = None
result_enemy = None
flag = 0  #使用flag控制循环，flag为0自己可以发动技能，flag为1敌人可以发动技能。flag为2自己可以发动敌人不可以，flag为3敌人可以自己不可发动

while True:
    if(flag == 2):
        flag = 0
    while flag == 0:  #输入错误编号重新进入循环
        oneself_num = input(f"回家(1),进攻（2），躲避（3）{user1.name}请发动技能：")
        if (oneself_num != '3'):
            if (result_enemy != None):
                Operation(user1).suffer_skill(user1_role, result_enemy)
        result_oneself = Operation(user1).use_skill(user1_role,oneself_num)
        if(result_oneself != 'WrongNum'):  #‘WrongNum’输入错误编号
            flag = 1
        if(result_oneself == 'SkipSkill'):  #'SkipSkill'跳过一次技能
            flag = 2

    if(flag == 3):
        flag = 1
    while flag == 1:
        enemy_num = input(f"回家(1),进攻（2），躲避（3）{user2.name}请发动技能：")
        if(enemy_num != '3'):
            if(isinstance(result_oneself,int)):
                Operation(user2).suffer_skill(user2_role,result_oneself)
        result_enemy = Operation(user2).use_skill(user2_role,enemy_num)
        if(result_enemy != 'WrongNum'):
            flag = 0
        if (result_enemy == 'SkipSkill'):
            flag = 3


