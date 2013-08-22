import re,os
from nltk import stem
from utils.file_reader import FileReader



class Preprocessor:
    
    def stop_words(self):
        stop_words_filename = os.path.join(os.path.dirname(__file__), 'stopwords_reference')
        stopwords = open(stop_words_filename, 'r+').read()
        return stopwords

    def regularise_expression(self, word_in_dataset):
        word = re.sub(r'[^\w\s]', ' ', word_in_dataset)
        return word


    def stem_word(self, word_in_dataset):
        stemmer = stem.snowball.EnglishStemmer()
        stemmed_word = stemmer.stem((word_in_dataset))
        return stemmed_word


    def preprocess(self, files, input_path):
        dataset_Reader = FileReader()
        preprocessed_list = []
        try:
            for doc in files:
                with open(input_path + doc):
                    inputdataset = (dataset_Reader.read(input_path + doc))
                    preprocessed_data = []
                    for word in inputdataset.split():
                        word = word.lower()
                        if word not in self.stop_words():
                            filter1 = self.regularise_expression(str(word))
                            filter2 = self.stem_word(filter1)
                            preprocessed_data.append(str(filter2))
                            
                    preprocessed_list.append(preprocessed_data)
        except IOError:
            print "IOError"
        
        return preprocessed_list



