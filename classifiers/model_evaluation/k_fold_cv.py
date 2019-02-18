import numpy as np
import pandas as pd


class KFoldCrossValidator:
    def __init__(self, n_folds, classifier, df, domain):
        self.n_folds = n_folds
        self.classifier = classifier
        self.df = df
        self.domain = domain
        self.n = len(self.domain.category.values)
        self.confusion_matrix = np.zeros((self.n, self.n))

    def pretty_confusion_matrix(self):
        return pd.DataFrame(self.confusion_matrix, self.domain.category.values, self.domain.category.values)

    def accuracy(self):
        return np.trace(self.confusion_matrix) / np.sum(self.confusion_matrix)

    def generate_confusion_matrix(self, test, predictions):
        confusion_matrix = np.zeros((self.n, self.n))

        for expected, predicted in zip(test[self.domain.category.name], predictions):
            row = self.domain.category.values.index(predicted)
            col = self.domain.category.values.index(expected)
            confusion_matrix[row][col] += 1

        return confusion_matrix

    def cross_validate(self):
        slices = np.array_split(self.df, self.n_folds)
        for fold in list(range(self.n_folds)):
            train = pd.concat(slices[:fold] + slices[(fold + 1):])
            test = slices[fold]
            self.classifier.fit(train, self.domain)
            predictions = self.classifier.predict(test)
            self.confusion_matrix += self.generate_confusion_matrix(test, predictions)











