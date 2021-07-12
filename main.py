alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

newText = ""
letterLoc = 0

if(direction == 'encode'):
    for letter in range(0, len(text)):
        letterLoc = alphabet.index(text[letter])
        print(letterLoc)
        if(letterLoc + shift > 25):
            newText = newText + alphabet[(letterLoc + shift) - 26]
        else:
            newText = newText + alphabet[letterLoc + shift]
    print(newText)
elif(direction == 'decode'):
    for letter in range(0, len(text)):
        letterLoc = alphabet.index(text[letter])
        if(letterLoc - shift < 0):
            newText = newText + alphabet[(letterLoc - shift) + 26]
        else:
            newText = newText + alphabet[letterLoc - shift]
    print(newText)
else:
    print("invalid inputs, please try again")
