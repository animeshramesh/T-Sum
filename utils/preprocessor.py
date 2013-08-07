import re,os
from nltk import stem



class Preprocessor:

    __text = []        # Private variable

    def return_stop_words(self):
        stop_words_filename = os.path.join(os.path.dirname(__file__), 'stopwords_reference')
        stopwords = open(stop_words_filename, 'r+').read()
        return stopwords

    def stop_word_eliminate(self, data):
        filtered_data = []
        stop_words = self.return_stop_words()
        text = data.split()
        for word in text:
            if stop_words.find(word) < 0:
                word=re.sub(r"[^\w\s]", '', word)
                filtered_data.append(word)
        return filtered_data


    def stem_word(self, data):
        stemmer = stem.snowball.EnglishStemmer()
        stemmed_data = " "
        for word in data:
            stemmed_data += stemmer.stem(word)+' '
        return stemmed_data

    def to_lower_case(self, data):
        return data.lower()

    def preprocess(self, data):
        filter1 = self.to_lower_case(data)
        filter2 = self.stop_word_eliminate(filter1)
        filter3 = self.stem_word(filter2)
        return filter3




