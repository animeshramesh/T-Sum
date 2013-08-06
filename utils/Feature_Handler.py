__author__ = 'Animesh'

from utils import IOHandler
from utils.preprocessor import Preprocessor

class feature_handler:

    __all_features = " "
    __unique_features = []
    __total_documents = 0

    def extract_features_from_dataset(self):
        dataset_input_handler = IOHandler.input_handler()
        dataset_output_handler = IOHandler.output_handler()
        dataset_preprocessor = Preprocessor()
        i = 1
        while 1:
            try:
                with dataset_input_handler.open_file('%d.txt' % i):
                    inputdataset = dataset_input_handler.input_from_file('%d.txt' % i)
                    preprocessed_data = Preprocessor.preprocess(inputdataset)
                    dataset_output_handler.write_to_file('out%i.txt' % i, preprocessed_data)
                    self.__all_features += preprocessed_data + ' '
                    i += 1
            except IOError:
                break
        self.__total_documents = i-1

    def generate_unique_features(self,data):
        for each_word in data.split():
            if each_word not in self.__unique_features:
                self.__unique_features.append(each_word)



