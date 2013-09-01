class SineNormaliser:
    
    def normalise_sine_matrix(self, sine_matrix):
        graph_matrix = []
        for each_row in sine_matrix:
            row = []
            for sine_value in each_row:
                if sine_value < 0.3:
                    row.append(0)
                else:
                    row.append(sine_value)
            graph_matrix.append(each_row)
        return graph_matrix
    