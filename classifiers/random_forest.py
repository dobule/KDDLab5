import random
from classifiers.C45 import *

USAGE_MESSAGE = "python runRF.py <trainingDataFile> <numAttributes> <numDataPoints> <NumTrees>"


class RandomForest:
    def __init__(self, n_data_points, n_attributes, n_trees, c_thresh=0.1):
        self.df = None
        self.c_thresh = c_thresh
        self.n_data_points = n_data_points
        self.n_attributes = n_attributes
        self.n_trees = n_trees
        self.domain = None
        self.trees = []

    def fit(self, df, domain):
        self.df = df
        self.domain = domain
        subsets = [self.select_random_subset() for _ in list(range(self.n_trees))]
        c45 = C45(self.c_thresh)
        for subset in subsets:
            c45.fit(subset, self.domain)
            self.trees.append(c45.tree)

    def select_random_subset(self):
        data_points = self.df.sample(n=self.n_data_points, replace=True)
        random_cols = [self.domain.attributes[i].name for i
                       in random.sample(range(len(self.domain.attributes)), self.n_attributes)]
        random_cols.append(self.domain.category.name)
        return data_points[random_cols]

    def predict(self, records):
        categories = self.domain.category.values
        predictions = []
        for i, record in records.iterrows():
            votes = np.zeros(len(self.domain.category.values))
            for tree in self.trees:
                result = classify_record(record, tree.root, self.domain)
                if result is not None:
                    votes[categories.index(result)] += 1
            predictions.append(categories[np.argmax(votes)])
        return predictions


def parse_args(argv):
    if len(argv) != 5:
        print(USAGE_MESSAGE)
        exit(0)

    data_filename = argv[1]
    num_attributes = int(argv[2])
    num_data_points = int(argv[3])
    num_trees = int(argv[4])

    return data_filename, num_attributes, num_data_points, num_trees
