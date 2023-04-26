from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
if __name__=="__main__":
    a=DataIngestion()
    train_data,test_data=a.Initiate_data_ingestion()
    b=DataTransformation()
    train_data_scaled,test_data_scaled,Pipeline_obj=b.Initiate_data_transform(train_data,test_data)