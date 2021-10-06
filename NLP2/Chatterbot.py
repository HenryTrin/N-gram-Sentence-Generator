import random
import re
import sys
import random
"""
10/6/2021
Henry Trinh
Chatterbot (N-gram Sentence Generator)
Description:

    This program is a n-gram se
Potential Output:

Usage Instruction:
    1. Make sure that python and python compiler is installed on the computer,
    2. Make sure to execute this program in a terminal such as Window Powershell, or a Linux terminal,
        *If using a IDE make sure to input arguments correctly.
    3. Make sure all input files are text files and reachable. The easiest would be to put them into the same folder as this program.
    4. To execute this program, an example would be "Chatterbot 1 10 1064-0.txt".
        Arguments explained:
            Chatterbot (1-3) (1-infinite) (input text files 1 - infinite) 
            * Chatterbot = the name of the program
            * (1-3) = the n-gram you wanted. There are 3 choices
                1 = Unigram
                2 = Bigram
                3 = Trigram
            * (1-inifite) = This is the number of sentences you want to produce from the n-gram
                            Make sure the number is greater then 1 or will throw an error
            * (input text files - infinite) = This is the number of text files used for the generation of random sentences.  
                                              Make sure the number of text files is greater then 1 or will throw an error. 
    5. The program will then execute with your given arguments and print out the random sentences.

Algorithms used:
    Unigram:
    Bigram:
    Trigram:
Links used: 

"""

"""
links used :
https://realpython.com/python-counter/ 
https://www.pythontutorial.net/python-basics/python-read-text-file/ 
https://www.geeksforgeeks.org/python-arrays/ 
"""



def unigramCalculator(text):
    unigramSentence = ""

    return unigramSentence


def bigramCalculator(text):
    bigramSentence = ""
    return bigramSentence


def trigramCalculator(text):
    trigramSentence = ""
    return trigramSentence


"""
n-gramSentenceGenerator(numberOfSentences, text)

The next 3 functions:
unigramSentenceGenerator
bigramSentenceGenerator
trigramSentenceGenerator

are the same functions where they take the number of sentences with the text
into their respective n-gramCalculator function to contain and print
the random n-gram sentences. I make it like this so its easier for to read each function
rather then put it all into the same function with a if statement.

:param int numberofSentences, string text
:return 0
"""

def unigramSentenceGenerator(numberOfSentences, text):
    for i in range (1, int(numberOfSentences) + 1):
        #Printing starts at 1 to numberofSentences
        print(str(i) + "." + unigramCalculator(text))
    return 0


def bigramSentenceGenerator(numberOfSentences, text):
    for i in range (1, int(numberOfSentences) + 1):
        # Printing starts at 1 to numberofSentences
        print(str(i) + "." + bigramCalculator(text))
    return 0


def trigramSentenceGenerator(numberOfSentences, text):
    for i in range (1, int(numberOfSentences) + 1):
        # Printing starts at 1 to numberofSentences
        print(str(i) + "." + trigramCalculator(text))
    return 0



"""
main()

This function handles the command line inputs, argv[1] = unigram, bigram, trigram,
argv[2] = number of sentences, argv[3-whatever numbers of text files greator then 1] = input text files
the functions will use to make sentences. 

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
    #String that will hold the input file texts
    allText = ''
    #Takes the arugment
    numberOfSentences = sys.argv[2]
    # Needed a way to keep going past any amount of input text files got this
    # from https://www.geeksforgeeks.org/python-arrays/
    inputFiles = sys.argv[3:]

    # Needed a way to open files with the number of input files
    # Source: https://www.pythontutorial.net/python-basics/python-read-text-file/
    for currentfile in inputFiles:
        #Had to use utf8 encoding, otherwise errors
        #Source: https://docs.python.org/3/howto/unicode.html
        with open(currentfile, encoding="utf8") as file:
            allText = allText +  file.read()
            file.close()

    # Lowers all of the text
    allText = allText.lower()

    # Separates the punctuation from the string
    # Source: https://pynative.com/python-regex-replace-re-sub/
    sepAllText = re.sub(r'([,.!?])', r' \1 ', allText)
    print(sepAllText)

    processedText = sepAllText.split()


    #Will choose the n-gram based on the argument given
    if int(sys.argv[1]) == 1:
        print("Unigram Selected: \n")
        unigramSentenceGenerator(numberOfSentences, processedText)
    elif int(sys.argv[1]) == 2:
        print("Bigram Selected: \n")
        bigramSentenceGenerator(numberOfSentences, processedText)
    elif int(sys.argv[1]) == 3:
        print("Trigram Selected: \n")
        trigramSentenceGenerator(numberOfSentences, processedText)
    else:
        print("Invalid Argument, please use 1-3 and not" + sys.argv[1])
    return 0

#Executes the program with arguments from command-line
main(sys.argv)
