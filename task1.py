'''
Created on 2022/10/14

@author: t20cs040
'''
import random

a = random.randrange(3)
b = random.randrange(3)

def howHand(n):
    if n==0:
        return("グー")
    elif n==1:
        return("チョキ")
    else:
        return("パー")
    
print("Aの手:",howHand(a)," v.s. Bの手:",howHand(b))

if a==b:
    print("→引き分け")

elif a==0 and b==1 or a==1 and b==2 or a==2 and b==0:
    print("→Aの勝ち")

else:
    print("→Bの勝ち")






