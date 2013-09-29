
class RankDistributor:
    
    def distribute_ranks(self,normalised_scores):
        distributed_ranks = [0,0,0,0,0,0,0,0,0,0]
        for val in normalised_scores:
            if val>0 and val<=0.1:
                distributed_ranks[0] += 1
            if val>0.1 and val<=0.2:
                distributed_ranks[1] += 1
            if val>0.2 and val<=0.3:
                distributed_ranks[2] += 1
            if val>0.3 and val<=0.4:
                distributed_ranks[3] += 1
            if val>0.4 and val<=0.5:
                distributed_ranks[4] += 1
            if val>0.5 and val<=0.6:
                distributed_ranks[5] += 1
            if val>0.6 and val<=0.7:
                distributed_ranks[6] += 1
            if val>0.7 and val<=0.8:
                distributed_ranks[7] += 1
            if val>0.8 and val<=0.9:
                distributed_ranks[8] += 1
            if val>0.9 and val<=1:
                distributed_ranks[9] += 1
        return distributed_ranks
