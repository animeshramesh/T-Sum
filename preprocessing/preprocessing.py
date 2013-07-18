'''from nltk import stem
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
            word=re.sub(r"[^\w\s]",'',word-)      
            sys.stdout.write(stemmer.stem(word)+' '); 


# Preprocessing ends

'''

class preprocessor:
    
    __text = ""         # Private variable
    
    def __init__(self):
        pass
    
    def stop_word_eliminate(self,data):
        preprocessor.__text = data
        
        
    
    def stem_word(self):
        pass
    
    def to_lower_case(self):
        pass
        
    
class input_this:
    
    
    def __init__(self,):
        pass
    
    def input_from_file(self):
        input_this.__text = open('dataset','r+').read()
        return input_this.__text
    
class output_this:
    
    def __init__(self,text):
        self.text = text

    def display(self):
        print (self.text)
        
        
        
        
    
    
     

        #output_this.display(preprocessor.stop_word_eliminate(input_this.input_from_file()))
print ("Here!!!!")
output_this.display(input_this.input_from_file())
        
