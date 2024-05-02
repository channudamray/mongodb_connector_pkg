import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception

import os 
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    pass

class DataIngestion:
    def __init__(self) -> None:
        pass

    def initiate_data_ingestion(self) -> None:
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e, sys)