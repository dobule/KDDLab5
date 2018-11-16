from Corpus import *
from Document import *

import argparse

# parse arguments
parser = argparse.ArgumentParser()
# positional
parser.add_argument('rootdir', help='root directory of rutgers dataset')
# optional
parser.add_argument('-sw', '--stop-words', action='store', help='stop words file path')
parser.add_argument('-st', '--stem', action='store_true', help='enable stemming')
parser.add_argument('--ground-truth', action='store', help='ground truth output filename')
parser.add_argument('--output', action='store', help='vector output filename')
args = parser.parse_args()
ROOT_DIR = args.rootdir
STOP_WORDS = args.stop_words
STEMMING = args.stem
GT_OUTFILE = args.ground_truth
OUTPUT = args.output

# create corpus
corpus = Corpus(ROOT_DIR, STOP_WORDS, STEMMING)

# write ground truth to file
if GT_OUTFILE:
    with open(GT_OUTFILE, 'w') as f:
        conv_gt = [','.join(list(entry)) for entry in corpus.ground_truth()]
        f.write('\n'.join(conv_gt))

# write vectors to file
out_string = '\n'.join([doc.vector for doc in corpus.documents])
if OUTPUT:
    with open(OUTPUT, 'w') as f:
        f.write(out_string)
else:
    print(out_string)
