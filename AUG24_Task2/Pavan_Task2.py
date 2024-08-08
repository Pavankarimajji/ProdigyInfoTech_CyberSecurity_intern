from PIL import Image
import numpy as np


def encrypt_image(image_path, output_path, key):
    # Open the image and convert it to RGB
    img = Image.open(image_path).convert('RGB')
    pixels = np.array(img)
    
    # Generate a pseudo-random key for pixel manipulation
    np.random.seed(key)
    random_matrix = np.random.randint(0, 256, pixels.shape, dtype=np.uint8)
    
    # Encrypt the pixels
    encrypted_pixels = np.bitwise_xor(pixels, random_matrix)
    
    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_pixels)
    encrypted_img.save(output_path)

def decrypt_image(encrypted_image_path, output_path, key):
    # Open the encrypted image and convert it to RGB
    img = Image.open(encrypted_image_path).convert('RGB')
    pixels = np.array(img)
    
    # Generate the same pseudo-random key for pixel manipulation
    np.random.seed(key)
    random_matrix = np.random.randint(0, 256, pixels.shape, dtype=np.uint8)
    
    # Decrypt the pixels (XOR again with the same matrix)
    decrypted_pixels = np.bitwise_xor(pixels, random_matrix)
    
    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_pixels)
    decrypted_img.save(output_path)


if __name__ == '__main__':    
    num = int(input("1)encrypt\n2)decrypt\n-------> "))
    if num == 1:
        key = int(input("Enter Key : "))
        encrypt = input("Enter Image Path To Encrpt : ")
        encrypt_image(encrypt, 'encrypted_image.jpg', key)
    else:
        key = int(input("Enter Key : "))
        decrypt = input("Enter Image Path To Decrypt : ")
        decrypt_image(decrypt, 'decrypted_image.jpg', key)
