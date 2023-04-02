import numpy as np
from scipy.stats import mode
from sklearn.metrics import confusion_matrix

class KNNClassifier():
    def __init__(self, k:int, test_split_ratio:float):
        self.k = k
        self.test_split_ratio = test_split_ratio

    @property
    def k_neighbors(self) -> int:
        return self.k

    def confusion_matrix(self) -> np.ndarray:
        return confusion_matrix(self.y_test, self.y_preds)

    @staticmethod
    def load_csv(cs_path : str):
        np.random.seed(42)
        dataset = np.genfromtxt(cs_path, delimiter=',')
        np.random.shuffle(dataset)
        x,y = dataset[:, :-1],dataset[:, -1]
        return x,y

    def train_test_splitting(self, features: np.ndarray, labels: np.ndarray,):
        
        test_size = int(len(features) * self.test_split_ratio)

        train_size = len(features)-test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        self.x_train, self.y_train = features[:train_size, :], labels[:train_size]
        self.x_test, self.y_test = features[train_size:, :], labels[train_size:]

    
    
    def euclidean(self, element_of_x: np.ndarray) -> np.ndarray:
        return np.sqrt(np.sum((self.x_train - element_of_x)**2, axis=0))
    


    def predict(self, x_test: np.ndarray):
        labels_pred = []
        for x_test_element in x_test:
            # Táv
            distances = self.euclidean(self.x_train, x_test_element)
            distances = np.array(sorted(zip(distances, self.y_train)))
            #Leggyakoribb value
            #dist móduszán
            labels_pred = mode(distances[:self.k, 1], keepdims =False).mode
            labels_pred.append(labels_pred)
        self.y_preds = np.array(labels_pred, dtype=np.int64)



    def accuracy(self)->float:
        true_positive= (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) *100