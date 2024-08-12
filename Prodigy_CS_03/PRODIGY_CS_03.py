'''PASSWORD COMPLEXITY CHECKER'''

from termcolor import colored
import pyfiglet

anti_caps = "qwertyuiopasdfghjklzxcvbnm"
caps = "QWERTYUIOPASDFGHJKLZXCVBNM"
num = '0123456789'
special = "!@#$%^&*()_+"

text = "Password Complexity Checker"
fonts = ["slant"]

for font in fonts:
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print(colored(f"Name: {'Pavan'}\n{ascii_art}\n", 'red'))
password = input("Enter your Password : ")

r = len(password)
c,ac,n,sp= False,False,False,False

for i in range(0,r):
    if r<8:
        print("more sure password must be 8 or more ")
        break
    if password[i] in caps:
        c = True
    if password[i] in anti_caps:
        ac = True
    if password[i] in num:
        n = True
    if password[i] in special:
        sp = True

re = (c,ac,n,sp)
if all(re):
    print(colored("your password is secured","green"))
else:
    print("<----"+colored(password,"red")+"----> \noops you need to give secure password\n" +colored("password should have caps,small_letters,special_chars_numbers","red"))    


