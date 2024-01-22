import os
import entities as en
import battle_mechanics as bm
import math
import asci_art as ac
import time
import msvcrt
import random


def treasureLoc():
    list=[]
    for i in range(-50,50):
        list.append(i)
    listx=random.sample(list,100)
    listy=random.sample(list,100)
    for i in range(3):
        temp1=random.sample(list,100)
        temp2=random.sample(list,100)
        listx.extend(temp1)
        listy.extend(temp2)
    listx.append(5)
    listy.append(5)
    return listx,listy

def isTreasure(a,listx,listy):
    
    check=False
    for i in range(len(listx)):
        if a.x == listx[i] and a.y == listy[i]:
            check = True
            del listx[i]
            del listy[i]
            break

    if check:
        ac.draw()
        print("\nYou have found treasure!")
        time.sleep(1)
        print("You get 200 gold and 200 magic")
        a.gold=a.gold+200
        a.magic=min(a.magic+200,a.maxmagic)
        input("\n>")

def move(movement, a):
    if movement == b'w':
        a.y += 1
    elif movement == b's':
        a.y -= 1 
    elif movement == b'a':
        a.x -= 1
    elif movement == b'd':                 
        a.x += 1
    elif movement == b'q':
        a.displayInventory()


def disto(a):
    miniboss1_notmet=True
    miniboss2_notmet=True
    miniboss3_notmet=True
    miniboss4_notmet=True
    miniboss_beaten_count=0
    dist = int(round(math.sqrt((a.x**2) + (a.y**2))))
    if dist>25 and miniboss1_notmet==True:
        bm.mb1Encounter(a)
        miniboss_beaten_count+=1
        miniboss1_notmet=False
    if dist>45 and miniboss2_notmet==True:
        bm.mb2Encounter(a)
        miniboss_beaten_count+=1
        minboss2_notmet=False 
    if dist>65 and miniboss3_notmet==True:
        bm.mb3Encounter(a)
        miniboss_beaten_count+=1
        miniboss3_notmet=False
    if dist>75 and miniboss4_notmet==True:
        bm.mb4Encounter(a)
        miniboss_beaten_count+=1
        miniboss3_notmet=False
    if dist>80 and miniboss_beaten_count==4:
        bm.jesusEncounter(a)
            
    
    return dist

def showLogo():
    os.system('cls')
    print("\n\n")
    print(ac.art3)
    time.sleep(1)

def showGuy():
    os.system('cls')
    print("\n\n")
    print(ac.art4)
    time.sleep(1)

def play(a):
    loc=treasureLoc()
    listx,listy=loc
    while True:
        os.system('cls')
        print(" " * 15, end=' ')
        ac.draw()
        print(" " * 15 + f"   X : {a.x}  Y : {a.y}  distance from home: {disto(a)} ")
        print(" " * 15, end=' ')
        ac.draw()
        print("\n\n\n")
        ac.draw()
        print(f"  enter direction you want to move")
        ac.draw()
        movement = msvcrt.getch()
        move(movement, a)
        isTreasure(a,listx,listy)
        os.system('cls')
        if bm.isEnemy():
            p = bm.getEnemyType()
            if p=='j':
                bm.jesusEncounter(a)
            else:    
             enemy = en.createEnemyObject(p)
             en.battle(a, enemy)

if __name__ == "__main__":

    print("\n\n\n\n")
    ac.draw()
    print("            What is your name ")
    ac.draw()
    name = input("\n\n> ")
    a = en.player(name)
    en.playerWelcome(a)
    showLogo() 
    play(a)
