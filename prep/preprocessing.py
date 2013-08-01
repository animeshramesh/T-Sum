import re
from nltk import stem

class preprocessor:
    
    __text = []        # Private variable
    
    def return_stop_words(self):
        stopwords=open('stopwords_reference','r+').read()
        return stopwords
    
    def stop_word_eliminate(self,data):
        filtered_data = []
        c = preprocessor()
        stop_words = c.return_stop_words()
        text = data.split()
        for word in text:
            if (stop_words.find(word)<0):
              word=re.sub(r"[^\w\s]",'',word) 
              filtered_data.append(word)
        return filtered_data
            
        
    def stem_word(self,data):
      stemmer=stem.snowball.EnglishStemmer()
      stemmed_data= " "
      for word in data:
         stemmed_data += stemmer.stem(word)+' '        
      return stemmed_data
    
    def to_lower_case(self,data):
        return data.lower()
    
    


