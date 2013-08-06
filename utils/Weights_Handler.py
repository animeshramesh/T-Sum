from utils.preprocessor import Preprocessor
from sys import stdout
from math import log
from utils.IOHandler import input_handler
from utils import Feature_Handler


class Weights_Handler:

    __tot_frequency = []
    __term_freq_matrix = []
    __inverse_document_freq = []
    __tot_words_in_each_doc = []
    __TFIDF = []

    def tot_frequency(self):
        return self.__tot_freq

    def generate_total_frequency(self, unique_features, all_features):
        for word in unique_features:
            self.__tot_frequency.append(all_features.count(word))

    def generate_term_freq_matrix(self, number):
        for i in range(1, number):
            file_data = input_handler.input_from_file('out%i.txt' % i)
            arr = []
            for each_word in Feature_Handler.feature_handler.unique_features:
                arr.append(file_data.count(each_word))
            self.__term_freq_matrix.append(arr)

    def term_freq_matrix(self):
        return self.__term_freq_matrix

    def generate_inverse_document_freq(self, total_docs, unique_features):
        for each_word in Feature_Handler.feature_handler.unique_features:
            docs = 0
            for i in range(1, total_docs):
                input_data = input_handler.input_from_file('out%i.txt' % i)
                if input_data.count(each_word) > 0:
                    docs += 1
            self.__inverse_document_freq.append(docs)

    def inverse_document_freq(self):
        return self.__inverse_document_freq

    def generate_tot_features_in_each_doc(self, tot_files):
        for i in range(1, tot_files):
            input_data = input_handler.input_from_file('out%i.txt' % i)
            self.__tot_words_in_each_doc.append(len(input_data.split()))

    '''def update_TFIDF(self, tot_docs, tot_features):
        for i in range(1, tot_docs):
            temp_arr = []
            for j in range(1, tot_features):
                idf = log(tot_docs / weights.__inverse_document_freq[j])
                temp_arr.append(self.__term_freq_matrix[i][j] / self.__tot_words_in_each_doc[i] * idf)
            self.__TFIDF.append(temp_arr)'''


