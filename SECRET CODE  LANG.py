import random
import string

def encrypt_message(message):
    """
    Encrypts each word in the given message based on the following rules:
    1. If a word has fewer than 3 characters, simply reverse it.
    2. If a word has 3 or more characters:
       - Swap the first and last letter.
       - Add three random letters at the beginning and end of the word.
    """
    
    words = message.split()  # Split the input into words
    encrypted_words = []  # List to store encrypted words
    
    for word in words:
        msg = list(word)  # Convert word to a list of characters
        
        if len(word) < 3:
            msg.reverse()  # Reverse if length is less than 3
            encrypted_words.append(''.join(msg))  # Convert back to string and store
        else:
            msg[0], msg[-1] = msg[-1], msg[0]  # Swap first and last character
            
            # Generate random letters for padding
            random_letters_start = ''.join(random.choices(string.ascii_letters, k=3))
            random_letters_end = ''.join(random.choices(string.ascii_letters, k=3))
            
            # Construct the encrypted word and store it
            encrypted_words.append(random_letters_start + ''.join(msg) + random_letters_end)
    
    return ' '.join(encrypted_words)  # Join the encrypted words back into a string


message = str(input("Enter A Message : "))  
print("Encrypted Message:", encrypt_message(message))

#=========================================================================================================================================================================================================================================================
# Decryption :=>


def decrypt_message(encrypted_message):
    """
    Decrypts each word in the given encrypted message based on the rules:
    1. If a word has fewer than 3 characters, simply reverse it.
    2. If a word has 9 or more characters (3 random + original word + 3 random):
       - Remove the 3 letters at the start and end.
       - Swap the first and last letters back.
    """
    words = encrypted_message.split()  # Split the message into words
    decrypted_words = []  # List to store decrypted words

    for word in words:
        if len(word) < 3:
            decrypted_words.append(word[::-1])  # Reverse for short words >> word[start:stop:step]
        else:
            core = word[3:-3]  # Remove the random letters
            core = list(core) # then make them into list
            core[0], core[-1] = core[-1], core[0]  # Swap first and last back
            decrypted_words.append(''.join(core))  # convert msg into string format

    return ' '.join(decrypted_words)  # Join words into a string


encrypted_message = input("Enter Encrypted Message: ")
print("Decrypted Message:", decrypt_message(encrypted_message))
