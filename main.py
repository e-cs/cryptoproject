"""Encryption tool
using functions:
Generate and save key
Encrypt file
Decrypt and read file
## FUTURE DEV. ADD OPTION TO CREATE ENCRYPTED DIVICE (OR ENCRYPTED FILE)
"""
from cryptography.fernet import Fernet, InvalidToken #import function for encryption
import argparse #import function used for handle and interpret arguments
import os #to interact with operating system ie local files

## FUTURE DEV. REWRITE USING CLASS

# Define functions 
## FUTURE DEV. ADD FUNCTION FOR PBKDF2
## FUTURE DEV. ADD FUNKTION TO WORK WITH WORD FILES

# Generate key and save to file
def generate_key(namepf):
    key = Fernet.generate_key()
    #print(f"Generated key: {key.decode()}") #Test to see if key is generated
    namepf = input("Name your keyfile: ")

    #if the file already exist
    if os.path.exists(namepf):
        print(f"The file '{namepf}' already exists. Please try again.") #kan försöka utv så att det dir blir input
        return
    
    #save the key to file
    with open(namepf, "wb" ) as key_file:
        key_file.write(key)
        print(f"Key is saved to file '{namepf}'.")

# Encrypt file, or create and encrypt file
def encrypt_file(file_name, key_file):
    key_file = input("Select keyfile: ")
    file_name = input("Select file to encrypt: ")
    if not os.path.exists(key_file):
        print(f"The keyfile '{key_file}' cannot be found.")
        return
    
    with open(key_file, "rb") as kf:
        key = kf.read()
        keyobject = Fernet(key)
        #steps above loads the saved key into the programme

        #function below is checking to see if the file exist
    if not os.path.exists(file_name):
        print(f"The file '{file_name}' cannot be found.")
        createfile = input(f"Do you want to create a file with the name '{file_name}', yes/no? ")
        if createfile.lower() == "yes":
            with open(file_name, "wb") as file:
                file.write(b"") #skapar en binär fil som är tom
            print(f"The file '{file_name}' has been created.")
        else:
            print("No file was created.")
            return
        
        #loads the already existing file or recently created file into the programme
    with open(file_name, "rb") as file:
        filecontent = file.read()
        print(f"The file '{file_name}' was opened successfully.")
        
        #encrypt the open file using the inserted password
    encrypted_data = keyobject.encrypt(filecontent)

        #unnecessary function just because its fun, masks as mp3 in order for unauthorized ppl not to know its an encrypted file
    base_name = os.path.splitext(file_name)[0]
    encrypted_file_name = f"{base_name}.mp3"

## FUTURE DEV. ADD OPTIONAL FUNCTION TO RENAME FILE WHEN ENCRYPTING

        #save the encrypted file into new file
    with open(encrypted_file_name, "wb") as enc_file:
        enc_file.write(encrypted_data)
        print(f"Encrypted file saved as '{encrypted_file_name}'.")

## FUTURE DEV. ADD OPTION TO DELETE ORIGINAL FILE WHEN CREATING ENCRYPTED VERSION

# Decrypt file
#function to select file and password to decrypt
def decrypt_file(file_name, key_file):
    file_name = input("Select file to decrypt: ")
    key_file = input("Select keyfile: ")

    #check if the file exist
    if not os.path.exists(file_name):
        print(f"The file '{file_name}' cannot be found. Try again.")
        return
    
    try:
        #read the encrypted file
        with open(file_name, "rb") as enc_file:
            encrypted_data = enc_file.read()
  
        #check if the passwordfile exist
        if not os.path.exists(key_file):
            print(f"The keyfile '{key_file}' cannot be found. Try again.")
            return
    
        #read the key from the keyfile
        with open(key_file, "rb") as kf:
            key = kf.read()
            keyobject = Fernet(key)

        #decrypt the data using the inserted keyfile
        decrypted_data = keyobject.decrypt(encrypted_data)

        #funtion to save the file as original format, not mp3
        original_file_name = os.path.splitext(file_name)[0]
        
        #message if successfully decrypted
        print(f"The file '{file_name}' was decrypted successfully.")

## FUTURE DEV. ADD OPTIONAL FUNCTION TO RENAME FILE WHEN DECRYPTING

        #save the enc data back to regular file
        with open(original_file_name, "wb") as dec_file:
            dec_file.write(decrypted_data)
            print(f"Decrypted file saved as '{original_file_name}'.")    

## FUTURE DEV. ADD OPTION TO DELETE ORIGINAL FILE WHEN CREATING DECRYPTED VERSION 
 
    # #if errors
    except InvalidToken:
         print("The key or the file is incorrect, please try again.")
    except Exception as e:
         print(f"An error occurred: {e}")


def main():

    parser = argparse.ArgumentParser(description="Encryption tool used to generate keyfile, encrypt or decrypte file.") #initiates argparser
   
    #bacis arguments needed to navigate and perform operations:
    parser.add_argument("-o", "--operation", choices=["generate", "encrypt", "decrypt"], required=True, help="Select operation")

    #arguments to access password key or file
    parser.add_argument("-keyf", "--keyfile", help="Create a keyfile or open a existing keyfile by inserting filename.")
    parser.add_argument("-f", "--file", help="Select a file to encrypt or decrypt, or create a new file, by inserting filename.")

    #function to connect choices with def functions  
    args = parser.parse_args()

    #generate key and save to file
    if args.operation == "generate":
        generate_key(args.keyfile)
    
    #encrypt file (or create file to encrypt)
    elif args.operation == "encrypt":
        encrypt_file(args.keyfile, args.file)

    #decrypt file
    elif args.operation == "decrypt":
        decrypt_file(args.file, args.keyfile)

if __name__ == "__main__":
    main()