__author__ = 'Animesh'

from utils.file_reader import FileReader
from utils.file_writer import FileWriter
from utils.preprocessor import Preprocessor
from utils.sentence_extractor import SentenceExtractor
from utils.feature_reducer import FeatureReducer
from utils.weights_handler import WeightsHandler
import os

class Summarizer:
	
	def summarize(self,input_path):
		
		tot_docs = 0
		preprocessed_list = []
		dataset_Reader = FileReader()
		dataset_output_handler = FileWriter()
		dataset_preprocessor = Preprocessor()
		dataset_WeightsHandler = WeightsHandler()
		dataset_FeatureReducer = FeatureReducer()
		
		
		files = [f for f in os.listdir(input_path) if os.path.isfile(input_path + '/'+ f)]
		
		try:
			for doc in files:
				with open(input_path + '/' + doc):
					print input_path + '/' + doc
					inputdataset = dataset_Reader.read(input_path + '/' + doc)
					
					dataset_WeightsHandler.update_sentenceList(inputdataset)  
					
					preprocessed_data = []
					for word in inputdataset.split():
						word = word.lower()
						if word not in dataset_preprocessor.stop_words():
							preprocessed_data.append(str(dataset_preprocessor.preprocess(word)))
  		
					for j in range(len(preprocessed_data)):
						dataset_WeightsHandler.update_totfreq_dict(preprocessed_data[j])
					preprocessed_list.append(preprocessed_data)
	

		except IOError:
			print "IOError"

		print preprocessed_list
		dataset_WeightsHandler.replace_totfreq_dict(dataset_FeatureReducer.reduceFeatures(dataset_WeightsHandler.tot_freq_dict()))
		
		#dataset_WeightsHandler.generate_inv_doc_freq_dict(total_documents, input_path)
		#dataset_WeightsHandler.generate_tot_weight_dict()
		dataset_WeightsHandler.generate_STM()
		#print dataset_WeightsHandler.sentenceWeight_dict()



if __name__ == '__main__':
	import sys	
	input_path = sys.argv[1]
	summarizer = Summarizer()
	summarizer.summarize(input_path)
