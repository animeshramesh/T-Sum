class NodeRanker:
    
    def calculate_score_of_each_sentence(self, dissimilarity_matrix):
        scorelist_of_sentences = []
        for each_row in dissimilarity_matrix:
            sum_of_elements = 0
            for each_cell in each_row:
                sum_of_elements += each_cell
            scorelist_of_sentences.append(sum_of_elements)
        return scorelist_of_sentences
    
    def rank_nodes(self, scorelist_of_sentences):
        ranklist = []
        for i in range(len(scorelist_of_sentences)):
            max_value = -1
            pos = 0
            for j in range(len(scorelist_of_sentences)):
                if scorelist_of_sentences[j] > max_value:
                    max_value = scorelist_of_sentences[j]
                    pos = j
            ranklist.append(pos)
            scorelist_of_sentences[pos] = -1
        return ranklist
            
            
        