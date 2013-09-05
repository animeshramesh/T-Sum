class DissimilarityScorer:
    
    def assign_dissimilarity_score(self, synonym_dict, sentence_list):
        dissimilarity_matrix = []
        for sentence1 in sentence_list:
            sentence_dissimilarity = []
            for sentence2 in sentence_list:
                dissimilarity_score = 0
                number_of_comparisons = len(sentence1.split()) * len(sentence2.split())
                for word1 in sentence1.split():
                    word1_synsets = synonym_dict[word1]
                    for word2 in sentence2.split():
                        word2_synsets = synonym_dict[word2]
                        if word1 != word2:
                            dissimilarity_score += (1 - self.calculate_max_wup_similarity(word1_synsets, word2_synsets))
                sentence_dissimilarity.append(dissimilarity_score/number_of_comparisons)
               
            dissimilarity_matrix.append(sentence_dissimilarity)
        return dissimilarity_matrix
                
                        
    def calculate_max_wup_similarity(self, word1_synsets, word2_synsets):
        max_similarity = 0
        for syns1 in word1_synsets:
            for syns2 in word2_synsets:
                similarity_score = syns1.wup_similarity(syns2)
                if similarity_score > max_similarity:
                    max_similarity = similarity_score
        return max_similarity
 
 
    def multiply_sine(self, dissimilarity_matrix, sine_matrix):
        for i in range(len(sine_matrix)):
            for j in range(len(sine_matrix[i])):
                dissimilarity_matrix[i][j] *= sine_matrix[i][j]
        return dissimilarity_matrix
        
        