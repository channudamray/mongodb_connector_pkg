import os
import sys
from src.logger.logging import logging
from src.exception.exception import customexception
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

if __name__ == "__main__":
    data_ingestion_obj=DataIngestion()
    data_transformation=DataTransformation()
    model_trainer_obj=ModelTrainer()
    model_eval_obj = ModelEvaluation()

    train_data_path,test_data_path=data_ingestion_obj.initiate_data_ingestion()
    train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)
    model_trainer_obj.initate_model_training(train_arr,test_arr)
    model_eval_obj.initiate_model_evaluation(train_arr,test_arr)