from utils.file_reader import FileReader
from sys import stdout
from math import log
from utils.preprocessor import Preprocessor
from utils.feature_extractor import FeatureExtractor


class WeightsHandler:

    
    __tot_freq_dict = {}		
    __inverse_doc_freq_dict = {}	
   
    def tot_freq_dict(self):
        return self.__tot_freq_dict
  
    def inverse_doc_freq(self):
	return self.__inverse_doc_freq_dict

    
    def update_totfreq_dict(self, key):
	if key in self.__tot_freq_dict:
	   self.__tot_freq_dict[key] += 1
	else:
	   self.__tot_freq_dict[key] = 1
  
    def generate_inv_doc_freq_dict(self, total_docs):
	for each_feature in self.__tot_term_freq_dict.keys():
	    docs = 0
	    for i in range(total_docs):
                input_data = FileReader.read('out%i.txt' % i)
		if input_data.count(each_feature) > 0:
                    docs += 1
	    self.__inverse_doc_freq_dict[each_feature] = docs
	

    
