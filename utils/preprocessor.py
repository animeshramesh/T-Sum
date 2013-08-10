import re,os
from nltk import stem



class Preprocessor:

    __text = []        # Private variable
    __preprocessed_words_dict = {}

    def return_stop_words(self):
        stop_words_filename = os.path.join(os.path.dirname(__file__), 'stopwords_reference')
        stopwords = open(stop_words_filename, 'r+').read()
        return stopwords

    def stop_word_eliminate(self, word_in_dataset):
        stop_words = self.return_stop_words()

        if stop_words.find(word_in_dataset) < 0:
            word=re.sub(r"[^\w\s]", '', word_in_dataset)
            return word
        else:
            pass


    def stem_word(self, word_in_dataset):
        stemmer = stem.snowball.EnglishStemmer()
        stemmed_word = stemmer.stem(word_in_dataset)
        return stemmed_word

    def to_lower_case(self, data):
        return data.lower()

    def assign_preprocessed_words_to_dict(self, original_word, preprocessed_word):
        if original_word not in self.return_stop_words():
            if original_word not in self.__preprocessed_words_dict:
                self.__preprocessed_words_dict[original_word] = str(preprocessed_word)


    def preprocess(self, data):
        filter1 = self.to_lower_case(data)
        filter2 = self.stop_word_eliminate(filter1)
        filter3 = self.stem_word(filter2)
        for word in data.split():
            self.assign_preprocessed_words_to_dict(word, filter3)
        return filter3

