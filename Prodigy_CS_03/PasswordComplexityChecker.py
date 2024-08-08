from termcolor import colored
anti_caps = "qwertyuiopasdfghjklzxcvbnm"
caps = "QWERTYUIOPASDFGHJKLZXCVBNM"
num = '0123456789'
special = "!@#$%^&*()_+"

password = input("Enter your Password : ")

r = len(password)
re ,c,ac,n,sp= False,False,False,False,False

print(r)
for i in range(0,r):
    if r<8:
        print("more sure password must be 8 or more ")
        break
    elif password[i] in caps:
        c = True
    elif password[i] in anti_caps:
        ac = True
    elif password[i] in num:
        n = True
    elif password[i] in special:
        sp = True

re = (c,ac,n,sp)
if all(re):
    print(colored("your password is secured","green"))
else:
    print(colored("oops you need to give secure password","red"))    


