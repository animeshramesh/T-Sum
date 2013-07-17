from nltk import stem
import sys
import re
 
<<<<<<< HEAD
# stopwords_reference contains the stop words collection.

=======

#stopwords_reference is a file which contains the stop words collection.
>>>>>>> 70bdcd6da788df3947ab27d5c49607fe95f7f4b7
stopwords=open('stopwords_reference','r+').read()

# Preprocessing begins
# Stopword elimination --> Case folding --> Stemming

text_input=open('dataset','r+').read()
stemmer=stem.snowball.EnglishStemmer()
<<<<<<< HEAD


for word in text_input.split(" "):	#Iterating through the words in the dataset
	word.lower()	# Implementing case-folding
	if(stopwords.find(word)<0):	# If word isnt a part of stopword collection
			word=re.sub(r"[^\w\s]",'',word)	  
			sys.stdout.write(stemmer.stem(word)+' '); # Stem and print the word


# Preprocessing ends
=======
f=open('dataset','r+')
text_input=f.read()

for word in text_input.split(" "):
	word.lower()
	if(stopwords.find(word)<0):
			word=re.sub(r"[^\w\s]",'',word)
			sys.stdout.write(stemmer.stem(word)+' ');
#stemming ends
>>>>>>> 70bdcd6da788df3947ab27d5c49607fe95f7f4b7
