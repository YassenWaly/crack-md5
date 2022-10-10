import hashlib
from hashlib import *
import os
import colorama
#--------------------------------
print('''\033[1;31m
           ..-""-.. 
           / .--.  |
          / /    \ |
          | |    | |
          | |.-""-.|
         ///`.::::.`|
        ||| ::/  \:: ;
        ||; ::\__/:: ;
         ||\ '::::' /
 \033[1;32m    md5 \033[1;31m `=':-..-'` \033[1;32m Dragon
''')
print('\033[1;33m')
print('1- check hash\n2- crack md5\n3- encode md5')
print("\033[1;36m")
inp1=input(" Enter ( 1 or 2 or 3 ) : ")
if inp1=="1":
    inp2=input("Enter Hash : ")
    num=len(inp2)
    #print(a)
    if num==32:
        print("\033[1;32m hash : md5")
    else:
        print("\033[1;31m Not md5 !!")
if inp1=="2":
    hash=input(" Enter Hash : ")
    file=input("Write File Nme : ")
    with open(file , mode='r') as f :
        for line in f :
            line = line.strip()
            if md5(line.encode()).hexdigest() == hash :
                print("\033[1;32m password found : "+line)
            else:
                print("\033[1;31m Not Found !!")
if inp1=="3":
    inp=input(" Enter Text : ")
    md=hashlib.md5(inp.encode())
    ll=md.hexdigest()
    print("\033[1;32m")
    print(ll)

