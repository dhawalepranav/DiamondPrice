import os
import pandas as pd
import sys

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from src.utils import load_object

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            self.features = features
            logging.info("Loading the Pipeline object and Best score model..")

            preprocessor_path="D:\\Data science\\INeuron\\INeuron Machine Learning Materials\\Project\\artifacts\\preprocessor.pkl"
            model_path="D:\\Data science\\INeuron\\INeuron Machine Learning Materials\\Project\\artifacts\\best_score_model.pkl"

            preprocessor = load_object(preprocessor_path)
            model =load_object(model_path)

            logging.info("Scaling the input data and prediction the result for it")
            scaled_input_data = preprocessor.transform(features)
            output_result = model.predict(scaled_input_data)

            return output_result
        
        except Exception as e:
            logging.info("Exception occurred inside predict method of PredictionPipeline")
            raise CustomException(e)

class PredictionPipelineDataPrepare:

    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity
    
    def dataframegeneration(self):
        try:

            data={
                'carat':[self.carat],
                    'depth':[self.depth],
                    'table':[self.table],
                    'x':[self.x],
                    'y':[self.y],
                    'z':[self.z],
                    'cut':[self.cut],
                    'color':[self.color],
                    'clarity':[self.clarity]
            }

            df=pd.DataFrame(data)
            return df
        except Exception as e:
            logging.info("Exception occurred while data frame generation inside Prediction pipeline")
            raise CustomException(e)

        







