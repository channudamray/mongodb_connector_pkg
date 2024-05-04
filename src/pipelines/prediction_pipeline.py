import os
import sys
import pandas as pd

from src.exception.exception import customexception
from src.logger.logging import logging
from src.utils.utils import load_object

class PredictPipeline:
    
    def __init__(self) -> None:
        print("Calling from __init__")
    
    def predict(self, features: pd.DataFrame):
        try:
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor_obj = load_object(preprocessor_path)
            model_obj = load_object(model_path)
            
            transformed_data = preprocessor_obj.transform(features)
            pred = model_obj.predict(transformed_data)

            return pred

        except Exception as e:
            logging.error("Error in predict method of PredictPipeline class")
            raise customexception(e, sys)

class CustomData:
    def __init__(self) -> None:
        pass
    def get_data_as_df(self, data):
        try:
            df = pd.DataFrame(data, index=[0])
            return df
        except Exception as e:
            logging.error("Error in get_data_as_df method of CustomData class")
            raise customexception(e, sys)