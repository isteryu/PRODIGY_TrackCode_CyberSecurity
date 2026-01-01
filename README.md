# PRODIGY_TrackCode_CyberSecurity
I would like to express my sincere gratitude to Prodigy Infotech for providing me with the opportunity to work on hands-on cybersecurity projects during my internship. This internship helped me understand the fundamentals of cryptography, data protection, and secure information handling. Through these tasks, I gained practical exposure to implementing encryption techniques and learned how cybersecurity principles are applied in real-world scenarios.

# Task 01: Caesar Cipher Tool

## Description
A Python-based security tool that implements the Caesar Cipher algorithm. This program can encrypt and decrypt text files by shifting the characters of the alphabet by a user-defined value.

## Features
* **File Support:** Reads from `.txt` files and saves results to new files.
* **Case Sensitivity:** Preserves uppercase and lowercase letters.
* **Special Characters:** Maintains spaces, numbers, and symbols without corruption.
* **Error Handling:** Validates file existence and user input.

## How to Use
1.  Place the text file you want to process in the project directory.
2.  Run the script: `python caesar_cipher.py`
3.  Select **(E)** to encrypt or **(D)** to decrypt.
4.  Enter the filename and the integer shift value.
5.  Find your result in the generated output file (e.g., `encrypted_filename.txt`).

## Technical Details
The algorithm uses the modulo operator `% 26` to ensure that shifts wrap around the alphabet (e.g., 'Z' shifted by 1 becomes 'A').

Task 2: Pixel Manipulation for Image Encryption
This task focuses on developing a simple image encryption tool using pixel manipulation techniques. The image is encrypted by modifying or swapping pixel values using basic mathematical operations. The encrypted image appears unreadable compared to the original image. Decryption is done by reversing the applied pixel operations. This task demonstrates how image data can be secured using encryption methods
