#Pixel Manipulation for Image Encryption
#task2

from PIL import Image
from termcolor import colored

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print(colored("Image encrypted successfully!","green"))

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print(colored("Image dencrypted successfully!","green"))

encrypted_image = "decrypted_image.jpg"
decrypted_image = "encrypted_image.jpg"

if __name__ == '__main__': 
    while True:
        num = int(input("**Cyber Security Task 2**\nPAVAN\n1)encrypt\n2)decrypt\n-------> "))
        if num == 1:
            key = int(input("Enter Key : "))
            input_image = input("Give Path : ")
            encrypt_image(input_image, encrypted_image, key)
        else:
            key = int(input("Enter Key : "))
            input_image = input("Give Path : ")
            decrypt_image(input_image, decrypted_image, key)
