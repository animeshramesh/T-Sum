import re,os
from nltk import stem
import string


class Preprocessor:

    def stop_words(self):
        stop_words_filename = os.path.join(os.path.dirname(__file__), 'stopwords_reference')
        stopwords = open(stop_words_filename, 'r+').read()
        return stopwords

    def regularise_expression(self, word_in_dataset):
        word = re.sub(r'[^\w\s]', ' ', word_in_dataset)
        return word


    def stem_word(self, word_in_dataset):
        stemmer = stem.snowball.EnglishStemmer()
        stemmed_word = stemmer.stem(str(word_in_dataset))
        return stemmed_word

    def to_lower_case(self, data):
        return data.lower()

    def preprocess(self, data):
        filter1 = self.to_lower_case(data)
        filter2 = self.regularise_expression(filter1)
        filter3 = self.stem_word(filter2)
        return str(filter3)

