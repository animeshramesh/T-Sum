class SynonymAssigner:
    
    def assign_synonyms(self, sentence_list):
        synonym_dictionary = {}
        from nltk.corpus import wordnet as wn
        for sentence in sentence_list:
            for word in sentence.split():
                synonyms = [x for x in wn.synsets(word)]
                synonym_dictionary[word] = synonyms
        return synonym_dictionary