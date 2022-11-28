class Hero():
    """"Clas of hero"""
    def __init__(self,name,level,race):
        """"Initiale hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        """" Print parametr of hero"""
        discription = (self.name + " level is:" + str(self.level) + " race is:" \
                      + self.race + " Health of hero: "+str(self.health)).title()
        print (discription)
    def level_up(self):
        """Upgrade level"""
        self.level+=1

    def move(self):
        """"Move print"""
        print ("Hero " + self.name + " is moving...")
    def set_health(self,health):
        self.health=health

class SuperHero(Hero):
    """Super Hero"""
    def __init__(self,name,level,race,magic_level):
        """initial Super Hero"""
        super().__init__(name,level,race)
        self.magic_level = magic_level
        self.magic=100

    def makemagic (self):
        """Make magic"""
        self.magic-=10

    def show_hero(self):
        discription = (self.name + " level is:" + str(self.level) + " race is:" \
                       + self.race + " Health of hero: " + str(self.health)).title()\
                        + " magic is: " + str(self.magic)
        print(discription)