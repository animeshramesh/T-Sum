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

    def extract(self):
        #This function is doing too much stuff. Need to separate the tasks.
        # Removing implementation of directories

        dataset_Reader = FileReader()
        dataset_preprocessor = Preprocessor()
        dataset_WeightsHandler = WeightsHandler()
        i = 1
        while 1:
            try:
                with open('%d.txt' % i):

                    inputdataset = dataset_Reader.read('%d.txt' % i)
                    print inputdataset
                    dataset_WeightsHandler.update_sentenceList(inputdataset)

                    preprocessed_data = []
                    for word in inputdataset.split():
                        preprocessed_data.append(dataset_preprocessor.preprocess(word))

                    for j in range(len(preprocessed_data)):
                        dataset_WeightsHandler.update_totfreq_dict(preprocessed_data[j])

                    i += 1

            except IOError:
                break

        self.__total_documents = i - 1


    def total_documents(self):
        return self.__total_documents


obj = FeatureExtractor()
obj.extract()

