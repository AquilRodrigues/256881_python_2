import ast
import string
def search():
    my_dict = open("words.txt", "r")
    word = input("Enter the word: ")
    word = word.lower()
    contents = my_dict.read()
    contents=contents.split("\n")
    flag=1
    for line in contents:
        line = line.split(":")
        if word in line[0]:
            print( line[0], ":", line[1])
            flag=0
    if flag==1:
        print("Word not available")
    my_dict.close()


def add_word():
    my_dict = open("words.txt", "a")
    word = input("Enter the word: ")
    word = word.lower()
    check=0
    check = word_check(word)
    if check == 1:
        print("word already exist")
        my_dict.close()
    else:
        meaning = input("Enter the meaning of the word : ")
        new= word + ":" + meaning + "\n"
        my_dict = open("words.txt", "a")
        my_dict.write(new)
        my_dict.close()

    

def word_check(check):
    my_dict = open("words.txt", "r")
    
    check = check.lower()
    contents = my_dict.read()
    contents=contents.split("\n")
    for line in contents:
        line = line.split(":")
       
        if check == line[0]:
            return 1
        


choice = input("Enter 1 if you want to search \n Enter 2 if you want to add word : ")
if choice== "1":
    search()
else:
    add_word()
#change