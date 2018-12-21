alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
crypt = input('Would you like to encrypt(e) or decrypt(d)? ')
key = int(input('Please enter a key: '))
newMessage = ''

message = input('Please enter a message: ')
if crypt == 'e':
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + key) % 52
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
elif crypt == 'd':
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position - key) % 52
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
    
print('The new message is:', newMessage)
    
    


