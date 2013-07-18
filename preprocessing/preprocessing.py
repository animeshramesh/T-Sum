import re
from nltk.stem.lancaster import LancasterStemmer
from nltk import stem


class preprocessor:
    
    __text = []        
    
    
    def ret_stop_words(self):
        stopwords=open('stopwords_reference','r+').read()
        return stopwords
    
    
    def stop_word_eliminate(self,data):
            
        filtered_data = []
        c = preprocessor()
        stop_words = c.ret_stop_words()
        text = data.split()
        for word in text:
            if (stop_words.find(word)<0) and len(word)>3:
              word=re.sub(r"[^\w\s]",'',word) 
              filtered_data.append(word)
        return filtered_data
            
        
    
    def stem_word(self,data):
      stemmer=LancasterStemmer()
      #stemmer = stem.snowball.EnglishStemmer()		# Getting the 'u' bug using snowball.. So used Lancaster instead
      stemmed_data=[]
      for word in data:
          stemmed_data.append(stemmer.stem(word))
      return stemmed_data
    
    
    def to_lower_case(self,data):
        return data.lower()
    
    
 
class input_this:
    
    def input_from_file(self,input_file):
        input_this.text = open(input_file,'r+').read()
        return input_this.text
    

class output_this:
    
    def display(self,word):
        print (word)
        
        

def main():
	a = input_this()
	b = output_this()
	prep = preprocessor()

	inputdataset = a.input_from_file("dataset");

	filter1 = prep.to_lower_case(inputdataset)
	filter2 = prep.stop_word_eliminate(filter1)
	filter3 = prep.stem_word(filter2)
	
	b.display(filter3)  
	  

main()

