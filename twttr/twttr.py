inword = input("Input: ")
outword = ""
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
#for every letter, check if it's in the vowels list. If so, return ""

for letter in range(len(inword)):
    if inword[letter] in vowels:
        outword += ""
    else:
        outword += inword[letter]
print ("Output: ", outword)