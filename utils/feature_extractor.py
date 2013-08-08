__author__ = 'Animesh'


from utils.file_reader import FileReader
from utils.file_writer import FileWriter
from utils.preprocessor import Preprocessor
from utils.weights_handler import WeightsHandler
from utils.feature_reducer import FeatureReducer
import re
from os import path


class FeatureExtractor:


    
    __total_documents = 0

    def extract(self, dataset_directory):
        dataset_Reader = FileReader()
        dataset_Writer = FileWriter()
        dataset_preprocessor = Preprocessor()
	dataset_WeightsHandler = WeightsHandler()
        i = 1
        while 1:
            try:
                with open(dataset_directory + '/%d.txt' % i):
                    inputdataset = dataset_Reader.read(dataset_directory + '/%d.txt' % i)
                    preprocessed_data = dataset_preprocessor.preprocess(inputdataset)
		    dataset_Writer.write(dataset_directory + '/out%i.txt' % i, preprocessed_data)
                    for j in range(len(preprocessed_data.split())):
		        dataset_WeightsHandler.update_totfreq_dict(preprocessed_data.split()[j])
                    i += 1
            except IOError:
                break
  
	self.__total_documents = i-1


    def total_documents(self):
        return self.__total_documents



class SentenceExtractor:
    
    def extract_sentences(self, textInDocument):
        sentenceEnders = re.compile('[?!.]')
	sentenceList = sentenceEnders.split(textInDocument)
	return sentenceList
