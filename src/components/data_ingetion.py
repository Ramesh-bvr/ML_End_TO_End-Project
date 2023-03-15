import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngetionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


class DataIngetion:
    def __init__(self):
        self.ingetion_config = DataIngetionConfig()
    
    def intiate_data_ingetion(self):
        logging.info("Enter the data ingetion method or component")
        try:
            df = pd.read_csv("")
        except:
            pass

