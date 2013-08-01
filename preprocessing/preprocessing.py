import sys
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
    
    
#The code from here,has just been used for testing;Suitable packages will be created. 
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

	#inputdataset = a.input_from_file("allin1.txt");
	i=1
	inputdataset = ""
	try:	
		while(inputdataset != '\0'):
   		#inputdataset = loadtxt('{0}.txt'.format(i + 1), float)
			
			inputdataset = a.input_from_file('%d.txt' % (i));
			filter1 = prep.to_lower_case(inputdataset)
		
			filter2 = prep.stop_word_eliminate(filter1)
			
			filter3 = prep.stem_word(filter2)
	
			i = i + 1
			b.display(filter3) 
			print '\n' * 2
	except IOError,e :
		print e[0],e[1]
				    

main()



