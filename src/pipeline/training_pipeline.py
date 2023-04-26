from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_training_and_eval import Model_Evaluation_Initiated

if __name__=="__main__":
    Data_ingestion_obj = DataIngestion()
    train_data,test_data = Data_ingestion_obj.Initiate_data_ingestion()
    Data_tranformation_obj =DataTransformation()
    train_data_scaled,test_data_scaled,Pipeline_obj =Data_tranformation_obj.Initiate_data_transform(train_data,test_data)
    Model_training_obj = Model_Evaluation_Initiated()
    best_score_model=  Model_training_obj.Model_Training(train_data_scaled,test_data_scaled)
