# def main():
    
## Encryption tool ##
from cryptography.fernet import Fernet #import function for encryption
import argparse #import function used for handle and interpret arguments
import os #to interact with operating system ie local files
from docx import Document #för att kunna öppna wordfiler

# 2, Encrypt file with key
#   when finished, back to menu
# 3, Decrypt and read a encrypted file
#   if wish to close and encrypt file, go to no 2 then menu


# borde jag göra om detta till en klass?
print("Welcome to the encryption service!") #welcome message followed by main menu with the different options of the programme
while True: 
    print("Menu:")
    print("1. Generate and save a key")
    print("2. Encrypt file (key needed)")
    print("3. Decrypt and read a file (key needed)")
    print("4. Exit")

    navigation = input("Select option (1-4): ")
    # print(navigation) #Test to see if input works
    
    if navigation == "1":
        key = Fernet.generate_key() #kör en metod
        #print(f"Generated password: {key.decode()}") #Test to see if key is generated

        namepf = input("Name your password file: ")
        if os.path.exists(namepf):
            namepf = input(f"The file {namepf} already exists. Please choose another name: ") #detta skulle kunna vara en klass

        with open(namepf, "wb" ) as key_file:
            key_file.write(key)
            print(f"Password is saved to file {namepf}.")

    if navigation == "2":
        while True:
            file2encrypt = input("Select file to encrypt: ")
            try:
                with open(file2encrypt, "rb") as file: 
                    data =file.read()
                print(f"The file '{file2encrypt}' was opened.")
                break
            except FileNotFoundError:
                print(f"Error: The file '{file2encrypt}' was not found. Please check the file name and path.")
                try_again = input("To try again write 'yes', to go back to menu write 'no': ").lower()
                if try_again == "no":
                    break

                
            
# with open("ny_bilg.png", "wb") as new_file:
#     new_file.write(data)
        #öppna en befintlig fil
        #fil finns redan
        #skapa en ny fil

    # if navigation == "3":

    # if navigation == "4":
    #     print("You are now closing the programme.")
    #     break

    


# ANVÄND OS FUNKTION FÖR ATT ÄNDRA OCH HANTERA FILER

# with open("den valda filen", "rb") as file: #såhär öppnar man en fil
#     data =file.read()
# with open("ny_bilg.png", "wb") as new_file:
#     new_file.write(data)

# If file doesnt exist
# Message: files doesnt exist. do you want to create a new file?
# If yes -> create and save file
# If no -> do you want to try another file name? 
#   If yes -> enter file name
#   If no -> Back to menu


# if __name__ == "__main__":
#     main()