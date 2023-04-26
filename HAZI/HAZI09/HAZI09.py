from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
import numpy as np

from sklearn.decomposition import PCA

class KMeansOnDigits():
    def __init__(self, n_clusters = 10, random_state = 42) -> None:
        self.n_clusters = n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = load_digits()

    def predict(self):
        self.model = KMeans(
            n_clusters=self.n_clusters,
            random_state=self.random_state,
            init='random'
        )

        pca = PCA(2)
        reduced = pca.fit_transform(self.digits)
        print(reduced.shape)

        X,y = self.digits.data, self.digits.target
        labels = self.model.fit_predict(reduced)
        unique_lab = np.unique(labels)

        self.centroids = self.model.cluster_centers_

        return self.centroids


    def get_labels(self):
        pass

    def calc_accuracy(self):
        pass

    def confusion_matrix(self):
        pass