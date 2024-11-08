## Encryption tool ##
from cryptography.fernet import Fernet #import function
import argparse #import function

# Menu with the following options
# 1, Generate and save a key
#   when finished, back to menu
# 2, Encrypt file with key
#   when finished, back to menu
# 3, Decrypt and read a encrypted file
#   if wish to close and encrypt file, go to no 2 then menu
# 4, Exit

# If file doesnt exist
# Message: files doesnt exist. do you want to create a new file?
# If yes -> create and save file
# If no -> do you want to try another file name? 
#   If yes -> enter file name
#   If no -> Back to menu
