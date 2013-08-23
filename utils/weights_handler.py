from utils.preprocessor import Preprocessor
from utils.sentence_extractor import SentenceExtractor


class WeightsHandler:


    __tot_freq_dict = {}
    __inverse_doc_freq_dict = {}
    __tot_weight_dict = {}
    __sentenceList =[]
    __sentenceWeight_dict = {}
    __preprocessed_list = []
    __cosine_similarity_triangle = []


    def sentenceList(self):
        return self.__sentenceList

    def tot_freq_dict(self):
        return self.__tot_freq_dict

    def inverse_doc_freq(self):
        return self.__inverse_doc_freq_dict

    def tot_weight_dict(self):
        return self.__tot_weight_dict

    def sentenceWeight_dict(self):
        return self.__sentenceWeight_dict
    
    def preprocessed_list(self):
        return self.__preprocessed_list
    
    def set_preprocessed_list(self, preprocessed_list):
        self.__preprocessed_list = preprocessed_list
        
    def update_totfreq_dict(self):
        for row in self.__preprocessed_list:
            for word in row:
                if word in self.__tot_freq_dict:
                    self.__tot_freq_dict[word] += 1
                else:
                    self.__tot_freq_dict[word] = 1

    def replace_totfreq_dict(self, new_tot_freq_dict ):
        self.__tot_freq_dict = new_tot_freq_dict


    def generate_inv_doc_freq_dict(self, preprocessed_list):
        #from math import log
        for each_feature in self.__tot_freq_dict.keys():
            docs = 0
            for i in range(len(preprocessed_list)):
                if preprocessed_list[i].count(each_feature) > 0:
                    docs += 1
            self.__inverse_doc_freq_dict[each_feature] = (docs)

    def generate_tot_weight_dict(self):
        from math import log
        for each_feature in self.__tot_freq_dict.keys():
            self.__tot_weight_dict[each_feature] = self.__tot_freq_dict[each_feature] * (log(self.__inverse_doc_freq_dict[each_feature]))

    def update_sentenceList(self, document):
        sentence_extractor = SentenceExtractor()
        self.__sentenceList.extend(sentence_extractor.extract_sentences(document))

    def generate_STM(self):     # this function need to be updated. 
        for sentence in self.__sentenceList:
            preprocessed_words = []
            sentence_weight = []
            word_preprocessor = Preprocessor()
            for word in sentence.split():
                preprocessed_words.append(str(word_preprocessor.preprocess(word)))
            for feature in self.tot_weight_dict().keys():
                if feature in preprocessed_words:
                    sentence_weight.append(self.__tot_freq_dict[feature])
                else:
                    sentence_weight.append(0)
            self.__sentenceWeight_dict[sentence] = sentence_weight
    

class CosineRelationExtractor:
    
    def extract_cos_similarity(self, vector_dict):
        cosine_matrix = []
        for sentence1 in vector_dict.keys():
            magnitude1 = self.calculate_magnitude(vector_dict[sentence1])
            cos_values = []
            for sentence2 in vector_dict.keys():
                magnitude2 = self.calculate_magnitude(vector_dict[sentence2])
                dotproduct = self.calculate_dotproduct(vector_dict[sentence1], vector_dict[sentence2])
                cos_values.append(dotproduct / (magnitude1 * magnitude2))
            cosine_matrix.append(cos_values)
        return cosine_matrix
                
    def calculate_magnitude(self, vector):
        from math import sqrt
        sum_of_squares = 0
        for feature_weight in vector:
            sum_of_squares += (feature_weight*feature_weight)
        return (sqrt(sum_of_squares))
    
    def calculate_dotproduct(self, vector1, vector2):
        dotproduct = 0
        from pip.vendor.html5lib.serializer.htmlserializer import len
        for i in range(len(vector1)):
            dotproduct += ((vector1[i]) * (vector2[i]))
        return dotproduct
        
    
                
    

