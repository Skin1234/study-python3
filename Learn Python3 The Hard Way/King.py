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
