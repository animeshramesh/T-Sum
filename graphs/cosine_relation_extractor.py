class CosineRelationExtractor:
    
    def extract_cos_similarity(self, vector_dict):
        cosine_matrix = []
        for sentence1 in vector_dict.keys():
            cos_values = []
            for sentence2 in vector_dict.keys():
                dotproduct = self.calculate_dotproduct(vector_dict[sentence1], vector_dict[sentence2])
                cos_values.append(dotproduct)
            cosine_matrix.append(cos_values)
        return cosine_matrix
                
    def calculate_magnitude(self, vector):
        from math import sqrt
        sum_of_squares = 0
        for feature_weight in vector:
            sum_of_squares += (feature_weight*feature_weight)
        return (sqrt(sum_of_squares))
    
    def calculate_dotproduct(self, vector1, vector2):
        dotproduct = 0
        for i in range(len(vector1)):
            dotproduct += ((vector1[i]) * (vector2[i]))
        dotproduct /= self.calculate_magnitude(vector1)
        dotproduct /= self.calculate_magnitude(vector2)
        return dotproduct
        
    
                
    

