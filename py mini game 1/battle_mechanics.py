import random 
import time 
import entities as en
import os 
import enemy_pop as ep
import asci_art as ac



def isCritical(a):
    prob=10+int(round(a.luck*0.1)) 
    t=random.randint(1,100)
    if t<=prob:
        return True
    else:
        return False
    
def isCriticalE(a):
    prob=10-int(round(a.luck*0.1)) 
    t=random.randint(1,100)
    if t<=prob:
        return True
    else:
        return False
    
       

def isHit(a):
    prob=80+int(round(a.luck*0.2)) 
    t=random.randint(1,100)
    if t<=prob:
        return True
    else:
        return False
    

def isDoubleGold(a):
    prob=10+int(round(a.luck*0.2)) 
    t=random.randint(1,100)
    if t<=prob:
        return True
    else:
        return False

def outDmgFlux(dmg,a):
    pchange=int(round(0.1*dmg))
    nchange=int(round(-0.08*dmg))
    luck_change=int(round(0.01*a.luck))
    t=random.randint(nchange,pchange)+luck_change
    finaldmg=dmg+t
    return finaldmg

def goldFlux(gold,a):
    pchange=int(round(0.1*gold))
    nchange=int(round(-0.08*gold))
    luck_change=int(round(0.01*a.luck))
    t=random.randint(nchange,pchange)+luck_change
    finalgold=gold+t
    return finalgold
   


def getEnemyType():
  flag=random.randint(0,100)
  if(flag>=0 and flag<=40):
   return 'w'
  
  elif(flag>40 and flag<=66):
    return 'gi'
  
  elif(flag>66 and flag<=83):
    return 'f'
  
  elif(flag>83 and flag<=91):
   return 'go'
  
  elif(flag>91 and flag<=96):
    return 'd'
  
  elif(flag>96 and flag<=100):
    return 'j'

def isEnemy():
   t=random.randint(1,100)
   if t>75:
      return True
   

def mb1Encounter(a):
    pass

def mb2Encounter(a):
    pass

def mb3Encounter(a):
    pass
 
def mb4Encounter(a):
    pass

def jesusEncounter(a):
   os.system('cls')
   ep.popMessage('j')
   ac.draw()
   print("\n You have encountered a warrior deity !\n")
   ac.draw()
   input("\n>")
   os.system('cls')
   ch=input("Do you wish to give up all your gold ?\ny/n \n>")
   if ch=='y':
      print("\nYour sacrifice has gotten you blessing of the warrior spirit !")
      time.sleep(2)
      a.gold=0
      print()
      ac.draw()
      print("\nYour sword has been imbued with heavenly energy \n Its  attack power has been increased by 100\n")
      ac.draw()
      time.sleep(3.5)
      a.sword_dmg+=100
      a.displayInventory()

   else:
      print("The warrior deity respects your commitment to your mission\nYour luck has been icreased by 10")  
      a.luck+=10
      time.sleep(3)
      a.displayInventory()

   os.system('cls')
   ac.draw() 
   print("Three doors open before you...")
   print("The door of life is guarded by two dragons ")
   print("The door of chaos is guarded by 4 golems ")
   print("The third door takes you back to your quest")
   ac.draw()
   time.sleep(1)
   ch1=input("\n which do you chose to go to 1/2/3\n>")
   if ch1=='1':
      enemy=en.createEnemyObject("d")
      en.battle(a,enemy)
      enemy1=en.createEnemyObject("d")
      en.battle(a,enemy1)
      ac.draw()
      print("Your max health has been increased by 100! ")
      ac.draw()
      time.sleep(2)
      a.maxhealth+=100
      a.health=a.maxhealth
      a.displayInventory()

   elif ch1=='2':
      for i in range(4):
         enemy=en.createEnemyObject('go')
         en.battle(a,enemy)
      print("Your max magic has been increased by 100")
      a.maxmagic+=100
      a.magic=a.maxmagic
      time.sleep(2)
      a.displayInventory()

   elif ch1=='3':
      print("You chose the cowards path!")   

   if a.kills>50:
      ac.draw()
      print("You unlocked the heavenly smite spell!")   
      a.spellkKey=5
      ac.draw()
      
        


def dungeon1(a):
   pass

def dungeon2(a):
   pass

def dungeon3(a):
   pass

if __name__=="__main__":
 a=en.player("bruv")
 jesusEncounter(a)

