from utils.preprocessor import Preprocessor
prep = Preprocessor()

class Size:
    
    def calculate_size_of_set(self,sentence_list):
        length_of_each_sentence = []
        preprocessed_words_in_each_sentence = []
        for s in sentence_list:
            arr = prep.preprocess_sentence(s)
            preprocessed_words_in_each_sentence.append(arr)
            length_of_each_sentence.append(len(arr))
        return length_of_each_sentence