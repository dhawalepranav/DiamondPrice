import pickle
import os
import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


def save_object(filepath, object):
    try:
        logging.info("Saving the object in pickle file")
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)

        with open(filepath,'wb') as f:
            pickle.dump(object,f)
        logging.info("Object has been saved in pickle file")

    except Exception as e:
        logging.info("Exception has occured while saving a file")
        raise CustomException(e)

def load_object(filepath):
    try:
        logging.info("Opening the filepath ..")
        with open(filepath,'rb') as f:
            return pickle.load(f)
    except Exception as e:
        logging.info("Exception occured while loading the object")
        raise CustomException(e)

def evaluate_model(models,X_train,y_train,X_test,y_test):
    try:
        logging.info("Fitting and Evaluating the models based on r2 score...")
        r2scores = {}
        model_object_dict={}

        for model_name,model_class in models.items():
            model_object=model_class.fit(X_train,y_train)
            y_pred=model_object.predict(X_test)

            model_object_dict[model_name]=model_object

            r2 =r2_score(y_test,y_pred)
            r2scores[model_name]=r2
        
        max=0
        best_model=""
        for key,val in r2scores.items():
            if val>max:
                max=val
                best_model=key
        
        logging.info("Model evalution is successful")

        logging.info(f"Out of all models {best_model} has a highest accuracy of {max*100} .")
        print(f"Out of all models {best_model} has a highest accuracy of {max*100} .")

        return  (model_object_dict[best_model],r2scores)
            
    except Exception as e:
        logging.info("Exception has occurred during evalution function inside utils")
        raise CustomException(e)

    