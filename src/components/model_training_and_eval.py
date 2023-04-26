import os
import sys
import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
from src.utils import evaluate_model
from dataclasses import dataclass

@dataclass
class ModelEvaluationConfig:
    best_score_model_path = os.path.join("artifacts", "best_score_model.pkl")

class Model_Evaluation_Initiated:

    def __init__(self):
        self.Model_Evaluation_Initiated = ModelEvaluationConfig()

    def Model_Training(self,train_data,test_data):
        try:
            logging.info("Model training is initiated...")
            logging.info("Splitting up the Training data array and testing data array into X_train,X_test,y_train,y_test")
            
            X_train= train_data[:,:-1]
            y_train= train_data[:,-1]

            X_test= test_data[:,:-1]
            y_test= test_data[:,-1]

            logging.info("Fitting the models on training data using evaluate function from utils...")

            models={
                "LinearRegression":LinearRegression(),
                "Lasso regression":Lasso(),
                "Ridge regression":Ridge(),
                "ElasticNet Regression":ElasticNet()
            }

            best_score_model,r2score_dict =evaluate_model(models,X_train,y_train,X_test,y_test)
            logging.info(f"R2 scores for all the models is as follows: \n\n {r2score_dict}")
            save_object(self.Model_Evaluation_Initiated.best_score_model_path,best_score_model)

            logging.info("Model Training is Successful")

            return (self.Model_Evaluation_Initiated.best_score_model_path)
        
        except Exception as e:
            logging.info("Exception occurred inside Model_Evaluation_Initiated")
            logging.info(e)
            raise CustomException(e)

