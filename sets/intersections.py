class Intersections:
    
    def count_itersections_of_each_set(self, preprocessed_words_in_each_sentence):
        number_of_intersections_of_each_sentence = []
        for collections1 in preprocessed_words_in_each_sentence:
            intersections = 0
            for term1 in collections1:
                intersections -= 1
                for collection2 in preprocessed_words_in_each_sentence:
                    if term1 in collection2:
                        intersections += 1
            number_of_intersections_of_each_sentence.append(intersections)
        return number_of_intersections_of_each_sentence