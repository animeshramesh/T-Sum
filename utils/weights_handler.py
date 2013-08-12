from utils.file_reader import FileReader
from utils.preprocessor import Preprocessor
from utils.sentence_extractor import SentenceExtractor


class WeightsHandler:


    __tot_freq_dict = {}
    __inverse_doc_freq_dict = {}
    __tot_weight_dict = {}
    __sentenceList =[]
    __sentenceWeight_dict = {}
    __original_word_totweight_dict = {}


    def sentenceList(self):
        return self.__sentenceList

    def tot_freq_dict(self):
        return self.__tot_freq_dict

    def inverse_doc_freq(self):
        return self.__inverse_doc_freq_dict

    def tot_weight_dict(self):
        return self.__tot_weight_dict

    def original_word_totweight_dict(self):
        return self.__original_word_totweight_dict

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

    def generate_tot_weight_dict(self):
        for each_feature in self.__tot_term_freq_dict.keys():
            self.__tot_weight_dict[each_feature] = self.__tot_freq_dict[each_feature] + self.__inverse_doc_freq_dict[each_feature]

    def update_sentenceList(self, document):
        sentence_extractor = SentenceExtractor()
        self.__sentenceList.extend(sentence_extractor.extract_sentences(document))

    def update_original_word_totweight_dict(self, preprocessed_word_dict):
        for sentence in self.__sentenceList:
            for word in sentence.split():
                if word in preprocessed_word_dict.keys():
                    self.__original_word_totweight_dict[word] = self.__tot_weight_dict[preprocessed_word_dict[word]]