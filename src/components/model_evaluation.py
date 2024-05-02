import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception

import os 
import sys
from dataclasses import dataclass
from pathlib import Path

from src.utils.utils import load_object, evaluate_model
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error


@dataclass
class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self) -> None:
        pass

    def initiate_model_evaluation(self) -> None:
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e, sys)