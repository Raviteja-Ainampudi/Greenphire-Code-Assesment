# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 12:10:03 2016

@author: RAVI TEJA
"""
import collections
import random
from random import randint

x = int(raw_input("Enter Number of Players: "))
a = []

#Obatining the name and inputs from the players
while x > 0:
    print " "
    x -= 1
    b = []
    first_name = raw_input("Enter your first name:")
    b.append(first_name)
    last_name = raw_input("Enter your last name:")
    b.append(last_name)
    flag = 1
    while flag == 1:
        select_1 = int(raw_input("select 1st # (1 thru 69):" ))
        if select_1 < 70:
                b.append(select_1)
                flag = 2
                
    flag = 1   
    while flag == 1:
        select_2 = int(raw_input("select 2nd # (1 thru 69 excluding [%s]): " %b[2]))
        if select_2 < 70 and select_2 != b[2]:
                b.append(select_2)
                flag = 2

    flag = 1   
    while flag == 1:
        select_3 = int(raw_input("select 3rd # (1 thru 69 excluding [%s] and [%s]): " %(b[2],b[3]) ))
        if select_3 < 70 and select_3 != b[2] and select_3 != b[3]:
                b.append(select_3)
                flag = 2
    
    flag = 1   
    while flag == 1:
        select_4 = int(raw_input("select 4th # (1 thru 69 excluding [%s], [%s] and [%s]):  " %(b[2],b[3],b[4]) ))
        if select_4 < 70 and select_4 != b[2] and select_4 != b[3] and select_4 != b[4]:
                b.append(select_4)
                flag = 2   
    
    flag = 1   
    while flag == 1:
        select_5 = int(raw_input("select 5th # (1 thru 69 excluding [%s], [%s], [%s] and [%s])  " %(b[2],b[3],b[4], b[5]) ))
        if select_5 < 70 and select_5 != b[2] and select_5 != b[3] and select_5 != b[4] and select_5 != b[5]:
                b.append(select_5)
                flag = 2 
    
    b.append("Powerball:")
    
    flag = 1
    while flag == 1:
        select_6 = int(raw_input("select Power Ball # (1 thru 26): " ))
        if select_6 < 27:
                b.append(select_6)
                flag = 2
    a.append(b)

for i in range(len(a)):
    print " "
    for j in range(9):
        print a[i][j],

final_powerball_6 = []
for i in range(len(a)):
    final_powerball_6.append(a[i][8])

a1 = final_powerball_6
x1 = [[item,count] for item, count in collections.Counter(a1).items() if count > 1]
just_count = [count for item, count in collections.Counter(a1).items() if count > 1]

if len(x1) == 0:
    power_ball = random.choice(a1)
else:
    pob = []
    k = max(just_count)
    for i in range(len(x1)):
        if x1[i][1] == k:
            pob.append(x1[i][0])
    power_ball = random.choice(pob) #Winning 6th Power_ball number
print " "

#Choosing the winning first 5 Power_ball numbers
element_inp = []
for i in range(len(a)):
    element_inp.append(a[i][2:7])
a11 = []
for i in range(len(element_inp)):
    for j in range(5):
        a11.append(element_inp[i][j])

x11 = [[item,count] for item, count in collections.Counter(a11).items() if count > 1]
just_count11 = [count for item, count in collections.Counter(a11).items() if count > 1]

power_mat = []
if len(x11)== 0:
    while len(power_mat) < 5:
        new = randint(1,69)
        if new not in power_mat:
            power_mat.append(new)
else:
    if len(x11) <= 5:
        for i in range(len(x11)):
            power_mat.append(x11[i][0])
    else:
        while len(power_mat) <5:
            sor_count = (just_count11)
            v = [item for item, count in collections.Counter(a11).items() if count == max(sor_count)]
            new1 = random.choice(v)
            if new1 not in power_mat:
                power_mat.append(new1)
                del sor_count[sor_count.index(max(sor_count))]
            
while len(power_mat) < 5:
    padd = randint(max(power_mat),69)
    if padd not in power_mat:
        power_mat.append(padd)

final = sorted(power_mat)
final.append("Powerball:")
final.append(power_ball)

print " "
print "Powerball winning number:"
for i in range(len(final)):
    print final[i],
