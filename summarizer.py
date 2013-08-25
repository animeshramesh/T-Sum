from utils.preprocessor import Preprocessor
from utils.feature_reducer import FeatureReducer
from utils.weights_handler import WeightsHandler
import os

class Summarizer:

    def summarize(self,input_path):
        dataset_preprocessor = Preprocessor()
        dataset_FeatureReducer = FeatureReducer()
        dataset_WeightsHandler = WeightsHandler()
        files = [f for f in os.listdir(input_path) if os.path.isfile(input_path + f)]
        preprocessed_list = dataset_preprocessor.preprocess(files, input_path)
        sentencelist = dataset_preprocessor.extract_sentences(files, input_path)
        dataset_WeightsHandler.set_preprocessed_list(preprocessed_list)
        dataset_WeightsHandler.set_sentence_list(sentencelist)
        dataset_WeightsHandler.update_totfreq_dict()
        dataset_WeightsHandler.replace_totfreq_dict(dataset_FeatureReducer.reduceFeatures(dataset_WeightsHandler.tot_freq_dict()))
        dataset_WeightsHandler.generate_inv_doc_freq_dict(preprocessed_list)      
        dataset_WeightsHandler.generate_tot_weight_dict()    
        dataset_WeightsHandler.generate_STM()
      

if __name__ == '__main__':
    import sys
    input_path = sys.argv[1]
    summarizer = Summarizer()
    summarizer.summarize(input_path)
