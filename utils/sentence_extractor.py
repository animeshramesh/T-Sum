from nltk.tokenize import sent_tokenize
import re
class SentenceExtractor:
    
    def extract_sentences(self, textInDocument):
        sentenceEnders = re.compile('[?!.]')
        sentenceList = sentenceEnders.split(textInDocument)
        newSentenceList = [sentence for sentence in sentenceList if len(sentence) > 3]
        return newSentenceList
     
        #return sent_tokenize(textInDocument)
        
        
