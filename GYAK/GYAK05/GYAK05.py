import numpy as np
from scipy.stats import mode

class KNNClassifier():
    def __init__(self, k:int, test_split_ratio:float):
        self.k = k
        self.test_split_ratio = test_split_ratio

    #k_neighbors = self.k        #SZÁMTING VONG HÍR


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
            labels_pred = mode(distances[:k, 1], keepdims =False).mode
            labels_pred.append(labels_pred)
        self.y_preds = np.array(labels_pred, dtype=np.int64)



    def accuracy(self)->float:
        true_positive= (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) *100




