from nltk import stem
import sys
import re
 
# stopwords_reference contains the stop words collection.

stopwords=open('stopwords_reference','r+').read()

# Preprocessing begins
# Stopword elimination --> Case folding --> Stemming

text_input=open('dataset','r+').read()
stemmer=stem.snowball.EnglishStemmer()


for word in text_input.split(" "):    
    word.lower()    
    if(stopwords.find(word)<0):    
            word=re.sub(r"[^\w\s]",'',word)      
            sys.stdout.write(stemmer.stem(word)+' '); 


# Preprocessing ends
