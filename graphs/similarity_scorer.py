'''
Created on Aug 27, 2013

@author: animesh
'''
class SimilarityScorer:
    
    def assign_similarity_score(self, synonym_dict, sentence_list): #incom
        for sentence1 in sentence_list:
            for word1 in sentence1.split():
                word1_synsets = synonym_dict[word1]
                for sentence2 in sentence_list:
                    for word2 in sentence2.split():
                        word2_synsets = synonym_dict[word2]
                        
                        
    def max_wup_similarity(self, word1_synsets, word2_synsets):
        from nltk.corpus import wordnet
        max_similarity = 0
        for syns1 in word1_synsets:
            wordnet_syns1 = wordnet.synset(syns1)
            for syns2 in word2_synsets:
                wordnet_syns2 = wordnet_syns1.synset(syns2)
                similarity_score = wordnet_syns1.wup_similarity(wordnet_syns2)
                if similarity_score > max_similarity:
                    max_similarity = similarity_score
        return max_similarity