class FeatureReducer:

    def reduceFeatures(self, TermFreq_Dictionary):
        for key, value in TermFreq_Dictionary.items():
            if value == 1:
                del TermFreq_Dictionary[key]

        return TermFreq_Dictionary
    
    def remove_features_with_zero_weight(self, tot_weight_dict):
        for key,value in tot_weight_dict.items():
            if value == 0:
                del tot_weight_dict[key]
        return tot_weight_dict

