maxKeySize = 26


def getMode():
    while True:
        mode = input(
            '\nEnter "e" to encrypt or "d" to decrypt a message: ').lower()
        if mode in 'e d'.split():
            return mode
        else:
            print('Enter either "e" or "d".')


def getMessage():
    msg = input("\nEnter your message: ")
    return msg


def getKey():
    key = 0
    while True:
        key = int(input("\nEnter the key number(1-26): "))
        if (key >= 1 and key <= maxKeySize):
            return key


def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)

        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print("\nYour translated text is: " +
      getTranslatedMessage(mode, message, key) + "\n")
