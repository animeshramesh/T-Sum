class Size:
    
    def calculate_size_of_set(self,preprocessed_words_in_each_sentence):
        size_of_sets = []
        for i in range(len(preprocessed_words_in_each_sentence)):
            size_of_sets.append(len(preprocessed_words_in_each_sentence[i]))
        return size_of_sets