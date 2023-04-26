import os
import sys
import pickle
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
import pandas as pd
import numpy as np
from dataclasses import dataclass

@dataclass
class DataTransformconfig:
    preprocessor_path=os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.DataTransformation=DataTransformconfig()
    
    def PipelineObject(self,num_features,cat_features,cat_features_ranking):
        logging.info("Creating Pipeline Object...")

        try:

            num_cols=num_features 
            cat_cols=cat_features 

            cat_features_ranking=cat_features_ranking 

            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
                ]
            )

            categorical_pipeline = Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('encoder',OrdinalEncoder(categories=cat_features_ranking)),
                ('scaler',StandardScaler())
                ]
            )

            preprocessor=ColumnTransformer(
                [
                ('num_pipeline',num_pipeline,num_cols),
                ('cat_pipeline',categorical_pipeline,cat_cols)
                ]
            )
            logging.info("Pipeline object has been created successfully")

            return preprocessor
        
        except Exception as e:
            logging.info("Exception has occurred inside Pipeline obj class at Data Transform method")
            raise CustomException(e)
    
    def Initiate_data_transform(self,train_data_path,test_data_path):

        logging.info("Data tranformation has been initiated..")

        try:

            logging.info("Reading the train and test data...")
            train_data=pd.read_csv(train_data_path)
            test_data=pd.read_csv(test_data_path)

            X_train=train_data.drop(['price','id'],axis=1)
            X_test=test_data.drop(['price','id'],axis=1)

            y_train=train_data[['price']]
            y_test=test_data[['price']]
            
            logging.info(f"X_train and y_train data is as following \n\n { str(X_train.head())},\n\n {str(y_train.head())}")

            logging.info(f"X_test and y_test data is as following \n\n {str(X_test.head())},\n\n {str(y_test.head())}")

            logging.info("Defining the Numerical and Categorical features")

            num_features=X_train.columns[X_train.dtypes != 'object'] #defining the numerical features
            cat_features=X_train.columns[X_train.dtypes == 'object'] #defining the categorical feature

            logging.info("Defining the rankings of categorical features")

            cut_categories=['Fair','Good','Very Good','Premium','Ideal']
            color_categories=['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories=['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            cat_features_ranking=[cut_categories,color_categories,clarity_categories]

            preprocessor=self.PipelineObject(num_features,cat_features,cat_features_ranking)

            logging.info("Applying the Pipeline on X_train and X_test data")

            X_train_scaled=preprocessor.fit_transform(X_train)
            X_test_scaled=preprocessor.transform(X_test)

            logging.info("Creating a Numpy array for train data and test data for optimising model training")

            train_data_arr =np.c_[X_train_scaled,np.array(y_train)]
            test_data_arr =np.c_[X_test_scaled,np.array(y_test)]

            logging.info("Saving the Pipeline object to a Pickle file")
            save_object(self.DataTransformation.preprocessor_path,preprocessor)

            logging.info("Data Transformation is successful.")

            return(
                train_data_arr,
                test_data_arr,
                self.DataTransformation.preprocessor_path
            )
        
        except Exception as e:
            logging.info("Exception has occurred inside Data Transformation - Initiate data transformation method")
            raise CustomException(e)








