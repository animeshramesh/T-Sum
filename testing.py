from utils.preprocessor import Preprocessor
import os
from sets.size import Size
from sets.intersections import Intersections
from sets.scorer import Scorer
from graphs.node_ranker import NodeRanker
from sets.distributed_ranks import RankDistributor



input_path = '/home/animesh/T-Sum/Data sets/Inception/'
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
rank_counter_in_0_to_1 = RankDistributor()

size_of_sets = size.calculate_size_of_set(preprocessed_words_in_each_sentence)
number_of_intersections_of_each_sentence = intersections.count_itersections_of_each_set(preprocessed_words_in_each_sentence)
scores = scorer.score_sentences(number_of_intersections_of_each_sentence, size_of_sets)

normalised_scores = scorer.normalise_score(scores)
distributed_ranks = rank_counter_in_0_to_1.distribute_ranks(normalised_scores)
print distributed_ranks

ranklist = ranker.rank_sentences(scores)
i = 0
with open('peer_summary.html','w') as f:
    f.write(''''<html>\n<head>\n<title>\npeer_Summary</title> </head><body bgcolor="white">\n''')     
    for rank in ranklist:
        if rank < 0.1 :
            break
        i += 1
        f.write('''<a name="%d">[%d]</a> <a href="#%d" id=%d>'''%(i,i,i,i) + sentence_list[rank])
        f.write('\n')
    f.write('</a>\n</body>\n</html>\n')
    

                
                
        
    

    
    