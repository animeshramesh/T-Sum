from nltk import stem
import sys
import re
 
#Casefolding is done in stemming itself.
#stopwords_reference is a file which contains the stop words collection.
stopwords=open('stopwords_reference','r+').read()

# stemming begins 
stemmer=stem.snowball.EnglishStemmer()
f=open('dataset','r+')
text_input=f.read()
#while(len(text_input)>0):
for word in text_input.split(" "):
	word.lower()
	if(stopwords.find(word)<0):
			word=re.sub(r"[^\w\s]",'',word)
			sys.stdout.write(stemmer.stem(word)+' ');
#stemming ends
