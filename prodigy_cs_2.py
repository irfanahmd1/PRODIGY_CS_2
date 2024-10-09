from PIL import Image

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size
    key = key % 256
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[i, j] = (r, g, b)
    image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size
    key = key % 256
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[i, j] = (r, g, b)
    image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").lower()
    image_path = input("Enter the path of the image: ").strip().strip('"')
    output_path = input("Enter the output path for the new image: ").strip().strip('"')
    key = int(input("Enter the encryption key (a number between 0 and 255): ").strip())
    print(f"Image path: {image_path}")
    print(f"Output path: {output_path}")
    if choice == 'e':
        encrypt_image(image_path, output_path, key)
    elif choice == 'd':
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()