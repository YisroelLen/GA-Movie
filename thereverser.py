reverse = (input("Enter a word or sentence, please. "))
# <User Input:> reverse_me
rev = ""
for letter in range(len(reverse), 0 , -1):
    rev += reverse[letter-1]
print (rev)
