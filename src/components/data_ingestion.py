import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class Data_ingestion_Config:

    logging.info("Creating the paths for Train, Test and Raw files...")

    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:

    def __init__(self):
        self.ingestionconfig=Data_ingestion_Config()

    def Initiate_data_ingestion(self):
        logging.info("Initiating the Data Ingestion Process")

        try:
            logging.info("Reading the Data from source...")
            os.makedirs(os.path.join(os.getcwd(),'artifacts'),exist_ok=True)
            df=pd.read_csv('D:\\Data science\\INeuron\\INeuron Machine Learning Materials\\Project\\Notebooks\\data\\gemstone.csv')

            logging.info("Performing the train test split...")
            train_data,test_data=train_test_split(df,test_size=0.30,random_state=42)
            logging.info("Train test data split is successful...")

            logging.info("Saving raw data , train data, test data")
            train_data.to_csv(self.ingestionconfig.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestionconfig.test_data_path,index=False,header=True)
            df.to_csv(self.ingestionconfig.raw_data_path,index=False,header=True)
            logging.info("Data Ingestion is complete.")

            return(self.ingestionconfig.train_data_path,self.ingestionconfig.test_data_path)

        except Exception as e:
            logging.info("Exception has occurred")
            raise CustomException(e)

'''if __name__=="__main__":
    a=DataIngestion()
    print(a.Initiate_data_ingestion())'''

