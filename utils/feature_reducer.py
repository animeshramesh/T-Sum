class FeatureReducer:

    def reduceFeatures(self, TermFreq_Dictionary):   
	for key,value in TermFreq_Dictionary.items():
	    if value == 1:
                del TermFreq_Dictionary[key]

	return TermFreq_Dictionary
