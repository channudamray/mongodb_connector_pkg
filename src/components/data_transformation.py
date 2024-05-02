import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception

import os 
import sys
from dataclasses import dataclass
from pathlib import Path

from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


@dataclass
class DataTransformationConfig:
    pass

class DataTransformation:
    def __init__(self) -> None:
        pass

    def initiate_data_transformation(self) -> None:
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e, sys)