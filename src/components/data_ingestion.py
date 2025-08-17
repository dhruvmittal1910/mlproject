# code related to data ingestion
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    # train data stored in artifact folder, defining location where we want to store train,test and raw data
    train_data_path:str=os.path.join('artifact',"train.csv")
    test_data_path:str=os.path.join('artifact',"test.csv") 
    raw_data_path:str=os.path.join('artifact',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        # read code from database here maybe aws, mongodb or anywhere
        
        logging.info("Entered the data ingestion method")
        
        try:
            print("read the dataset form different sources")
            df=pd.read_csv('notebook/data/StudentsPerformance.csv')
            
            logging.info("Read the dataset into df-dataframe")
            
            # exists_ok=true--- checks if the file is alreadu there or not
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.15,random_state=42)
            
            logging.info("saving train and test data to csv files")
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion of the data is completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()