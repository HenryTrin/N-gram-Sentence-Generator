import random
import re
import sys
import collections

"""
Things to do

2 inputs
arg 0 = 1,2,3 (unigram, bi,tri)

arg 1- infinite is the input text files

so that means we want to have the files be read

the input files are txt files

We take each text file and lowercase and split them 
Also take each puntuation and seprate them.

regex for first punctation = ^[.!?]+?
so now we need the regex for seperating puncaion

steps
chatterbot 1 input1.txt input2.txt
first take the input files
lower + split + seperate them
*remember this can be any input files greater then 1
so while len sys[argv]
go to each input files


put them into keys(tokens) and value(counter for each)
have it count the number as it goes in the input files

unigram calc
probabilty 
so takes single words
then uses probabiltiy to make the sentences
then print


"""

def textFileProccess():
   return 0

def unigramSentenceGenerator():
	print("Unigram")
	return 0
def bigramSentenceGenerator():
   return 0

def trigramSentenceGenerator():
   return 0

def main(argv):
	"""
	Chatterbot 1 10 pg2554.txt pg2600.txt pg1399.txt

	argv[1] = uni, bi, tri
	arv[2] = number of sentences
	argv[3-whatever] = text files


	split, lowercase
	word, punctuation = tokens

	each word is key
	each occurance is a counter

	
	"""


	numberOfSentences = sys.argv[2]

	if int(sys.argv[1]) == 1:
		unigramSentenceGenerator(numberOfSentences)
	elif int(sys.argv[1]) == 2:
		bigramSentenceGenerator(numberOfSentences)
	elif int(sys.argv[1]) == 3:
		trigramSentenceGenerator(numberOfSentences)
	else:
		print("Invalid Argument, please use 1-3 and not" + sys.argv[1])
	return 0

main(sys.argv)
