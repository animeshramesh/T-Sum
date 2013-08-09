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
        dataset_preprocessor = Preprocessor()
	dataset_WeightsHandler = WeightsHandler()
        i = 1
        while 1:
            try:
                with open(dataset_directory + '/%d.txt' % i):
                    inputdataset = dataset_Reader.read(dataset_directory + '/%d.txt' % i)
		    dataset_WeightsHandler.update_sentenceList(inputdataset)
		    preprocessed_data = dataset_preprocessor.preprocess(inputdataset)
                    for j in range(len(preprocessed_data.split())):
			dataset_WeightsHandler.update_totfreq_dict(preprocessed_data.split()[j])
                    i += 1
            except IOError:
                break
  	
	self.__total_documents = i-1
	
   
    def total_documents(self):
        return self.__total_documents

