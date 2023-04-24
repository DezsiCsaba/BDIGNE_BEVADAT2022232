import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr
        self.m = 0
        self.c = 0


    def fit(self, X: np.array, y: np.array):
        
        n = float(len(X)) # Number of elements in X

        # Performing Gradient Descent 
        self.losses = []
        for i in range(self.epochs): 
            y_pred = self.m*X + self.c  # The current predicted value of Y

            residuals = y - y_pred
            loss = np.sum(residuals ** 2)
            self.losses.append(loss)
            D_m = (-2/n) * sum(X * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            self.m = self.m - self.lr * D_m  # Update m
            self.c = self.c - self.lr * D_c  # Update c
            if i % 100 == 0:
                print(np.mean(y-y_pred))
        return self.losses
            

    def predict(self, X_test):
        # Run the model on the test set
        #self.pred = []
        #for X in self.X_test:
        #    y_pred = self.m*X + self.c
        #    self.pred.append(y_pred)
        #print(self.pred)
        #print(self.y_test)
        return self.m * X_test + self.c

    def evaluate(self, x, y):
        pred = self.predict(x)
        err = np.mean((pred - y) ** 2)
        return f"Mean squared error: {err}"