from sklearn.datasets import load_digits

class KMeansOnDigits():
    def __init__(self, n_clusters = 10, random_state = 42) -> None:
        self.n_clusters = n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = load_digits()

    def predict(self):
        pass

    def get_labels(self):
        pass

    def calc_accuracy(self):
        pass

    def confusion_matrix(self):
        pass