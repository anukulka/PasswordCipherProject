'''
Project 2 - Secret Codes - Fall 2020
Author: <Anurag Kulkarni >

<This program encrypts/decrypts the users statement using a shift factor and unicode characters.>

I have neither given or received unauthorized assistance on this assignment.
Signed:  <Anurag Kulkarni>
'''

print('Welcome to Cryptic2020!\n')
'''The main method/function prompts the user to enter an input that will either encrypt/decrypt a statement of their choice or quit the program. The main method/function calls the encrypt and decrypt functions if the user enters 'e' or 'd'. '''
def main():
    o = input('Encrypt (E), Decrypt (D), or Quit (Q)?')
    while o.lower() != 'quit' and o.lower() != 'q':#loops so that the user can enter another input unless user quits program
        if o.lower() != 'e' and o.lower() != 'd' and o.lower() != 'q' and o.lower() != 'encrypt' and o.lower() != 'decrypt' and o.lower()!= 'quit':
            break
        k = input('What is the original message you would like to input? ')#prompts the user to enter a statement
        v = get_shift_factor()#calls the get_shift_factor function which asks for the shift factor
        if o.lower() == 'e' or o.lower() == 'encrypt':
            w = encrypt(k,v)#calls the encrypt function if the user enters e or encrypt
            print(w) #prints the encrypted result with the shift factor
        if o.lower() == 'd' or o.lower() == 'decrypt':
            decrypt(k,v)#calls the decrypt function if the user enters d or decrypt
            d = decrypt(k,v)
            print(d) #prints the decrypted result with the shift factor
        o = input('Encrypt (E), Decrypt (D), or Quit (Q)?')
'''The get_shift_factor function asks for the user to enter an input, if it is less than or equal to zero, the function asks again'''
def get_shift_factor():
    a = input('Enter your desired shift factor')
    while int(a) <= 0: #this function only works if the input is greater than zero
        print('Try again, enter a shift factor that is greater than zero.')
        a = input('Enter your desired shift factor')
    return int(a) #returns the desired shift factor 
'''The encrypt function stores the statement string, then encrypts the statement and then stores the ecnrypted string back into the original string'''
def encrypt(string1, shift):
    encryptedstr = '' #null string which eventually stores the encrypted string
    for i in string1: #for each character in the string, the code below encrypts it into unicode
        relative_shift = (ord(i)- ord(' ') + shift) % 95
        encrypted_char = chr(ord(' ') + relative_shift)
        encryptedstr += encrypted_char #stores the encrypted string back into the null string
    return encryptedstr #returns the encrypted string
'''The decrypt function stores the statement string, then decrypts the statement and then stores the decrypted string back into the original string'''
def decrypt(string2, shift):
    decryptedstr = '' #null string that eventually stores the decrypted string
    for i in string2: #for each character in the string, the code below decrypts it into unicode
        relative_shift = (ord(i)- ord(' ') - shift) % 95
        decrypted_char = chr(ord(' ') + relative_shift)
        decryptedstr += decrypted_char #stores the decrypted string back into the null string
    return decryptedstr #returns the decrypted string

if __name__ == '__main__':
    main() #calls the main method/function for the program to run