import Text

def search_word(word):
    counter_word = 0
    for string in splited_text:
        if string == word:
            counter_word += 1    
    dic[word] = counter_word    




dic = {}

text = Text.text

splited_text = text.split()

string = input("Write the string you want to verify in the text: ")

search_word(string)

for key, value in dic.items():
    print(f"The word: {key} has appeared: {value}")

