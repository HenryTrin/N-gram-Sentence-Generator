import random
import re
import sys
import random
from collections import defaultdict

"""
10/6/2021
Henry Trinh
Chatterbot (N-gram Sentence Generator)
Description:
    This program is a N-gram Sentence Generator program with the goal of taking text files and generate random 
    sentences from those files as the data. The program will look at the patterns of words from the data and generate
    sentneces. There are 3 different ways this program can generate those files.Each will grab text from the text files.
    It goes unigram, bigram, and trigram. As you change from unigram -> trigram 
    the sentence will get more and more clear in meaning. 
    
Potential Output:
Input: 
    $ Chatterbot2.py 1 3 35-0.txt 84-0.txt
Output:
    1.into whole chinese strange , f for an to but with possible of touched i .
    
    2.have more a was face cried , blind had seemed was was all their , to .
    
    3., blood give my ; she i think i .

Usage Instruction:
    1. Make sure that python and python compiler is installed on the computer,
    2. Make sure to execute this program in a terminal such as Window Powershell, or a Linux terminal,
        *If using a IDE make sure to input arguments correctly.
    3. Make sure all input files are text files and reachable. 
        The easiest would be to put them into the same folder as this program.
    4. To execute this program, an example would be "Chatterbot 1 10 1064-0.txt".
        Command Line Arguments explained:
            Chatterbot (n-gram choice: 1-3) (number of sentences: 1-infinite) (input text files: 1-infinite) 
            * Chatterbot = the name of the program
            * (1-3) = the n-gram you wanted. There are 3 choices
                1 = Unigram
                2 = Bigram
                3 = Trigram
            * (1-infinite) = This is the number of sentences you want to produce from the n-gram
                            Make sure the number is greater then 1 or will throw an error
            * (input text files - infinite) = This is the number of text files used for the generation of random sentences.  
                                              Make sure the number of text files is greater then 1 or will throw an error. 
    5. The program will then execute with your given arguments and print out the random sentences.

Algorithms used:
    Unigram:
    Bigram:
    Trigram:
Links used: 

links used :
https://www.pythontutorial.net/python-basics/python-read-text-file/ 
https://www.geeksforgeeks.org/python-arrays/ 
https://www.w3schools.com/python/ref_dictionary_setdefault.asp 
"""

""" 
bigramDictionary(text)

Description:


:param String text
:return bigramDict
"""
def bigramDictionary(text):
    bigramDict = {}
    #Since we are looking at every 2 words. We need to minus the length by one otherwise a index error
    length = len(text) -1


    for i in range(length):
            key = text[i]
            value = text[i + 1]
            # This is here to remove any empty space entry that might occur
            if(value == ""):
                continue

            #Needed a way to have new keys coming in
            #Used: https://www.w3schools.com/python/ref_dictionary_setdefault.asp
            bigramDict.setdefault(key, []).append(value)

    return bigramDict


def trigramDictionary(text):
    trigramDict = {}
    # Since we are looking at every 3 words. We need to minus the length by one otherwise a index error
    length = len(text) - 2

    # Runs through the whole text and insert into the dictionary with a key and value
    for i in range(length):
        key = text[i] + " " + text[i + 1]
        value = text[i + 1] + " " + text[i + 2]
        # This is here to remove any empty space entry that might occur
        if (value == ""):
            continue

        # Needed a way to have new keys coming in
        # Used: https://www.w3schools.com/python/ref_dictionary_setdefault.asp
        trigramDict.setdefault(key, []).append(value)
    return trigramDict

"""
unigramCalculator(string text)
For unigram it takes the whole text and randomly pick a word from the text and add it to a (String n-gramSentence).
This process will keep going until the conditions are met:
    -If the sentence hits sentenceBoundary which are the tokens: ".!?".
        Then will check if the (String n-gramSentence) is greater then or less then the inputted parameter.
            -If greater then will return the (String n-gramSentence).
            -If less then will keep going and add words until it hits the sentenceBoundary

:param string text, int sentenceLength
:return string unigramSentence
"""

def unigramCalculator(text, sentenceLength):
    counter = 0
    unigramSentence = ""

    # Sentence Boundary to end the sentence
    sentenceBoundary = r'[.!?]'

    #Goes through all the data and just randomly pick words from the list of text
    while (True):
        #Picks a random word
        word = random.choice(text)
        if re.match(sentenceBoundary, word):
            #This is to make sure the sentences are a at least a bit long enough.
            if counter < int(sentenceLength) + 1:
                continue
            else:
                #This is the case where we met the sentence length and will put in the sentence boundary and stop.
                unigramSentence += word
                break
        else:
            #This is a word and will add on to the unigram sentence
            unigramSentence += word + " "
            counter += 1

    return unigramSentence

"""
picks 2 random words at the beggining
looks at the last word 
then find the next word
then conitnues until period.

"""
def bigramCalculator(text, sentenceLength, bigramDictionary):
    # Empty sentence used fo
    bigramSentence = ""

    # Sentence Boundary to end the sentence
    sentenceBoundary = r'[.!?]'
    counter = 0
    while(True):
        if  counter <  int(sentenceLength) + 1:
            bigramSentence = ""
            word = random.choice(text)
            counter = 0
            while not re.match(sentenceBoundary, word):
                bigramSentence += word + " "
                word = random.choice(bigramDictionary[word])
                counter += 1
            bigramSentence += word
        else:
            break

    return bigramSentence

def trigramCalculator(text, sentenceLength, trigramDictionary):
    #Counter for keeping track how long the sentence is.
    counter = 0
    trigramSentence = ""
    # Sentence Boundary to end the sentence
    sentenceBoundary = r'[.!?]'
    while (True):
        #Checks for the sentence length from the counter making sure that its long enough.
        if  counter <  int(sentenceLength) + 2:
            trigramSentence = ""
            word = random.choice(list(trigramDictionary.keys()))
            counter = 0
            while not re.match(sentenceBoundary, word):
                singleTokens = word.split()
                trigramSentence += singleTokens[0] + " "
                word = random.choice(trigramDictionary[word])
                counter += 1
            trigramSentence += word
        else:
            break


    trigramSentence = trigramSentence.split()
    while not re.match(sentenceBoundary, trigramSentence[-1]):
        trigramSentence.remove(trigramSentence[-1])

    trigramSentence = ' '.join(trigramSentence)

    return trigramSentence

"""
n-gramSentenceGenerator(numberOfSentences, text)

The next 3 functions: unigramSentenceGenerator, bigramSentenceGenerator, and trigramSentenceGenerator
are the same functions where they take the number of sentences with the text
into their respective n-gramCalculator function to contain and print
the random n-gram sentences. I make it like this so its easier for to read each function
rather then put it all into the same function with a if statement.

:param int numberofSentences, string text
:return 0
"""
def unigramSentenceGenerator(numberOfSentences, text):
    for i in range(1, int(numberOfSentences) + 1):
        # Printing starts at 1 to numberofSentences
        print(str(i) + "." + unigramCalculator(text, numberOfSentences) + "\n")
    return 0

def bigramSentenceGenerator(numberOfSentences, text, dictionary):
    for i in range(1, int(numberOfSentences) + 1):
        #Printing starts at 1 to numberofSentences
        print(str(i) + "." + bigramCalculator(text, numberOfSentences, dictionary) , "\n")


def trigramSentenceGenerator(numberOfSentences, text, dictionary):
    for i in range(1, int(numberOfSentences) + 1):
        # Printing starts at 1 to numberofSentences
        print(str(i) + "." + trigramCalculator(text, numberOfSentences, dictionary), "\n")

"""
main()

This function handles the command line inputs, 
argv[1] = unigram, bigram, trigram,
argv[2] = number of sentences, 
argv[3-whatever numbers of text files greator then 1] = input text files the functions will use to make sentences. 

First it will take the input files one at a time until all of them are processed into a allText string.
Then it will lowercase all of the text in the allText string. Then it will add a space on both sides
for all punctuation: ".!?," turning the allText string into sepAllText string. 
Now the text is ready for processing with the n-grams. Based on the user's argument of 1, 2, or 3.
The program will move into the functions (unigram, bigram, trigam)SentenceGenerator and print 
the random sentences from those functions. 
Overall just the starter function for the processing
of random sentence generation. 

:param argv
:return 0
"""

def main(argv):
    # String that will hold the input file texts
    allText = ''

    numberOfSentences = sys.argv[2]
    if int(numberOfSentences) < 0:
        print("Error: number of sentences is less then 1. Please try again.")
    # Needed a way to keep going past any amount of input text files got this
    # from https://www.geeksforgeeks.org/python-arrays/
    inputFiles = sys.argv[3:]

    # Needed a way to open files with the number of input files
    # Source: https://www.pythontutorial.net/python-basics/python-read-text-file/
    for currentfile in inputFiles:
        # Had to use utf8 encoding, otherwise errors occur with some of the input files
        # Source: https://docs.python.org/3/howto/unicode.html
        with open(currentfile, encoding="utf8") as file:
            allText = allText + file.read()
            file.close()

    # Lowers all of the text
    allText = allText.lower()

    # Separates the punctuation from the string
    # Source: https://pynative.com/python-regex-replace-re-sub/
    sepAllText = re.sub(r'([^\w])', r' \1 ', allText)

    processedText = sepAllText.split()

    # Prints the number of tokens
    print("Number of Tokens: " + str(len(processedText)))

    # Will choose the n-gram based on the argument given
    if int(sys.argv[1]) == 1:
        print("Unigram Selected:")
        unigramSentenceGenerator(numberOfSentences, processedText)
    elif int(sys.argv[1]) == 2:
        print("Bigram Selected:")
        #Will call the bigramDictionary function to generate our dictionary of bigrams
        biDict = bigramDictionary(processedText)
        bigramSentenceGenerator(numberOfSentences, processedText, biDict)
    elif int(sys.argv[1]) == 3:
        print("Trigram Selected:")
        # Will call the trigramDictionary function to generate our dictionary of trigrams
        triDict = trigramDictionary(processedText)
        trigramSentenceGenerator(numberOfSentences, processedText, triDict)
    else:
        print("Invalid Argument, please use 1-3 and not " + sys.argv[1])
    return 0

# Executes the program with arguments from command-line
main(sys.argv)
