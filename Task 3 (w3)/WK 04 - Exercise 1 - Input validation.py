'''
WEEK 03 Exercise - Application of recent learning
Incorporate your recent studies of Python data structures and file handling to solve the following, e.g. 
- file handling and methods
- strings
- lists
- sets and/or dictionaries

along with the relevant functions/methods they offer.

Paul Knighton
'''
# Open a word_list.txt file for reading
with open("words.txt", "r") as file:
    content = file.readlines()# Main file reading loop
    print(content)# read all lines into a list 

# count the number of lines in a file
number=len(content)
print(number)
# Main processing of list:
# print all items in the list
content = [line.strip() for line in content]
# print all items in the list in alphabetic order A-Z (ascending), e.g. sorted.
print(sorted(content, key=str.lower,reverse=False))
# print all items in the list in alphabetic order Z-A (descending), eg sorted and reversed.
print(sorted(content, key = str.lower,reverse=True))
# print the shortest word and its' length
shortest_word = min(content, key=len)
print(shortest_word ,len(shortest_word))
# print the longest word and its' length
longest_word = max(content,key=len)
print(longest_word,len(longest_word))
# print number of items in the list, the first item and the last item of list.
print(content[0],"is the first word") 
print(content[number - 1],"is the last word in the last")
# print only the unique items in the list, along with the number of times each one occurs in the list
for word in content:
    if word[0].isupper():
        print(word)
        print(len(word),"is how long the word is")# print the number of unique items in the list

# Scrabble / Word finder v1:
# in a loop ask the user for a start letter,
# then print all words beginning with a specific letter, which the user inputs.
# Extend your Scrabble / Word finder to print all words beginning with a specific letter, which are a specific number of letters long, which the user inputs.
game=True
while game == True:
    start_letter=input("Enter a start letter: ")
    length=int(input("Enter the length of the word: "))
    for word in content:
        if word[0]==start_letter and len(word) == length:
            print(word)
    play_again=input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        game = False
        print("Thanks for playing!")