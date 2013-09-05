class SineRelationExtractor:
    
    def extract_sine_similarity(self, vector_dict):
        sine_matrix = []
        for sentence1 in vector_dict.keys():
            sine_values = []
            for sentence2 in vector_dict.keys():
                dotproduct = self.calculate_dotproduct(vector_dict[sentence1], vector_dict[sentence2])
                from math import sqrt
                if (1-(dotproduct*dotproduct)) < 0.09:
                    sine_values.append(0)
                else:
                    sine_values.append(sqrt(1-(dotproduct*dotproduct)))
            sine_matrix.append(sine_values)
        return sine_matrix
                
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
