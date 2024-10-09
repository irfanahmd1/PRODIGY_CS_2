Image Encryption and Decryption Tool

This Python project allows you to encrypt and decrypt images using a simple key-based pixel manipulation technique. The encryption is done by modifying the RGB values of each pixel, and the decryption reverses the changes using the same key.

Features
Encrypt Images: Encrypt an image by shifting its RGB pixel values using a key.
Decrypt Images: Decrypt an encrypted image using the same key to restore the original image.
Prerequisites
To run this project, you need to have Python installed along with the Pillow library.

Install Dependencies

Run the following command to install the required library:

pip install Pillow

How to Use
Clone the repository:

git clone https://github.com/irfanahmd1/PRODIGY_CS_2.git

Navigate to the project directory:

cd PRODIGY_CS_2
Run the script:
Use the following command to run the program:

python prodidy_cs_2.py

Choose to Encrypt or Decrypt:

After running the script, you will be prompted to either encrypt or decrypt an image.

Encryption: Enter E to encrypt an image.
Decryption: Enter D to decrypt an image.
Provide the required details:

Image path (e.g., image.jpg)
Output path for the new image (e.g., encrypted_image.jpg)
An encryption key (a number between 0 and 255)
