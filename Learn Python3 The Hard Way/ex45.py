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
class Role(object):

    def __init__(self,person,blood=0):
        self.person = person
        self.blood = blood

    avoid_num = 0

    def get_blood(self, volume):
        self.current_blood = volume
        self.total_volume = volume

    def damage(self, value):
        self.damage = value

    def under_attack(self, value):
        self.current_blood = self.current_blood - value

    def skill(self, number):

        if (number == '1'):
            self.back_home()

        elif (number == '2'):
            attack = self.attack()
            return attack

        elif (number == '3'):
            self.avoid()

        else:
            return 'WrongNum'

    def back_home(self):
        self.current_blood = self.total_volume
        # 对方继续进攻两次

    def attack(self):
        return self.damage

    def avoid(self):
        self.avoid_num += 1

    def death(self):
        print(f"玩家{self.person.name}死亡！")
        print("游戏结束！")

    def monitoring(self):
        # 是不是应该在每次检测的时候打印阵营当前状态
        print(f"{self.person.name}当前英雄血量为{self.current_blood}/{self.total_volume}  水晶塔血量为xx/xx")

        if (self.current_blood == 0):
            self.death()
        # 检测塔掉没了没

        if (self.avoid_num == 3):
            pass  # 塔掉血当前的20%

        # 监控躲避次数
        elif (self.avoid_num == 3):
            pass  # 水晶塔掉血当前20%


class Tank(Role):

    pass

class Assassin(Role):

    pass

class Shooter(Role):

    pass

class Mage(Role):

    contral_skill = False

    def skill(self,number):

        if (number == '1'):
            self.back_home()

        elif (number == '2'):
            attack = self.attack()
            return attack

        elif (number == '3'):
            self.avoid()

        else:
            print("技能编码输入错误！")

    def modify_avoid_num(self,num):
        self.avoid_num = self.avoid_num + num

    def get_contral_status(self):
        return self.contral_skill

    def set_contral_status(self,status):
        self.contral_skill = status


class Additive(object):

    def __init__(self,person):
        self.person = person
        self.person.attack =  0
        self.person.recover = 0

    def add(self,attack=0,recover=0):
        self.person.attack = self.person.attack + attack
        self.person.recover = self.person.recover + recover

class Operation(object):


    def __init__(self,person):
        self.person = person
        self.role = Role(self.person)

    def determine_role(self,number):

        if (number == '1'):
            print(f"{self.person.name}You are a tank.")
            self.role = Tank(self.person)
            self.role.get_blood(1000)
            self.role.damage(50)

        elif (number == '2'):
            print("You are a assassin.")
            self.role = Assassin(self.person)
            self.role.get_blood(500)
            self.role.damage(100)

        elif (number == '3'):
            print("You are a shooter.")
            self.role = Shooter(self.person)
            self.role.get_blood(500)
            self.role.damage(100*2)

        elif (number == '4'):
            print("You are a mage.")
            self.role = Mage(self.person)
            self.role.get_blood(500)
            self.role.damage(200)

        elif (number == '5'):
            print("You are a auxiliary.")
        else:
            print("角色编码输入错误！")
            return 'WrongNum'

        return self.role

    def use_skill(self,role,skill):
        role.monitoring()
        if(skill == '2'):
            if(role.__class__.__name__ == 'Mage'):

                lable = True
                if(role.get_contral_status() == True):
                    attack = role.skill(skill)
                    lable = False
                    role.set_contral_status(False)

                while lable:
                    flag = input("Mage有两种技能，控制（0），攻击（1），请输入：")
                    if(flag == '0'):
                        print("对方以被控制不能使用技能。")
                        role.modify_avoid_num(-1)
                        role.skill('3')
                        role.set_contral_status(True)
                        return 'SkipSkill'
                    elif(flag == '1'):
                        lable = False
                        attack = role.skill(skill)/2

                    else:
                        print("Mage技能输入错误,请重新输入！")
                        lable = True

            else:
                attack = role.skill(skill)

            print(f"攻击输出{attack}能量")
            return attack
        else:
            result = role.skill(skill)
            if(skill == '3'):
                print(f"{role.person.name}规避次数：{role.avoid_num}")
            if(result == 'WrongNum'):
                print("技能编码输入错误，请重新输入！")
                return 'WrongNum'



    def suffer_skill(self,role,attack):
        role.under_attack(attack)

class Person(object):

    def __init__(self,ID,name):
        self.ID = ID
        self.name = name
        self.addn = Additive(self)

    def additive(self,attack,recover):
        self.addn.add(attack,recover)

class Enemy(Person):

    def choose(self):
        print("role:tank(1),assassin(2),shooter(3),mage(4),auxiliary(5)")
        number = input("please input your number:")
        return number

class Onemy(Person):

    def choose(self):
        print("role:tank(1),assassin(2),shooter(3),mage(4),auxiliary(5)")
        number = input("please input enemy's number:")
        return number

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


