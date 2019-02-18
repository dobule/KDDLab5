import numpy as np


class KNN:
    def __init__(self, k):
        self.k = k
        self.data = None
        self.trained_set = None
        self.domain = None

    def euclidean_dist(self, i, x_train, x_test):
        return np.sqrt(np.sum(np.square(x_test - x_train[i, :])))

    def fit(self, train_data, domain):
        self.trained_set = train_data
        self.domain = domain
        return

    def predict(self, test_data):
        dists, results = [], []
        x_train = np.array(self.trained_set.drop([self.domain.category.name], axis=1))
        y_train = np.array(self.trained_set[self.domain.category.name])
        x_test = np.array(test_data.drop([self.domain.category.name], axis=1))
        predictions = []
        for i in range(x_test.shape[0]):
            for i in range(x_train.shape[0]):
                dist = self.euclidean_dist(i, x_train, x_test)
                dists.append([dist, i])
            dists = sorted(dists)

            for i in range(self.k):
                index = dists[i][1]
                results.append(y_train[index])

            unique, counts = np.unique(np.array(results), return_counts=True)
            predictions.append(unique[np.argmax(counts)])
        return predictions



