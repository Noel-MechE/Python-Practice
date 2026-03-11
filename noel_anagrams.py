# Noel A Bobadilla Castillo
# Date: March 2026
# Program: Single Word Anagram Finder
# Description: This program accepts a word or name
# from the user and searches through an English
# dictionary to find all words that are anagrams
# of the input. 
# Two words are anagrams if they contain the same letters
# in any order.

#First we must begin with loading the elements we will be working with 
#1)Import Dictionary; tyhis dictionary willa ccept words and names
import load_dictionary

#2)Now that we have imported such dictionary we can now load in the words and phrases it will compare the input too while aslo declaring such input as a variable
word_list=load_dictionary.load('2of4brif.txt')

#3)Now we will, create a an empoty list to hold anagrams
anagram_list=[]

#4)We will now start to accept user name input and fixing them to lowercase 
name = input("Enter a word or phrase: ")
print("Imput name={}".format(name))
name=name.lower()
print("Using name= {}".format(name))

#5) We will begin to sort the words, first by sorting them and adding a variable to them
# We told the computer to convert sorted words into the variable name_sorted
# Then we told it to look through all the words and match it with the word entered
# Followed by telling it to fill the empty anagram list created earlier 
# with the words that match the amount of same letters in the entered word
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

#6) print out list of anagrams
print()
if len(anagram_list)==0:
    print("You need a larger dictionary or new name!")
else:
    print("Anagrams =",*anagram_list, sep="\n")