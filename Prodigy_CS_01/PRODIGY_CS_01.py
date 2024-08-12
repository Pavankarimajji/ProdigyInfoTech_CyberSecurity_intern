#CyberSecurity_Intern #task1
#Prodigy_Info_Tech
#Pavan_Naga_Durga_Ramesh_Karimajji
'''
Implement Caesar Cipher

Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. 
Allow users to input a message and a shift value to perform encryption and decryption.
'''



letters = 'abcdefghijklmnopqrstuvwxyz'
letters1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrpt(text,key):
    cp = ''
    for letter in text:
        if letter == ' ':
            cp+=letter
        elif letter == letter.upper():
            index = letters1.find(letter)
            new_index = index + key
            if index ==-1:
                pass
            else:
                new_index = index + key
                if new_index >= 26:
                    new_index-=26
            cp += letters1[new_index]
        elif letter == letter.lower():
            index = letters.find(letter)
            if index ==-1:
                pass
            else:
                new_index = index + key
                if new_index >= 26:
                    new_index-=26
            cp += letters[new_index]
    return cp 

def decrypt(text,key):
    pt = ''
    for letter in text:
        if letter == ' ':
            pt+=letter
        elif letter == letter.upper():
            index = letters1.find(letter)
            new_index = index - key
            if index ==-1:
                pass
            else:
                new_index = index - key
                if new_index < 0:
                    new_index+=26
            pt += letters1[new_index]
        elif letter == letter.lower():
            index = letters.find(letter)
            if index ==-1:
                pass
            else:
                new_index = index - key
                if new_index < 0:
                    new_index+=26
            pt += letters[new_index]
    return pt


print()
print("***CYBERSECURITY_INTERNSHIP_TASK_1***")
print()




while True:
    mode = input("1)encrypt\n2)decrypt\n3)exit\nChoose option : ")
    if mode =='1':
        key = int(input("enter key between 1 to 26 : "))
        plain_text = input("enter the plain_text : ")
        ct = encrpt(plain_text,key)
        print(f"Causer Cipher Text '{ct}'")

    elif mode == '2':
        key = int(input("enter key between 1 to 26 : "))
        print()
        causer_text = input("enter causer text : ")
        print()
        plain = decrypt(causer_text,key)
        print(f"Plain Text '{plain}'")
    elif mode == '3':
        print(exit())
    
