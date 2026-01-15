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
2.  Run the script: `python caesar_cipher.py.`
3.  Select **(E)** to encrypt or **(D)** to decrypt.
4.  Enter the filename and the integer shift value.
5.  Find your result in the generated output file (e.g., `encrypted_filename.txt`).

## Technical Details
The algorithm uses the modulo operator `% 26` to ensure that shifts wrap around the alphabet (e.g., 'Z' shifted by 1 becomes 'A').


# Task-03: Password Complexity Checker

## Description
Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.
Key Features & Requirements:
* Real-time Analysis: The tool should process the string and provide immediate feedback.
* Multi-Factor Validation: The assessment must be based on at least four distinct character types:
                                             Length: Minimum of 8–12 characters.
                                             Casing: A mix of uppercase ($A-Z$) and lowercase ($a-z$) letters.
                                             Numbers: Inclusion of digits ($0-9$).Special Characters:                                                                                                                        Use of symbols (e.g., 1$!$, 2$@$, 3$\#$, 4$\$$).5Strength
Categorization:
* Passwords should be ranked into tiers such as Weak, Fair, Good, or Strong.
* Actionable Feedback: If a password is weak, the tool must tell the user why (e.g., "Missing a special character").
* Evaluation Logic: The tool functions as a "scoring engine." Each time a security criterion is met, the password earns points.
* Technical Implementation
* Overview String Manipulation: Using built-in string methods or regular expressions (regex) to scan for specific patterns.Conditional
* Logic: If/Else structures to determine the final rating based on the total score.User
 * Interface: Can be implemented as a simple Command Line Interface (CLI) or a graphical web form with a dynamic color-coded strength bar.
