from utils.preprocessor import Preprocessor
import os
from sets.size import Size
from sets.intersections import Intersections
from sets.scorer import Scorer
from graphs.node_ranker import NodeRanker


input_path = '/home/animesh/workspace/T-Sum/Data sets/India/'
files = [f for f in os.listdir(input_path) if os.path.isfile(input_path + f)]
prep = Preprocessor()
sentence_list = prep.extract_sentences(files, input_path)
preprocessed_words_in_each_sentence = []

for s in sentence_list:
    preprocessed_words_in_each_sentence.append(prep.preprocess_sentence(s)) 

size = Size()
intersections = Intersections()
scorer = Scorer()
ranker = NodeRanker()

size_of_sets = size.calculate_size_of_set(preprocessed_words_in_each_sentence)
number_of_intersections_of_each_sentence = intersections.count_itersections_of_each_set(preprocessed_words_in_each_sentence)
scores = scorer.score_sentences(number_of_intersections_of_each_sentence, size_of_sets)

normalised_scores = scorer.normalise_score(scores)

ranklist = ranker.rank_sentences(scores)

for rank in ranklist:
    print sentence_list[rank]
    
    

                
                
        
    

    
    