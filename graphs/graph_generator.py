class GraphGenerator:
    
    def generate_graph(self, cosine_matrix):
        graph_matrix = []
        for row in cosine_matrix:
            each_row = []
            for cosine_value in row:
                if cosine_value < 0.3:
                    each_row.append(0)
                else:
                    each_row.append(cosine_value)
            graph_matrix.append(each_row)
        return graph_matrix