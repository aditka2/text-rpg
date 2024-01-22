import os 
import random
import time
import enemy_pop as ep
import asci_art as aa
import battle_mechanics as bm
import asci_art as ac


class player:

    bomb_dmg=100
    arrows_dmg=80
    spell_dmg=150
    potion_val=100
    
    def __init__(self,name):

        os.system('cls')
        self.name=name
        self.health=500
        self.maxhealth=500
        self.magic=1000
        self.maxmagic=1000
        self.sword_dmg=50
        self.sword_element=0
        self.bombs=40
        self.arrows=100
        self.revives=5
        self.gold=0
        self.potions=0
        self.spells=0
        self.spellKey=4
        self.xp=0
        self.luck=60
        self.x=0
        self.y=0
        self.dist=0
        self.kills=60


    def attack(self):
        os.system('cls')
        ac.draw()
        print("1 SLASH")
        print("2 BOMB")
        print("3 ARROWS")
        print("4 SPELL")
        ac.draw()
        ch=int(input("\nWhat do you choose to do \n\n>"))
        if(bm.isHit(self)):
            dmg=self.getDmg(ch)
            return dmg
        else:
            ac.draw()
            print("Your attack missed!")
            ac.draw()
            return 0

        


    def takeDmg(self,dmg):
        self.health=self.health-dmg

    def isAlive(self):
        if self.health>0:
            return True    
        else:
            return False

    def checkAmt(self,type):
        if type=="bomb":
            if self.bombs>0:
             return True 
            else:
                return False
        elif type=="arrows":
            if self.arrows>0:
                return True
            else:
                return False    

    def getDmg(self,ch):
        dmg=0
        if ch==1:
            dmg= self.sword_dmg
        elif ch==2:
            if(self.checkAmt("bomb")):
             self.bombs-=1
             dmg= self.bomb_dmg
            else:
                print("you do not have enough bombs ")
                time.sleep(2)
                dmg= self.attack()
        elif ch==3:
            if(self.checkAmt("arrows")):
             self.arrows-=1
             dmg= self.arrows_dmg
            else:
                print("you do not have enough arrows")
                time.sleep(2)
        elif ch==4:
            dmg= self.useSpell()
        else:
            self.attack()
        
        dmg=bm.outDmgFlux(dmg,self)
        if(bm.isCritical(self)):
            ac.draw()
            print("It is a critical hit !") 
            ac.draw()   
            dmg=int(round(dmg*(1.5)))

        return dmg    
        
    def addGold(self,loot,source):
        loot=bm.goldFlux(loot,self)
        if(bm.isDoubleGold(self)):
            ac.draw()
            print("\nYou were lucky and got double gold \n")
            ac.draw()
            loot=loot*2    
        print("\n\n")
        self.gold=self.gold+loot    
        print(f"You obatined {loot} gold from the {source}")
        input("")

    def dead(self):
        print("you have been slain ")
        if(self.revives>0):
            ch=int(input("1 Use revive  2 quit game\n\n>"))
            if(ch==1):   
                self.revives=self.revives-1
                self.health=500 
                print("you have come back from the dead")
                time.sleep(1.5)
                self.displayInventory()
                time.sleep(2)
                os.system('cls')
                print("continue fighting ")
                time.sleep(1.5)
                os.system('cls')

            elif(ch==2):
                print("thanks for playing ")
                quit()

            else:
                self.dead()    
        else:
            print("you have no revives left !")
            print("game over ")
            quit()



    def displayInventory(self):
        os.system('cls')
        print("\n\n")
        ac.draw()
        print(f"  CURRENT HEALTH : {self.health}")  
        print(f"  SWORD POWER : {self.sword_dmg}")    
        print(f"  ARROWS : {self.arrows}\n  BOMBS : {self.bombs}\n  MAGIC : {self.magic}")
        print(f"  GOLD : {self.gold}")
        print(f"  REVIVES : {self.revives}")
        ac.draw()
        print("\n\n")
        input(">")  


    def spellChoice(self):
        os.system('cls')
        print("Which spell do you want to use :")
        print("0 heal \n1 energy beam \n2 freeze\n3 incinerate \n4 meteor \n")
        while True:
         ch=input("\n> ")
         temp=ch
         if(int(temp)<=self.spellKey):
             return ch

         else:
             print("You have not unlocked this spell yet\ntry another spell ")
             return ch
        



    def useSpell(self):
        ch=self.spellChoice()
    
        if(ch=='0' and self.magic>=50):
            self.health=self.health+self.potion_val
            self.magic=self.magic-50
            return 0
        elif(ch=='1' and self.magic>=50):
            self.magic=self.magic-50
            return 150
        elif(ch=='2' and self.magic>=100):
            self.magic=self.magic-100
            return 100
        elif(ch=='3' and self.magic>=150):
            self.magic=self.magic-150
            return 250
        elif(ch=='4' and self.magic>=200): 
            self.magic=self.magic-200
            return 500  

        else:
            print("You do not have enough magic for this spell try again")
            time.sleep(1.5)
            return self.attack() 

class werewolf:

    def __init__(self):

        self.health=100
        self.maxhealth=100
        self.dmg=50
        self.item=None
        self.gold=20
        self.name="WERE-WOLF"
        self.ability="BITE"
        self.xp=50
        self.magic=30
        self.healthg=10
        ep.popMessage('w')

    def attack(self,a):
        ac.draw()
        print("WERE-WOLF ATTACKS YOU!!")
        dmg=self.dmg
        if(bm.isCriticalE(a)):
            print("Its a critical hit!")
            dmg=dmg*1.5
        ac.draw()    
        return dmg

    def takeDmg(self,dmg):
        self.health=self.health-dmg

    def isAlive(self):
        if self.health>0:
            return True
        elif self.health<=0:
            return False      

    def lootDrops(self):
        return self.gold  
    
class giant:

    def __init__(self):
        self.health=250
        self.maxhealth=250
        self.dmg=40
        self.item=None
        self.name="GIANT"
        self.ability="STOMP"
        self.gold=40
        self.xp=50
        self.magic=60
        self.healthg=30
        ep.popMessage('gi')

    def attack(self,a):
        ac.draw()
        print("GIANT ATTACKS YOU!!")
        dmg=self.dmg
        if(bm.isCriticalE(a)):
            print("Its a critical hit!")
            dmg=dmg*1.5
        ac.draw()    
        return self.dmg

    def takeDmg(self,dmg):
        self.health=self.health-dmg

    def isAlive(self):
        if self.health>0:
            return True
        elif self.health<=0:
            return False      

    def lootDrops(self):
        return self.gold     

class firedemon:

    def __init__(self):
        self.health=200
        self.maxhealth=200
        self.dmg=100
        self.item=None
        self.gold=100
        self.xp=200
        self.name="FIRE DEMON"
        self.ability="HELL FIRE"
        self.magic=100
        self.healthg=60
        ep.popMessage('f') 

    def attack(self,a):
        ac.draw()
        print("FIRE DEMON ATTACKS YOU!!")
        dmg=self.dmg
        if(bm.isCriticalE(a)):
            print("Its a critical hit!")
            dmg=dmg*1.5
        ac.draw()    
        return dmg

    def takeDmg(self,dmg):
        self.health=self.health-dmg

    def isAlive(self):
        if self.health>0:
            return True
        elif self.health<=0:
            return False      

    def lootDrops(self):
        return self.gold      

class golem:

    def __init__(self):
        self.health=400
        self.maxhealth=400
        self.dmg=180
        self.item=None
        self.gold=400
        self.xp=500
        self.name="GOLEM"
        self.ability="BOULDER SLAM"
        self.magic=150
        self.healthg=100
        ep.popMessage('go')  

    def attack(self,a):
        ac.draw()
        print("GOLEM ATTACKS YOU!!")
        dmg=self.dmg
        if(bm.isCriticalE(a)):
            print("Its a critical hit!")
            dmg=dmg*1.5
        ac.draw()    
        return dmg

    def takeDmg(self,dmg):
        self.health=self.health-dmg

    def isAlive(self):
        if self.health>0:
            return True
        elif self.health<=0:
            return False      

    def lootDrops(self):
        return self.gold      
       
class dragon:

    def __init__(self):
        self.health=1000
        self.maxhealth=1000
        self.dmg=200
        self.item='lightningcrest'   
        self.gold=1000
        self.xp=1000
        self.magic=300
        self.healthg=300
        self.name="LIGHTNING DRAGON"
        self.ability="LIGHTNING STORM"
        ep.popMessage('d')  

    def attack(self,a):
        ac.draw()
        print("DRAGON ATTACKS YOU!!")
        dmg=self.dmg
        if(bm.isCriticalE(a)):
            print("Its a critical hit!")
            dmg=dmg*1.5
        ac.draw()    
        return dmg

    def takeDmg(self,dmg):
        self.health=self.health-dmg

    def isAlive(self):
        if self.health>0:
            return True
        elif self.health<=0:
            return False      

    def lootDrops(self):
        return self.gold    
   

def healthbar(a):
    
    remain_symbol='█'
    lost_symbol='░'
    bars=30
    remaining_bars= round(a.health/a.maxhealth*bars)
    losthealth_bars=bars-remaining_bars
    print("   X"+30*"="+"X")
    print(f"    {remaining_bars*remain_symbol}{losthealth_bars*lost_symbol}")
    print("   X"+30*"="+"X")

def playerbar(a):
    remain_symbol='█'
    lost_symbol='░'
    bars=30
    remaining_mbars= round(a.magic/a.maxmagic*bars)
    lostmagic_bars=bars-remaining_mbars
    remaining_bars= round(a.health/a.maxhealth*bars)
    losthealth_bars=bars-remaining_bars
    print("   X"+30*"="+"X"+"       X"+30*"="+"X")
    print(f"     {remaining_bars*remain_symbol}{losthealth_bars*lost_symbol}         {remaining_mbars*remain_symbol}{lostmagic_bars*lost_symbol}")
    print("   X"+30*"="+"X"+"       X"+30*"="+"X")


def battle(player,enemy):
 a=player
 b=enemy
 a.displayInventory()                                                                                  
 os.system('cls')                      
 loot=0
 
 while(b.isAlive()):
  ac.draw()
  print()
  print(f"   {b.name} HEALTH : {b.health}/{b.maxhealth}\n")
  healthbar(b)
  print()
  ac.draw()
  input(">")
  dmg=a.attack()
  print(f"You do {dmg} damage to the {b.name} ")
  b.takeDmg(dmg)
  time.sleep(3)
  if b.isAlive():
   os.system('cls')
   dmg=b.attack(a)
   print(f"It inflicts {dmg} with its {b.ability}")
   a.takeDmg(dmg)
   time.sleep(1)
   print("\n\n")
   print("X"+70*"-"+"X\n")
   print(f"     YOUR HEALTH {a.health}/{a.maxhealth}                   YOUR MAGIC {a.magic}/{a.maxmagic}")
   playerbar(a)
   print()
   print("X"+70*"-"+"X")
   print("\n\n")
   if a.isAlive()==False:
       os.system('cls')
       a.dead()

 if b.isAlive()==False:
     print(f"You have killed the {b.name}")
     time.sleep(2)
     loot=b.lootDrops()
     a.addGold(loot,b.name)
     print(f"\nYou recover {b.healthg} health")
     a.health=min(a.health+b.healthg,a.maxhealth)
     print(f"\nYou get back {b.magic} magic from killing the {b.name}")
     input(" ")
     

 a.displayInventory()


def createEnemyObject(p):

    enemy=None
    if p=='w':
        enemy=werewolf()
    elif p=='gi':
        enemy=giant()
    elif p=='f':
        enemy=firedemon()
    elif p=='go':
        enemy=golem()
    elif p=='d':
        enemy=dragon()

    return enemy  

def playerWelcome(a):
    os.system('cls')
    print(f"{aa.art7}\n\n\n")
    ac.draw()
    print(f" {a.name}  Welcome to Knights of Valor  \n\nyou will start with the following stats")
    ac.draw()
    time.sleep(4)
    a.displayInventory()

if __name__=="__main__":
   a=player("adit")
   p=bm.getEnemyType()
   enemy=createEnemyObject(p)
   battle(a,enemy)  


