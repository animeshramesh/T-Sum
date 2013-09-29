from __future__ import division
class Scorer:
    
    max = -1.0
    
    def score_sentences(self,number_of_intersections_of_each_sentence,size_of_sets):
        scores = []
        for i in range(len(size_of_sets)):
            scores.append(number_of_intersections_of_each_sentence[i]*size_of_sets[i])
            if scores[i]>self.max:
                self.max = scores[i]
        return scores
    
    def normalise_score(self, scores):
        normalised_score = []
        for each_score in scores:
            normalised_score.append((each_score/self.max))
        return normalised_score
    