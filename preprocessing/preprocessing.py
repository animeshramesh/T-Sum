from nltk import stem
import sys
import re
 
# stopwords_reference contains the stop words collection.

stopwords=open('stopwords_reference','r+').read()

# Preprocessing begins
# Stopword elimination --> Case folding --> Stemming

text_input=open('dataset','r+').read()
stemmer=stem.snowball.EnglishStemmer()


for word in text_input.split(" "):	#Iterating through the words in the dataset
	word.lower()	# Implementing case-folding
	if(stopwords.find(word)<0):	# If word isnt a part of stopword collection
			word=re.sub(r"[^\w\s]",'',word)	  
			sys.stdout.write(stemmer.stem(word)+' '); # Stem and print the word


# Preprocessing ends
