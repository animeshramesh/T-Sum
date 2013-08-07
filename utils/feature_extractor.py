__author__ = 'Animesh'


from utils.file_reader import FileReader
from utils.file_writer import FileWriter
from utils.preprocessor import Preprocessor
from os import path


class FeatureExtractor:

    __all_features = " "
    __total_documents = 0

    def extract(self):
        dataset_input_handler = FileReader()
        dataset_output_handler = FileWriter()
        dataset_preprocessor = Preprocessor()
        i = 1
        while 1:
            try:
                with open('%d.txt' % i):
                    inputdataset = dataset_input_handler.read('%d.txt' % i)
                    preprocessed_data = dataset_preprocessor.preprocess(inputdataset)
                    dataset_output_handler.write('out%i.txt' % i, preprocessed_data)
                    self.__all_features += preprocessed_data + ' '
                    i += 1
            except IOError:
                break
        self.__total_documents = i-1

    
    def all_features(self):
        return self.__all_features

    def total_documents(self):
        return self.__total_documents

