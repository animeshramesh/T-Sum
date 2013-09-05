from utils.preprocessor import Preprocessor
from utils.synonym_assigner import SynonymAssigner
from utils.feature_reducer import FeatureReducer
from utils.weights_handler import WeightsHandler
from graphs.sine_relation_extractor import SineRelationExtractor

from graphs.dissimilarity_scorer import DissimilarityScorer
from graphs.node_ranker import NodeRanker
import os

class Summarizer:

    def summarize(self,input_path):
        dataset_preprocessor = Preprocessor()
        dataset_FeatureReducer = FeatureReducer()
        dataset_WeightsHandler = WeightsHandler()
        
        
        files = [f for f in os.listdir(input_path) if os.path.isfile(input_path + f)]
        
        preprocessed_list = dataset_preprocessor.preprocess(files, input_path)
        sentencelist = dataset_preprocessor.extract_sentences(files, input_path)
        
        print sentencelist
        
        dataset_WeightsHandler.set_preprocessed_list(preprocessed_list)
        dataset_WeightsHandler.set_sentence_list(sentencelist)
        dataset_WeightsHandler.update_totfreq_dict()
        dataset_WeightsHandler.replace_totfreq_dict(dataset_FeatureReducer.reduceFeatures(dataset_WeightsHandler.tot_freq_dict()))
        dataset_WeightsHandler.generate_inv_doc_freq_dict(preprocessed_list)      
        dataset_WeightsHandler.generate_tot_weight_dict()    
        dataset_WeightsHandler.generate_STM()
        
        vector_dict = dataset_WeightsHandler.sentence_weight_dict() #vector_dict[sentence]=vector
        
        dataset_FeatureReducer.remove_features_with_zero_weight(vector_dict)
        sentencelist = dataset_preprocessor.remove_stop_words_from_sentencelist(sentencelist) 
        
        print sentencelist
      
        
        VectorSineRelationExtractor = SineRelationExtractor()
        sine_matrix = VectorSineRelationExtractor.extract_sine_similarity(vector_dict)
        
            
          
        synonym_assigner = SynonymAssigner()
        synonym_dict = synonym_assigner.assign_synonyms(sentencelist)
    
        
        SentenceDissimilarityScorer = DissimilarityScorer()
        dissimilarity_matrix = SentenceDissimilarityScorer.assign_dissimilarity_score(synonym_dict, sentencelist)
        dissimilarity_matrix = SentenceDissimilarityScorer.multiply_sine(dissimilarity_matrix, sine_matrix)
        
        
        
        SentenceRanker = NodeRanker()
        scorelist_of_sentences= SentenceRanker.calculate_score_of_each_sentence(dissimilarity_matrix)
        ranked_indices = SentenceRanker.rank_nodes(scorelist_of_sentences)
        
        #for each_index in ranked_indices:
        #    print sentencelist[each_index]
        
      

if __name__ == '__main__':
    import sys
    input_path = sys.argv[1]
    summarizer = Summarizer()
    summarizer.summarize(input_path)
