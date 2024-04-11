def palindrome(word):
    wordSplit = [x for x in word if x != ' ']
    wordReverse = [wordSplit[i] for i in range(len(wordSplit) - 1, - 1, - 1)]
    if wordSplit == wordReverse:
        return "It is a palindrome "
    else: 
        return "Its not a palindrome"
    
word = input("Write a word: ")
print(palindrome(word))    