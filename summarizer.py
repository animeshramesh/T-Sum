__author__ = 'Animesh'

from utils.file_reader import FileReader
from utils.file_writer import FileWriter
from utils.preprocessor import Preprocessor
from utils.sentence_extractor import SentenceExtractor
from utils.feature_reducer import FeatureReducer
from utils.weights_handler import WeightsHandler

tot_docs = 0

dataset_Reader = FileReader()
dataset_output_handler = FileWriter()
dataset_preprocessor = Preprocessor()
dataset_WeightsHandler = WeightsHandler()
dataset_FeatureReducer = FeatureReducer()
dataset_directory = raw_input()
i = 1
while 1:
    try:
        with open(dataset_directory + '%d.txt' % i):
            inputdataset = dataset_Reader.read(dataset_directory + '%d.txt' % i)
            dataset_WeightsHandler.update_sentenceList(inputdataset)
            preprocessed_data = []
            for word in inputdataset.split():
                word = word.lower()
                if word not in dataset_preprocessor.stop_words():
                    preprocessed_data.append(str(dataset_preprocessor.preprocess(word)))
                # To lower and stop-word elimination above required for removing 'none' in dictionary
            dataset_output_handler.write(dataset_directory + 'out%d.txt' % i, preprocessed_data)
            for j in range(len(preprocessed_data)):
                dataset_WeightsHandler.update_totfreq_dict(preprocessed_data[j])
            i += 1

    except IOError:
        break

total_documents = i - 1
dataset_WeightsHandler.replace_totfreq_dict(dataset_FeatureReducer.reduceFeatures(dataset_WeightsHandler.tot_freq_dict()))
dataset_WeightsHandler.generate_inv_doc_freq_dict(total_documents, dataset_directory)
dataset_WeightsHandler.generate_tot_weight_dict()
dataset_WeightsHandler.generate_STM()
print dataset_WeightsHandler.sentenceWeight_dict()

