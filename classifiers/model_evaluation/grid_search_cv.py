import itertools as it
import numpy as np
import pandas as pd


class GridSearchOptimizer:
    def __init__(self, classifier, scorer, param_dict, n_folds):
        self.classifier = classifier
        self.scorer = scorer
        self.param_dict = param_dict
        self.param_combos = self.generate_param_combos(param_dict)
        self.n_folds = n_folds
        self.scores = np.zeros(len(self.param_combos), dtype=np.float32)

    @staticmethod
    def generate_param_combos(param_dict):
        keys = param_dict
        combos = it.product(*(param_dict[key] for key in keys))
        return list(combos)

    def fit(self, df, domain):
        for i, combo in enumerate(self.param_combos):
            args = dict(zip(self.param_dict.keys(), combo))
            classifier = self.classifier(**args)
            classifier.fit(df, domain)
            scorer = self.scorer(self.n_folds, classifier, df, domain)
            scorer.cross_validate()
            self.scores[i] = scorer.accuracy()

    def best_parameters(self):
        return dict(zip(self.param_dict.keys(), self.param_combos[self.scores.argmax()]))

    def best_score(self):
        return self.scores.max()

    def score_parameter_detail(self):
        return pd.DataFrame([list(combo) + [score] for combo, score in list(zip(self.param_combos, self.scores.tolist()))], columns=list(self.param_dict.keys()) + ["score"])
