from __future__ import division
from utils.sentence_extractor import SentenceExtractor
import sys

sentence_extractor = SentenceExtractor()
gold_file = sys.argv[1]
peer_file = sys.argv[2]

gold_text = open(gold_file,'r+').read()
peer_text = open(peer_file,'r+').read()

gold_sentences = sentence_extractor.extract_sentences(gold_text)
peer_sentences = sentence_extractor.extract_sentences(peer_text)

tp = 0  #True positive
fp =0   #False positive
fn=0    #False negative

for sentence in peer_sentences:
    if sentence in gold_sentences:
        tp = tp + 1
    else:
        print sentence
        fp = fp + 1
        
        
for sentence in gold_sentences:
    if sentence not in peer_sentences:
        fn = fn + 1
    
precision = tp / (tp + fp)
recall = tp / (tp + fn)

sys.stdout.write("\n\nPrecision = "+str(precision))
sys.stdout.write("\nRecall = "+str(recall)+'\n\n')
