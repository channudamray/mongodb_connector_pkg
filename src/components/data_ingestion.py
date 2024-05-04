import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception
from typing import Tuple
import os 
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    dataset_path:str = os.path.join('playground-series-s3e8','train.csv')

class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self) -> Tuple[str,str]:
        logging.info("Data ingestion is started")
        try:
            logging.info("Reading a dataframe")
            data = pd.read_csv(self.ingestion_config.dataset_path)
            
            logging.info(f"Saving the raw data to {self.ingestion_config.raw_data_path}")
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)))
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            
            logging.info("Saving the training & testing data to artifacts folder")
            train_data, test_data = train_test_split(data, test_size=0.25, random_state=42)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info("Error data ingestion part!")
            raise customexception(e, sys)